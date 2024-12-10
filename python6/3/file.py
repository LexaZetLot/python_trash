import torch

a = torch.tensor(list(range(9)))
print(a)
print(a.shape)
print(a.stride())

b = a.view(3, 3)
print(b)

print(id(a.untyped_storage()) == id(b.untyped_storage()))

c = b[1: ,1:]
print(c)
torch.cos(a)
print(torch.cos(a))

a.cos()
print(a)
