import torch
import torch.nn as nn
from torch.nn import functional as F
import config
torch.manual_seed(config.SEED)

class Bigram(nn.Module):
    def __init__(self, vocab_size):
        super().__init__()
        self.tok_emb_table = nn.Embedding(vocab_size, vocab_size)
    def forward(self, inputs, targets=None):
        logits = self.tok_emb_table(inputs)
        if targets is None:
            loss = None
        else:
            B, T, C = logits.shape
            logits = logits.view(B * T, C)
            targets = targets.view(B * T)
            loss = F.cross_entropy(logits, targets)
        return logits, loss

class DecoderBlock(nn.Module):
    def __init__(self, emb_size, context_window, num_heads, dropout):
        super().__init__()
        head_size = emb_size // num_heads
        self.self_attention = nn.Sequential(
            MultiHeadedAttention(emb_size, head_size, context_window, num_heads, dropout),
            nn.Dropout(dropout),
            nn.Linear(emb_size, emb_size)
        )
        self.norm1 = nn.LayerNorm(emb_size)
        self.ffwd = nn.Sequential(
            nn.Linear(emb_size, emb_size * 4),
            nn.ReLU(),
            nn.Linear(emb_size * 4, emb_size),
            nn.Dropout(dropout)
        )
        self.norm2 = nn.LayerNorm(emb_size)
    def forward(self, input):
        # residual connections
        input = self.self_attention(self.norm1(input)) + input
        input = self.ffwd(self.norm2(input)) + input
        return input

# emb_size is the size of the simple embedding for one token, containing the identity and position
class Transformer(nn.Module):
    def __init__(self, vocab_size, emb_size, context_window, num_blocks, num_heads, dropout):
        super().__init__()
        self.tok_emb_table = nn.Embedding(vocab_size, emb_size)
        self.pos_emb_table = nn.Embedding(context_window, emb_size)
        self.transform = nn.Sequential(
            *[DecoderBlock(emb_size, context_window, num_heads, dropout) for i in range(num_blocks)],
            nn.LayerNorm(emb_size),
            nn.Linear(emb_size, vocab_size)
        )
        self.head = nn.Linear(emb_size, vocab_size)
    def forward(self, inputs, targets=None, device=config.DEVICE):
        B, T = inputs.shape # B batches of T tokens. each token is just an integer of the token ID
        tok_emb = self.tok_emb_table(inputs) # B batches of T embeddings
        pos_emb = self.pos_emb_table(torch.arange(T, device=device)) # T position embeddings
        emb = tok_emb + pos_emb # combined embeddings, copies position embeddings across B batches
        logits = self.transform(emb)
        if targets is None:
            loss = None
        else:
            B, T, C = logits.shape
            logits = logits.view(B * T, C)
            targets = targets.view(B * T)
            loss = F.cross_entropy(logits, targets)
        return logits, loss

# head_size is the size of the complex embedding for one token, containing the actual meaning
# the context window is only for generating the lower triangular mask for the limited-context weights
class Head(nn.Module):
    def __init__(self, emb_size, head_size, context_window, dropout):
        super().__init__()
        self.generate_key = nn.Linear(emb_size, head_size, bias=False) # what information does this token contain?
        self.generate_query = nn.Linear(emb_size, head_size, bias=False) # what information is this token looking for in other tokens?
        self.generate_value = nn.Linear(emb_size, head_size, bias=False) # what information should this token contribute to the understanding of the context?
        self.register_buffer("tril", torch.tril(torch.ones(context_window, context_window)))
        self.dropout = nn.Dropout(dropout)
    def forward(self, tok_emb):
        B, T, C = tok_emb.shape # B batches of T tokens. each token has an embedding of size C
        key = self.generate_key(tok_emb)
        query = self.generate_query(tok_emb)
        weights = query @ key.transpose(-2, -1) * C**-0.5 # compare token query with other token keys to generate "affinities"
        weights = weights.masked_fill(self.tril[:T, :T] == 0, float("-inf")) # limited context (decoder): each token can only query itself and the tokens before it
        weights = F.softmax(weights, dim=-1) # dim=-1 softmaxes over each token; each token has some affinities with other tokens, and these affinities should sum to 1 for each token
        weights = self.dropout(weights)
        return weights @ self.generate_value(tok_emb) # B batches of T values (contextual information relevant to the token). each value is an embedding of size C
class MultiHeadedAttention(nn.Module):
    def __init__(self, emb_size, head_size, context_window, num_heads, dropout):
        super().__init__()
        self.heads = nn.ModuleList([Head(emb_size, head_size, context_window, dropout) for i in range(num_heads)])
    def forward(self, input):
        return torch.cat([head(input) for head in self.heads], dim=-1)

