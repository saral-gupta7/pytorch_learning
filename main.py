import torch

x = torch.rand(3, 4)


if torch.cuda.is_available():
    print("GPU is available")
else:
    print("Gpu is not available")

print(x.device)
# print(x)
