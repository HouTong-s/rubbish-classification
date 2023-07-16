import torch
import torchvision
from PIL import Image
import os
from torchvision import transforms
import time
import torch.optim as optim
from mydatasets import MyDataset
from torch.utils.data import DataLoader
from torch.autograd import Variable
os.environ["CUDA_VISIBLE_DEVICES"]="0,1"
root =os.getcwd()+ '/DATASET/'
classes = ('可回收垃圾', '干垃圾', '湿垃圾', '有害垃圾')
preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
path = 'MyModel.pth' 
def get_variable(x):
    x = Variable(x)
    return x.cuda() if torch.cuda.is_available() else x
if __name__ == '__main__':
    #model = torch.load(path)
    #model = model.cuda()
    model = torch.load(path,map_location=torch.device('cpu'))
    model = model.to(torch.device('cpu'))
    if torch.cuda.is_available():
        model = model.cuda()
    test_data = MyDataset(txt=root+'test.txt', transform=preprocess)
    testing_correct = 0
    size = 1
    test_loader = DataLoader(dataset=test_data, batch_size=size, shuffle=True,num_workers=0)
    i=0
    for data in test_loader:
        with torch.no_grad():
            X_test, y_test = data
            X_test, y_test = get_variable(X_test),get_variable(y_test)
            outputs = model(X_test)
            
            _, pred = torch.max(outputs, 1) #返回每一行中最大值的那个元素，且返回其索引
            print(pred,y_test.data)
            testing_correct += torch.sum(pred == y_test.data)
            i += 1
            print("Total:{:d}  Test Accuracy is:{:.4f}%".format(i*size,
                100 * testing_correct / (i*size)))
    
