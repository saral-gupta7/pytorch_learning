import torch
import time

x_val = 2.0
RUNS = 10_000

# --- With grad tracking ---
start = time.time()
for _ in range(RUNS):
    x = torch.tensor(x_val, requires_grad=True)
    f = 3 * x**3 - 2 * x**2 + 5 * x - 1
with_grad = time.time() - start

# --- Without grad tracking ---
start = time.time()
for _ in range(RUNS):
    with torch.no_grad():
        x = torch.tensor(x_val)
        f = 3 * x**3 - 2 * x**2 + 5 * x - 1
without_grad = time.time() - start

ratio = with_grad / without_grad
print(f"With grad:    {with_grad:.4f}s")
print(f"Without grad: {without_grad:.4f}s")
print(f"Speedup:      {ratio:.2f}x faster with no_grad")
