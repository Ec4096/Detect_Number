import torch as t
from torch import nn
class Linear(nn.Module):
    def __init__(self,in_features,out_features):
        super(Linear,self).__init__()
        #nn.Module.__init__(self)
        self.w = nn.Parameter(t.randn(in_features,out_features))
        self.b = nn.Parameter(t.randn(out_features))

    def forward(self,x):
        x = x.mm(self.w)
        return x +self.b.expand_as(x)


# layer = Linear(4,3)
# input = t.randn(2,4)
# output = layer(input)
# print(output)

class Perceptron(nn.Module):
    def __init__(self, in_features, hidden_features, out_features):
        super(Perceptron, self).__init__()
        self.layer1 = Linear(in_features, hidden_features)
        self.layer2 = Linear(hidden_features, out_features)

    def forward(self, x):
        x = self.layer1(x)
        x = t.sigmoid(x)
        return self.layer2(x)
    
perceptron = Perceptron(3,4,1)
# for name, param in perceptron.named_parameters():
#     print(name, param.size())


# from PIL import Image
# #from torchvision.transforms import ToTensor, ToPILImage
# from torchvision import transforms

# to_tensor = transforms.ToTensor()
# to_pil = transforms.ToPILImage()
# lena = Image.open('lena.png')

# num_list = list(x**y for x in range(10) for y in range(10) if x==y)
# print(num_list)

