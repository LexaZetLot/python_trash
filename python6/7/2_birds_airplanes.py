from matplotlib import pyplot as plt
from torchvision import datasets, transforms
import torch.nn as nn
import numpy as np
import torch
import torch.optim as optim

class_names = ['airplane','automobile','bird','cat','deer',
               'dog','frog','horse','ship','truck']

data_path = '../data-unversioned/p1ch7/'
cifar10 = datasets.CIFAR10(
    data_path, train=True, download=False,
    transform=transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.4915, 0.4823, 0.4468),
                             (0.2470, 0.2435, 0.2616))
    ]))

cifar10_val = datasets.CIFAR10(
    data_path, train=False, download=False,
    transform=transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.4915, 0.4823, 0.4468),
                             (0.2470, 0.2435, 0.2616))
    ]))

label_map = {0: 0, 2: 1}
class_names = ['airplane', 'bird']
cifar2 = [(img, label_map[label])
          for img, label in cifar10
          if label in [0, 2]]
cifar2_val = [(img, label_map[label])
              for img, label in cifar10_val
              if label in [0, 2]]

n_out = 2
mobel = nn.Sequential(nn.Linear(3072, 512), nn.Tanh(), nn.Linear(512, n_out))

def softmax(x):
    return torch.exp(x) / torch.exp(x).sum()

x = torch.tensor([1.0, 2.0, 3.0])
print(softmax(x))
print(softmax(x).sum())

softmax = nn.Softmax(dim=1)
x = torch.tensor([[1.0, 2.0, 3.0],
                  [1.0, 2.0, 3.0]])
print(softmax(x))

model = nn.Sequential(
    nn.Linear(3072, 512),
    nn.Tanh(),
    nn.Linear(512, 2),
    nn.Softmax(dim=1))

img, _ = cifar2[0]
plt.imshow(img.permute(1, 2, 0))
plt.show()

img_batch = img.view(-1).unsqueeze(0)
out = model(img_batch)
print(out)

_, index = torch.max(out, dim=1)
print(index)

model = nn.Sequential(
    nn.Linear(3072, 512),
    nn.Tanh(),
    nn.Linear(512, 2),
    nn.LogSoftmax(dim=1)
)

loss = nn.NLLLoss()

img, label = cifar2[0]
out = model(img.view(-1).unsqueeze(0))
print(loss(out, torch.tensor([label])))


#model = nn.Sequential(
#    nn.Linear(3072, 512),
#    nn.Tanh(),
#    nn.Linear(512, 2),
#    nn.LogSoftmax(dim=1))
#
#learning_rate = 1e-2
#optimizer = optim.SGD(model.parameters(), lr=learning_rate)
#loss_fn = nn.NLLLoss()
#
#n_epochs = 100
#for epoch in range(n_epochs):
#    for img, label in cifar2:
#        out = model(img.view(-1).unsqueeze(0))
#        loss = loss_fn(out, torch.tensor([label]))
#
#        optimizer.zero_grad()
#        loss.backward()
#        optimizer.step()
#
#    print("Epoch: %d, Loss: %f" % (epoch, float(loss)))

train_loader = torch.utils.data.DataLoader(cifar2, batch_size=64, shuffle=True)

model = nn.Sequential(
    nn.Linear(3072, 512),
    nn.Tanh(),
    nn.Linear(512, 2),
    nn.LogSoftmax(dim=1))

learning_rate = 1e-2
optimizer = optim.SGD(model.parameters(), lr=learning_rate)
loss_fn = nn.NLLLoss()

n_epochs = 100
for epoch in range(n_epochs):
    for imgs, labels in train_loader:
        batch_size = imgs.size(0)
        outputs = model(imgs.view(batch_size, -1))
        loss = loss_fn(outputs, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    print("Epoch: %d, Loss: %f" % (epoch, float(loss)))

val_loader = torch.utils.data.DataLoader(cifar2_val, batch_size=64, shuffle=True)

correct = 0
total = 0

with torch.no_grad():
    for imgs, labels in val_loader:
        batch_size = imgs.shape[0]
        outputs = model(imgs.view(batch_size, -1))
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += int((predicted == labels).sum())
print("Accuracy: %f", correct / total)

model = nn.Sequential(
            nn.Linear(3072, 1024),
            nn.Tanh(),
            nn.Linear(1024, 512),
            nn.Tanh(),
            nn.Linear(512, 128),
            nn.Tanh(),
            nn.Linear(128, 2),
            nn.LogSoftmax(dim=1))

numel_list = [p.numel()
    for p in model.parameters()
    if p.requires_grad == True]
print(sum(numel_list), numel_list)

