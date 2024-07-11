import torch
import torchvision
import torchvision.transforms as transforms
import torch.optim as optim
import matplotlib.pyplot as plt
from model_detect import MNIST_Net

# 数据加载和预处理
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
trainset = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)

testset = torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=64, shuffle=False)

# 网络初始化
net = MNIST_Net()


# 定义损失函数和优化器
criterion = torch.nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

# 训练网络
epochs = 10
train_losses, test_accuracies = [], []

for epoch in range(epochs):
    running_loss = 0.0
    for i, data in enumerate(trainloader, 0):
        inputs, labels = data
        optimizer.zero_grad()
        outputs = net(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        running_loss += loss.item()
    train_losses.append(running_loss / len(trainloader))
    
    correct = 0
    total = 0
    with torch.no_grad():
        for data in testloader:
            images, labels = data
            outputs = net(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    # test_accuracies.append(100 * correct / total)
    accuracy = 100 * correct / total
    test_accuracies.append(accuracy)
    
    # 打印每个epoch的训练损失和测试准确率
    #print(f"Epoch {epoch+1}/{epochs} - Loss: {train_losses:.4f}, Accuracy: {accuracy:.2f}%")
    print(f"Epoch {epoch+1}/{epochs} - Loss: {train_losses[-1]:.4f}, Accuracy: {test_accuracies[-1]:.2f}%")

# 绘制Loss变化曲线图
plt.figure(figsize=(10,5))
plt.plot(train_losses, label='Training Loss')
plt.title('Training Loss')
plt.legend()
plt.savefig('training_loss.png')

# 绘制测试集正确率变化曲线图
plt.figure(figsize=(10,5))
plt.plot(test_accuracies, label='Test Accuracy')
plt.title('Test Accuracy')
plt.legend()
plt.savefig('test_accuracy.png')
# 保存模型
torch.save(net.state_dict(), './mnist_net.pth')