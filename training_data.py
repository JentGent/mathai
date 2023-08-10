import os

import config

import torch
torch.manual_seed(config.SEED)

import numpy as np

# load all idek how many tokens into memory instead of loading them by batch ... is this a good idea?
# the data type is actually uint16, but as long as no token id is too big, int16 should be fine(?)
# pytorch doesn't support uint16 for some reason
DATA_TOKEN_IDS = torch.from_numpy(np.fromfile(os.path.join(os.path.dirname(__file__), "data.bin"), dtype=np.int16))
print(str(len(DATA_TOKEN_IDS)) + " training data tokens loaded successfully")
NUM_PROOFS = DATA_TOKEN_IDS[0] # 18273
DATA_TOKEN_IDS = DATA_TOKEN_IDS[2:]
# load 18273 indices into memory instead of searching for them for every batch
SECTION_INDICES = np.fromfile(os.path.join(os.path.dirname(__file__), "sections.bin"), dtype=np.uint32)
TRAIN_VAL_SPLIT = int(0.99 * len(DATA_TOKEN_IDS))

def get_batch(batch_size=1, validation=False):
    batches = torch.randint(TRAIN_VAL_SPLIT, len(DATA_TOKEN_IDS) - config.CONTEXT_WINDOW, (batch_size,)) if validation else torch.randint(TRAIN_VAL_SPLIT - config.CONTEXT_WINDOW, (batch_size,))
    inputs = torch.stack([DATA_TOKEN_IDS[i:i + config.CONTEXT_WINDOW] for i in batches])
    outputs = torch.stack([DATA_TOKEN_IDS[i + 1:i + 1 + config.CONTEXT_WINDOW] for i in batches])
    return inputs.to(config.DEVICE), outputs.to(config.DEVICE)


