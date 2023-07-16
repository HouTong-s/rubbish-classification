# -*- coding: utf-8 -*-
import unittest

import torch
import torchvision
from PIL import Image
from torchvision import transforms
from Predictor import predictor
class predictor_test(unittest.TestCase):
    def test_init(self):
        
        path = 'MyModel.pth'
        self.model = torch.load(path, map_location='cpu')
        self.model = self.model.to(torch.device("cpu"))
        #判断模型是否加载成功，即不为空
        self.assertIsNotNone(self.model,"Load model failed")
    def test_predict(self):
        path = 'MyModel.pth'
        self.model = torch.load(path, map_location='cpu')
        self.model = self.model.to(torch.device("cpu"))
        classes = ('可回收垃圾', '干垃圾', '湿垃圾', '有害垃圾')
        pictures = ['./img/img_尺子_1.jpeg','./img/img_电池_15.jpeg','./img/img_毛巾_7.jpeg','./img/img_苹果_1.jpeg']
        input_images = []
        for picture in pictures:
            input_image = Image.open(picture).convert('RGB')
            input_images.append(input_image)
        preprocess = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])
        input_tensors = []
        for input_image in input_images:
            input_tensors.append(preprocess(input_image).unsqueeze(0))
        input_batch = input_tensors[0]
        for i in range(1,len(input_tensors)):
            input_batch = torch.cat((input_batch,input_tensors[i]),0)
        with torch.no_grad():
            output = self.model(input_batch)
        _ , nums =torch.max(output,1)
        num1 = nums[0].item()
        class1 = classes[num1]
        num2 = nums[1].item()
        class2 = classes[num2]
        num3 = nums[2].item()
        class3 = classes[num3]
        num4 = nums[3].item()
        class4 = classes[num4]

        #识别尺子出来结果是可回收垃圾
        self.assertTrue(class1 == "可回收垃圾","predict 1 false")
        #识别电池出来结果是有害垃圾
        self.assertTrue(class2 == "有害垃圾","predict 2 false")
        #识别毛巾出来结果是干垃圾
        self.assertTrue(class3 == "干垃圾","predict 3 false")
        #识别苹果出来结果是湿垃圾
        self.assertTrue(class4 == "湿垃圾","predict 4 false")
if __name__ == '__main__':
    unittest.main()