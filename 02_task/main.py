import torch

# x = torch.tensor([3.0], requires_grad=True)


# f = 3 * x**3 - 2 * x**2 + 5 * x - 1
# g = torch.sin(x**2)

# # print(f"f(2)  = {f.item()}")

# f.backward(retain_graph=True)
# # g.backward()

# # f.backward()
# x.grad.zero_()

# print(f"f'(2)  = {x.grad.item()}")
# # print(f"f'(2)  = {x.grad.item()}")

# f.backward(retain_graph=True)

w = torch.tensor([2.0], requires_grad=True)
b = torch.tensor([1.0], requires_grad=True)


loss = (w * 3.0 + b - 0.5) ** 2

loss.backward()

print(f"d(loss)/dw is {w.grad.item()}")
print(f"d(loss)/db is {b.grad.item()}")
