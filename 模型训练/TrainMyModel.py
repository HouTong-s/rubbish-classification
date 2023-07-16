# -*- coding: utf-8 -*-
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
path = 'MyModel.pth'

def get_variable(x):
    x = Variable(x)
    return x.cuda() if torch.cuda.is_available() else x

if __name__ == '__main__':
    #model = torch.load(path)
    model = torch.load(path,map_location=torch.device('cpu'))
    model = model.to(torch.device('cpu'))
    criterion = torch.nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=0.0001, momentum=0.9)


    if torch.cuda.is_available():
        model = model.cuda()
    model = model.to(torch.device('cpu'))
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    train_data=MyDataset(txt=root+'train.txt', transform=preprocess)
    train_loader = DataLoader(dataset=train_data, batch_size=6, shuffle=True,num_workers=4)
    torch.cuda.empty_cache()
    for epoch in range(1):  # loop over the dataset multiple times
        running_loss = 0.0
        running_correct = 0.0
        for i, data in enumerate(train_loader, 0):
            #time_start=time.time()
            # get the inputs; data is a list of [inputs, labels]
            inputs, labels = data
            inputs, labels = get_variable(inputs), get_variable(labels)
            # zero the parameter gradients
            optimizer.zero_grad()
            #print(inputs.shape)
            # forward + backward + optimize
            outputs = model(inputs)
            _, pred = torch.max(outputs.data, 1)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            #print(loss.item())
            print(i)
            # print statistics
            running_loss += loss.item()
            running_correct += torch.sum(pred == labels.data)
            if i % 50 == 49:    # print every 20 mini-batches
                torch.save(model,path)
                print('[%d, %2d] loss: %.3f' %
                    (epoch + 1, i + 1, running_loss / 50))
                running_loss = 0.0
                
            #time_end=time.time()
            #print('totally cost',time_end-time_start)
    torch.save(model,path)






