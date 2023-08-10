import torch

# Model
# vocab size is in tokenizer.py
CONTEXT_WINDOW = 256
EMB_SIZE = 300
NUM_BLOCKS = 6
NUM_HEADS = 6

# Training
SEED = 1337
BATCH_SIZE = 32
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
print(DEVICE)
ITERS = 500
RATE = 0.0003
EVAL_INTERVAL = 500
EVAL_ITERS = 100
DROPOUT = 0.2


