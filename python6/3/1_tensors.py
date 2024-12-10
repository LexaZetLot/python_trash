import torch
import h5py

a = [1.0, 2.0, 1.0]
print(a[0])
a[2] = 3.0
print(a)

a = torch.ones(3)
print(a)
print(a[1])
print(float(a[1]))
a[2] = 2.0
print(a)

points = torch.zeros(6)
points[0] = 4.0
points[1] = 1.0
points[2] = 5.0
points[3] = 3.0
points[4] = 2.0
points[5] = 1.0

points = torch.tensor([4.0, 1.0, 5.0, 3.0, 2.0, 1.0])
print(points)
print((float(points[0]), float(points[1])))

points = torch.tensor([[4.0, 1.0], [5.0, 3.0], [2.0, 1.0]])
print(points)
print(points.shape)

points = torch.zeros(3, 2)
print(points)

points = torch.tensor([[4.0, 1.0], [5.0, 3.0], [2.0, 1.0]])
print(points)
print(points[0, 1])
print(points[0])

some_list = list(range(6))
print(some_list[:])
print(some_list[1:4])
print(some_list[1:])
print(some_list[:4])
print(some_list[:-1])
print(some_list[1:4:2])

print(points[1:])
print(points[1:,:])
print(points[1:, 0])
print(points[None])

double_points = torch.ones(10, 2, dtype=torch.double)
short_points = torch.tensor([[1, 2], [3, 4]], dtype=torch.short)

print(short_points.dtype)

double_points = torch.zeros(10, 2).double()
short_points = torch.ones(10, 2).short()

double_points = torch.zeros(10, 2).to(torch.double)
short_points = torch.ones(10, 2).to(torch.short)

points_64 = torch.rand(5, dtype=torch.double)
points_short = points_64.to(torch.short)
print(points_64 * points_short)

a = torch.ones(3, 2)
a_t = torch.transpose(a, 0, 1)
print(a.shape, a_t.shape)

a = torch.ones(3, 2)
a_t = a.transpose(0, 1)
print(a.shape, a_t.shape)

points = torch.tensor([[4.0, 1.0], [5.0, 3.0], [2.0, 1.0]])
print(points.storage())

points_storage = points.storage()
print(points_storage[0])
print(points.storage()[1])

points = torch.tensor([[4.0, 1.0], [5.0, 3.0], [2.0, 1.0]])
points_storage = points.storage()
points_storage[0] = 2.0
print(points)

a = torch.ones(3, 2)
a.zero_()
print(a)

points = torch.tensor([[4.0, 1.0], [5.0, 3.0], [2.0, 1.0]])
second_point = points[1]
second_point.storage_offset()
print(second_point.storage_offset())
print(second_point.size())
print(second_point.shape)
print(points.stride())

print(second_point.storage_offset())
print(second_point.stride())

points = torch.tensor([[4.0, 1.0], [5.0, 3.0], [2.0, 1.0]])
second_point = points[1]
second_point[0] = 10.0
print(points)

points = torch.tensor([[4.0, 1.0], [5.0, 3.0], [2.0, 1.0]])
second_point = points[1].clone()
second_point[0] = 10.0
print(points)

points = torch.tensor([[4.0, 1.0], [5.0, 3.0], [2.0, 1.0]])
print(points)
points_t = points.t()
print(points_t)

print(id(points.storage()) == id(points_t.storage()))
print(points.stride())
print(points_t.stride())

some_t = torch.ones(3, 4, 5)
transpose_t = some_t.transpose(0, 2)
print(some_t.shape)
print(transpose_t.shape)
print(some_t.stride())
print(transpose_t.stride())

print(points.is_contiguous())
print(points_t.is_contiguous())

points = torch.tensor([[4.0, 1.0], [5.0, 3.0], [2.0, 1.0]])
points_t = points.t()
print(points_t)

print(points_t.storage())

print(points_t.stride())

points_t_cont = points_t.contiguous()
print(points_t_cont)

print(points_t_cont.stride())

print(points_t_cont.storage())

points_gpu = torch.tensor([[4.0, 1.0], [5.0, 3.0], [2.0, 1.0]], device='cuda')
points_gpu = points.to(device='cuda')

points_gpu = points.to(device='cuda:0')
points = 2 * points
points_gpu = 2 * points.to(device='cuda')

points_gpu = points_gpu + 4
points_cpu = points_gpu.to(device='cpu')

points_gpu = points.cuda()
points_gpu = points.cuda(0)
points_cpu = points_gpu.cpu()

points = torch.ones(3, 4)
points_np = points.numpy()
print(points_np)

points = torch.from_numpy(points_np)

torch.save(points, '../data/p1ch3/ourpoints.t')

with open('../data/p1ch3/ourpoints.t','wb') as f:
    torch.save(points, f)

points = torch.load('../data/p1ch3/ourpoints.t')

with open('../data/p1ch3/ourpoints.t','rb') as f:
    points = torch.load(f)

f = h5py.File('../data/p1ch3/ourpoints.hdf5', 'w')
dset = f.create_dataset('coords', data=points.numpy())
f.close()

f = h5py.File('../data/p1ch3/ourpoints.hdf5', 'r')
dset = f['coords']
last_points = dset[-2:]

last_points = torch.from_numpy(dset[-2:])
f.close()