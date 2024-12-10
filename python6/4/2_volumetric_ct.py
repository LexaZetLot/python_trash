import imageio
import torch

dir_path = "../data/p1ch4/volumetric-dicom /2_LUNG_3_0_B70f_04083"
vol_arr = imageio.volread(dir_path, 'DICOM')
print(vol_arr.shape)

vol = torch.from_numpy(vol_arr).float()
vol = torch.unsqueeze(vol, 0)
print(vol.shape)