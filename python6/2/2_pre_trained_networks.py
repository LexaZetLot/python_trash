from torchvision import models
import torch
from torchvision import transforms
from PIL import Image

print(dir(models))

alexnet = models.AlexNet()

resnet = models.resnet101(pretrained=True)
print(resnet)

preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
)])

img = Image.open('../data/p1ch2/bobby.jpg')
Image._show(img)
img_t = preprocess(img)

batch_t = torch.unsqueeze(img_t, 0)

resnet.eval()


output = resnet(batch_t)
print(output)

with open('../data/p1ch2/imagenet_classes.txt') as f:
    labels = [line.strip() for line in f.readlines()]

_, index = torch.max(output, 1)

percentage = torch.nn.functional.softmax(output, dim=1)[0] * 100
print(labels[index[0]], percentage[index[0]].item())

_, indices = torch.sort(output, descending=True)
print([(labels[idx], percentage[idx].item()) for idx in indices[0][:5]])