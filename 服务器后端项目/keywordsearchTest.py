import unittest
from keywordsearch import Ksearch
class Ksearch_test(unittest.TestCase):
    a1 = [] 
    a2 = [] 
    a3 = [] 
    a4 = [] 
    def test_init(self):
        self.a1 = []
        self.a2 = []
        self.a3 = []
        self.a4 = []
        with open("可回收垃圾.txt","r",encoding='UTF-8') as f:
            arr = f.readline().split(" ")
            for s in arr:
                self.a1.append(s)
        with open("干垃圾.txt","r",encoding='UTF-8') as f:
            arr = f.readline().split(" ")
            for s in arr:
                self.a2.append(s)
        with open("湿垃圾.txt","r",encoding='UTF-8') as f:
            arr = f.readline().split(" ")
            for s in arr:
                self.a3.append(s)
        with open("有害垃圾.txt","r",encoding='UTF-8') as f:
            arr = f.readline().split(" ")
            for s in arr:
                self.a4.append(s)
        #判断是否把txt文件中的关键字加载到了数组中
        self.assertTrue(len(self.a1)>0 ,"Load file failed")
        self.assertTrue(len(self.a2)>0 ,"Load file failed")
        self.assertTrue(len(self.a3)>0 ,"Load file failed")
        self.assertTrue(len(self.a4)>0 ,"Load file failed")
    def search(self,keyword):
        for t in self.a1:
            if t!="" and t in keyword:
                return {"class":"可回收垃圾"}
        for t in self.a2:
            if t!="" and t in keyword:
                return {"class":"干垃圾"}
        for t in self.a3:
            if t!="" and t in keyword:
                return {"class":"湿垃圾"}
        for t in self.a4:
            if t!="" and t in keyword:
                return {"class":"有害垃圾"}
        return {"class":"数据库未收录该种垃圾"}
    def test_search(self):
        with open("可回收垃圾.txt","r",encoding='UTF-8') as f:
            arr = f.readline().split(" ")
            for s in arr:
                self.a1.append(s)
        with open("干垃圾.txt","r",encoding='UTF-8') as f:
            arr = f.readline().split(" ")
            for s in arr:
                self.a2.append(s)
        with open("湿垃圾.txt","r",encoding='UTF-8') as f:
            arr = f.readline().split(" ")
            for s in arr:
                self.a3.append(s)
        with open("有害垃圾.txt","r",encoding='UTF-8') as f:
            arr = f.readline().split(" ")
            for s in arr:
                self.a4.append(s)
        #判断如下垃圾的所属种类
        self.assertTrue(self.search("苹果") == {"class":"湿垃圾"},"search result false")
        self.assertTrue(self.search("尺子") == {"class":"可回收垃圾"},"search result false")
        self.assertTrue(self.search("毛巾") == {"class":"干垃圾"},"search result false")
        self.assertTrue(self.search("电池") == {"class":"有害垃圾"},"search result false")
if __name__ == '__main__':
    unittest.main()