import torch as t
from torch import nn
from PIL import Image
from torchvision.transforms import ToTensor, ToPILImage
to_tensor = ToTensor() # img -> tensor
to_pil = ToPILImage()
lena = Image.open('lena.png')

input = to_tensor(lena).unsqueeze(0) # 在第0维增加一个维度，相当于input = input[None]
kernel = t.ones(3,3)/-9.
kernel[1][1] = 1
conv = nn.Conv2d(3,1,(3,3),1,bias=False)
# conv.weight.data = kernel.view(1,3,3,3)
# 原始kernel是3x3，需要扩展为1x3x3，然后重复3次变为3x3x3，最后增加一个维度变为1x3x3x3
expanded_kernel = kernel.unsqueeze(0).repeat(3, 1, 1).unsqueeze(0)
conv.weight.data = expanded_kernel

out = conv(input)
output_image = to_pil(out.data.squeeze(0))
output_image.show()