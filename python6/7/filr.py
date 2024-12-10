import torch
import torchvision.transforms
from matplotlib import pyplot as plt
from torch import nn, optim
from torchvision import datasets, transforms


data_path = '../data-unversioned/p1ch7/'
cifar10 = datasets.CIFAR10(
    data_path, train=True, download=False,
    transform=transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.4915, 0.4823, 0.4468),
                             (0.2470, 0.2435, 0.2616))
    ]))


img, _ = cifar10[0]

img = torchvision.transforms.RandomCrop(32, padding=4)(img)
#plt.imshow(img.permute(1, 2, 0))
#plt.show()


train_loader = torch.utils.data.DataLoader(cifar10, batch_size=64, shuffle=True)


model = nn.Sequential(
    nn.Linear(3072, 512),
    nn.Tanh(),
    nn.Linear(512, 10),
    nn.Softmax(dim=1))

learning_rate = 1e-2
optimizer = optim.SGD(model.parameters(), lr=learning_rate)
loss_fn = nn.MSELoss()

n_epochs = 100
for epoch in range(n_epochs):
    for imgs, labels in train_loader:
        batch_size = imgs.size(0)
        outputs = model(imgs.view(batch_size, -1))
        _, outputs = torch.max(outputs, dim=1)

        outputs = outputs.float() / 10
        labels = labels.float() / 10


        loss = loss_fn(outputs, labels)

        optimizer.zero_grad()
        loss.requires_grad = True
        loss.backward()
        optimizer.step()

    print("Epoch: %d, Loss: %f" % (epoch, float(loss)))
