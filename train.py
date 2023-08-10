import torch
import torch.nn as nn
import torch.distributed as dist
import models
import tokenizer
import config as cfg
import training_data
import os
import generate

def train(rank, world_size):
    print(f"running DDP on rank {rank}.")
    torch.manual_seed(0)

    os.environ['MASTER_ADDR'] = 'localhost'
    os.environ['MASTER_PORT'] = '12355'
    dist.init_process_group(backend='gloo', rank=rank, world_size=world_size)

    model = models.Transformer(tokenizer.VOCAB_SIZE, cfg.EMB_SIZE, cfg.CONTEXT_WINDOW, cfg.NUM_BLOCKS, cfg.NUM_HEADS, cfg.DROPOUT).to("cuda")
    model = nn.SyncBatchNorm.convert_sync_batchnorm(model)
    model = nn.parallel.DistributedDataParallel(model, device_ids=[rank])

    optimizer = torch.optim.AdamW(model.parameters(), lr=0.001)

    @torch.no_grad()
    def estimate_loss(iters=cfg.EVAL_ITERS):
        out = {}
        model.eval()
        for split in [True, False]:
            losses = torch.zeros(iters)
            for i in range(iters):
                inputs, targets = training_data.get_batch(validation=split)
                logits, loss = model(inputs.to(torch.int32), targets.to(torch.long))
                losses[i] = loss.item()
            out["val" if split else "train"] = losses.mean()
        model.train()
        return out

    for iter in range(cfg.ITERS):
        if iter == 0 or (iter + 1) % cfg.EVAL_INTERVAL == 0:
            losses = estimate_loss()
            print(f"step {iter}: val loss {losses['val']}, train loss {losses['train']}")
        inputs, targets = training_data.get_batch(cfg.BATCH_SIZE)
        optimizer.zero_grad(set_to_none=True)
        logits, loss = model(inputs.to(torch.int32), targets.to(torch.long))
        loss.backward()
        optimizer.step()

    context = torch.tensor([[2]], dtype=torch.int, device=cfg.DEVICE)
    print(tokenizer.decode(generate.generate(model, context, 256, cfg.CONTEXT_WINDOW)[0].tolist()))
    
    dist.destroy_process_group()

def main():
    world_size = torch.cuda.device_count()
    print(f"{world_size} GPUs")
    torch.multiprocessing.spawn(train, args=(world_size,), nprocs=world_size, join=True)

if __name__ == '__main__':
    main()

