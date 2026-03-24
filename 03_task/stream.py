import torch
import json


def train(lr=0.1):
    torch.manual_seed(42)
    X = torch.randn(100, 1)
    y = 3 * X + 2 + torch.randn(100, 1) * 0.3

    w = torch.randn(1, 1, requires_grad=True)
    b = torch.zeros(1, requires_grad=True)

    for epoch in range(100):
        y_pred = X @ w + b
        loss = ((y_pred - y) ** 2).mean()
        loss.backward()

        if w.grad is not None and b.grad is not None:
            with torch.no_grad():
                w -= lr * w.grad
                b -= lr * b.grad

                if w.grad is not None:
                    w.grad.zero_()
                if b.grad is not None:
                    b.grad.zero_()

        payload = {
            "epoch": epoch,
            "loss": round(loss.item(), 6),
            "w": round(w.item(), 4),
            "b": round(b.item(), 4),
        }

        yield f"data: {json.dumps(payload)}\n\n"


train(0.8)
