import csv

import numpy as np
import torch
from torch import nn, optim
from collections import OrderedDict


def training_loop(n_epochs, optimizer, model, loss_fn, t_u_train, t_u_val, t_c_train, t_c_val):
    for epoch in range(1, n_epochs + 1):
        t_p_train = model(t_u_train)
        loss_train = loss_fn(t_p_train, t_c_train)

        t_p_val = model(t_u_val)
        loss_val = loss_fn(t_p_val, t_c_val)

        optimizer.zero_grad()
        loss_train.backward()
        optimizer.step()

        if epoch == 1 or epoch % 1000 == 0:
            print(f"Epoch {epoch}, Training loss {loss_train.item():.4f},"
                  f" Validation loss {loss_val.item():.4f}")


wine_path = '../data/p1ch4/tabular-wine/winequality-white.csv'
wineq_numpy = np.loadtxt(wine_path, dtype=np.float32, delimiter=";", skiprows=1)
col_list = next(csv.reader(open(wine_path), delimiter=';'))

wineq = torch.from_numpy(wineq_numpy)

win_out = wineq[:,-1]
win_out.unsqueeze_(1)

win_input = wineq[:,:-1]
#win_input = win_input.view(-1, 11, 1)
print(win_input[2])
print(win_out[2])

n_samples = wineq.shape[0]
n_val = int(0.2 * n_samples)

shuffled_indices = torch.randperm(n_samples)

train_indices = shuffled_indices[:-n_val]
val_indices = shuffled_indices[-n_val:]

t_u_train = win_input[train_indices]
t_c_train = win_out[train_indices]

t_u_val = win_input[val_indices]
t_c_val = win_out[val_indices]

t_un_train = 0.1 * t_u_train
t_un_val = 0.1 * t_u_val

seq_model = nn.Sequential(OrderedDict([
    ('hidden_linear', nn.Linear(11, 28)),
    ('hidden_activation', nn.Tanh()),
    ('output_linear', nn.Linear(28, 1))
]))
optimizer = optim.SGD(seq_model.parameters(), lr=1e-3)


training_loop(
    n_epochs=5000,
    optimizer=optimizer,
    model=seq_model,
    loss_fn=nn.MSELoss(),
    t_u_train=t_un_train,
    t_u_val=t_un_val,
    t_c_train=t_c_train,
    t_c_val=t_c_val)




print('output', seq_model(t_un_val))
print('answer', t_c_val)
print('hidden', seq_model.hidden_linear.weight.grad)
print(win_input)

from matplotlib import pyplot as plt

t_range = torch.arange(20., 97.).unsqueeze(1)
t_range = t_range.view(-1, 11)
print(t_range)

fig = plt.figure(dpi=600)
plt.xlabel("Fahrenheit")
plt.ylabel("Celsius")
plt.plot(win_out.numpy(), win_out.numpy(), 'o')
plt.plot(t_range.numpy(), seq_model(0.1 * t_range).detach().numpy(), 'c-')
plt.plot(win_input.numpy(), seq_model(0.1 * win_input).detach().numpy(), 'kx')

plt.show()