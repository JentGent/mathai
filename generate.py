import torch
from torch.nn import functional as F
import tokenizer

def generate(model, input, num_new_tokens=100, context_window=0):
    next_char = 0
    i = 0
    while i < num_new_tokens and next_char != tokenizer.TOKEN_TO_INDEX["$}"]:
        i += 1
        logits, loss = model(input[:, -context_window:])
        logits = logits[:, -1, :]
        probs = F.softmax(logits, dim=-1)
        next_char = torch.multinomial(probs, num_samples=1)
        input = torch.cat((input, next_char), dim=1)
    return input
