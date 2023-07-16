
class Ksearch:
    def __init__(self) -> None:
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