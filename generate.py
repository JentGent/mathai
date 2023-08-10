import torch
from torch.nn import functional as F

def generate(model, input, num_new_tokens=100, context_window=0):
    for i in range(num_new_tokens):
        logits, loss = model(input[:, -context_window:])
        logits = logits[:, -1, :]
        probs = F.softmax(logits, dim=-1)
        next_char = torch.multinomial(probs, num_samples=1)
        input = torch.cat((input, next_char), dim=1)
    return input
