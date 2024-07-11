

# import torch
# import torch.nn as nn
# import torch.nn.functional as F

# class HandwrittenDigitModel(nn.Module):
#     def __init__(self):
#         super(HandwrittenDigitModel, self).__init__()
#         # 第一个卷积层，输入通道数1，输出通道数6，卷积核大小5x5
#         self.conv1 = nn.Conv2d(1, 6, kernel_size=(5,5), stride =(1,1),padding = (2,2))
#         # 第二个卷积层，输入通道数6，输出通道数64，卷积核大小5x5
#         self.conv2 = nn.Conv2d(6, 64, kernel_size=(5,5), stride =(1,1))
#         # 第一个线性层，输入特征数64*7*7，输出特征数120
#         self.fc1 = nn.Linear(in_features=400, out_features=120, bias=True)
#         # 第二个线性层，输入特征数120，输出特征数84
#         self.fc2 = nn.Linear(in_features=120,out_features=84, bias=True)
#         # 最后一个线性层，输入特征数84，输出特征数10
#         self.fc3 = nn.Linear(in_features=84, out_features=10, bias=True)

#     def forward(self, x):
#         # 通过第一个卷积层后接ReLU激活函数和2x2最大池化层
#         x = F.max_pool2d(F.relu(self.conv1(x)), kernel_size=2, stride=2,padding=0,dilation=1,ceil_mode=False)
#         # 通过第二个卷积层后接ReLU激活函数和2x2最大池化层
#         x = F.max_pool2d(F.relu(self.conv2(x)), kernel_size=2, stride=2,padding=0,dilation=1,ceil_mode=False)
#         # 展平特征图，准备输入到线性层
#         #x = x.view(-1, 64 * 7 * 7)
#         # 展平特征图，准备输入到线性层
#         x = x.view(-1, 400)
#         # 通过第一个线性层后接ReLU激活函数
#         x = F.relu(self.fc1(x),feature = 400,out_features = 120, bias=True)
#         # 通过第二个线性层后接ReLU激活函数
#         x = F.relu(self.fc2(x),feature = 120,out_features = 84, bias=True)
#         # 通过最后一个线性层
#         x = self.fc3(x)
#         return x


import torch
import torch.nn as nn
import torch.nn.functional as F

class MNIST_Net(nn.Module):
    def __init__(self):
        super(MNIST_Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 6, kernel_size=3)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 12, kernel_size=3)
        self.fc1 = nn.Linear(12 * 5 * 5, 160)
        self.fc2 = nn.Linear(160, 80)
        self.fc3 = nn.Linear(80, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 12 * 5 * 5)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

model = MNIST_Net()