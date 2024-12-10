import torch
from matplotlib import pyplot as plt
from torchvision import datasets, transforms
data_path = '../data-unversioned/p1ch7/'
cifar10 = datasets.CIFAR10(data_path, train=True, download=True)
cifar10_val = datasets.CIFAR10(data_path, train=False, download=True)

print(type(cifar10).__mro__, len(cifar10))
class_names = ['airplane','automobile','bird','cat','deer',
               'dog','frog','horse','ship','truck']


img, label = cifar10[99]
print(img, label, class_names[label])

plt.imshow(img)
plt.show()

print(dir(transforms))

to_tensor = transforms.ToTensor()
img_t = to_tensor(img)
print(img_t.shape)

tensor_cifar10 = datasets.CIFAR10(data_path, train=True, download=False, transform=transforms.ToTensor())
img_t, _ = tensor_cifar10[99]
print(type(img_t))

print(img_t.shape, img_t.dtype)
print(img_t.max(), img_t.min())

plt.imshow(img_t.permute(1,2,0))
plt.show()

imgs = torch.stack([img_t for img_t, _ in tensor_cifar10], dim=3)
print(imgs.shape)

print(imgs.view(3, -1).mean(dim=1))
print(transforms.Normalize((0.4915, 0.4823, 0.4468), (0.2470, 0.2435, 0.2616)))

transformed_cifar10 = datasets.CIFAR10(data_path, train=True, download=False,
                                       transform=transforms.Compose([
                                           transforms.ToTensor(),
                                           transforms.Normalize((0.4915, 0.4823, 0.4468),
                                                                (0.2470, 0.2435, 0.2616))
                                       ]))

img_t, _ = transformed_cifar10[99]
plt.imshow(img_t.permute(1,2,0))
plt.show()
