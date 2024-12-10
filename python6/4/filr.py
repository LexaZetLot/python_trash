import os

import imageio.v2 as imageio
import torch

data_dir = '../data/p1ch4/'
filenames = [name for name in os.listdir(data_dir) if os.path.splitext(name)[-1] == '.jpg']
batch = []
print(os.path.splitext('red1.jpg'))

for filename in filenames:
    img_arr = imageio.imread(os.path.join(data_dir, filename))
    img_t = torch.from_numpy(img_arr)
    img_o = img_t.permute(2, 0, 1)
    img_o = img_o[:3]
    batch.append(img_o.float())


for batch in batch:
    print("ful", batch.mean())
    for i in range(1, 4):
        print(i, batch[:i].mean())