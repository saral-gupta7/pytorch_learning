import torch

x = torch.tensor(2.0, requires_grad=True)

with torch.no_grad():  # it does not compute the graph at all so during backward pass, pytorch has now knowledge of history.
    f = 3 * x**3 - 2 * x**2 + 5 * x - 1
    print(f.requires_grad)
    print(f.grad_fn)

    f.backward()

# Training — needs graph
