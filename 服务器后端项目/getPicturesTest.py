import unittest
import random
import os

from getPictures import getpictures
arrs = ['可回收垃圾','干垃圾','湿垃圾','有害垃圾']
brrs = ['可回收垃圾','其他垃圾','厨余垃圾','有害垃圾']
class getpictures_test(unittest.TestCase):
    def get(self,class1,class2):
        if class1 == arrs[0]:
            class1 = brrs[0]
        elif class1 == arrs[1]:
            class1 = brrs[1]
        elif class1 == arrs[2]:
            class1 = brrs[2]
        elif class1 == arrs[3]:
            class1 = brrs[3]
        if class1 == "可回收垃圾":
            class3 = "可回收物"
        else:
            class3 = class1
        if class2 == None:   
            
            files = os.listdir("C:/Users/Administrator/Desktop/Pictures/"+class1)
            items = []
            for file in files:
                #print(file)
                if "_" in file and file != ".DS_Store":
                    items.append(file.split("_")[-1])
            return {"status": "0","data":items}
        else :
            files = os.listdir("C:/Users/Administrator/Desktop/Pictures/"+class1+"/"+class3+"_"+class2)
            random.shuffle(files)
            length = len(files)
            num = 10 if 10 < length else length
            items = []
            for i in range(0,length):
                if i < num:
                    items.append("http://139.224.50.124:8081/Pictures/"+class1+"/"+class3+"_"+class2+"/"+files[i])
            return {"status": "1","data":items}
    def test_get(self):
        #print(self.get("可回收垃圾", None))
        #两种请求方式，一种是查看一种类别的垃圾具体包括哪些种类(status:0)
        #一种是查看具体种类垃圾的图片url(status:1)
        self.assertTrue(self.get("可回收垃圾", None)["status"] == "0","request false")
        self.assertTrue(self.get("可回收垃圾","尺子")["status"] == "1","request false")
if __name__ == '__main__':
    unittest.main()
