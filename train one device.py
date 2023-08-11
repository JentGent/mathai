import torch
import models
import tokenizer
import config as cfg
import training_data
import os

CHKPT = "checkpoint.pth"

model = models.Transformer(tokenizer.VOCAB_SIZE, cfg.EMB_SIZE, cfg.CONTEXT_WINDOW, cfg.NUM_BLOCKS, cfg.NUM_HEADS, cfg.DROPOUT).to(cfg.DEVICE)
optimizer = torch.optim.AdamW(model.parameters(), lr=0.001)

def save_checkpoint(model: torch.nn.Module, optimizer: torch.optim.Optimizer, loss, path):
    checkpoint = {
        "model": model.state_dict(),
        "optimizer": optimizer.state_dict(),
        "loss": loss
    }
    torch.save(checkpoint, path)

def load_checkpoint(model: torch.nn.Module, optimizer: torch.optim.Optimizer, path):
    checkpoint = torch.load(path)
    model.load_state_dict(checkpoint["model"])
    optimizer.load_state_dict(checkpoint["optimizer"])
    loss = checkpoint["loss"]
    return model, optimizer, loss

min_loss = float("inf")
if os.path.exists(CHKPT):
    model, optimizer, min_loss = load_checkpoint(model, optimizer, CHKPT)
    print("checkpoint loaded")

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
        if losses["val"] < min_loss:
            save_checkpoint(model, optimizer, losses["val"], CHKPT)
        print(f"step {iter}: val loss {losses['val']}, train loss {losses['train']}")
    inputs, targets = training_data.get_batch(cfg.BATCH_SIZE)
    logits, loss = model(inputs.to(torch.int32), targets.to(torch.long))
    optimizer.zero_grad(set_to_none=True)
    loss.backward()
    optimizer.step()

losses = estimate_loss()
if losses["val"] < min_loss:
    save_checkpoint(model, optimizer, losses["val"], CHKPT)
print(f"step {iter}: val loss {losses['val']}, train loss {losses['train']}")

import generate
# context = torch.tensor([[2]], dtype=torch.int, device=cfg.DEVICE)
context = torch.tensor([tokenizer.encode("""${
  mp2.1 $e |- ph $.
  mp2.2 $e |- ps $.
  mp2.3 $e |- ( ph -> ( ps -> ch ) ) $.
  mp2 $p |- ch $=""")], dtype=torch.int, device=cfg.DEVICE)
print(tokenizer.decode(generate.generate(model, context, 256, cfg.CONTEXT_WINDOW)[0].tolist()))
