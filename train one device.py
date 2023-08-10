import torch
import models
import tokenizer
import config as cfg
import training_data

model = models.Transformer(tokenizer.VOCAB_SIZE, cfg.EMB_SIZE, cfg.CONTEXT_WINDOW, cfg.NUM_BLOCKS, cfg.NUM_HEADS, cfg.DROPOUT).to(cfg.DEVICE)

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
    logits, loss = model(inputs.to(torch.int32), targets.to(torch.long))
    optimizer.zero_grad(set_to_none=True)
    loss.backward()
    optimizer.step()
print(loss.item())

import generate
context = torch.tensor([[2]], dtype=torch.int, device=cfg.DEVICE)
print(tokenizer.decode(generate.generate(model, context, 256, cfg.CONTEXT_WINDOW)[0].tolist()))
