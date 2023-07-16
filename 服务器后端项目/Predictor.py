# -*- coding: utf-8 -*-
import torch
import torchvision
from PIL import Image
from torchvision import transforms

class predictor:
    def __init__(self) -> None:
        path = 'MyModel.pth'
        self.model = torch.load(path, map_location='cpu')
        self.model = self.model.to(torch.device("cpu"))
    def predict(self,picture):
        classes = ('可回收垃圾', '干垃圾', '湿垃圾', '有害垃圾')

        input_image = Image.open(picture).convert('RGB')
        preprocess = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])
        input_tensor = preprocess(input_image)
        input_batch = input_tensor.unsqueeze(0)
        with torch.no_grad():
            output = self.model(input_batch)
        _ , nums =torch.max(output,1)
        num = nums[0].item()
        class1 = classes[num]
        return class1
