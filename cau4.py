import csv
import numpy as np
class cau4:
    min = 2
    max = 4
    X = np.float16(np.array(np.random.rand(min,max)))
    K = np.float16(np.array(np.random.rand(min,max)))
    def csvsave(self,address):
        with open(address,"w+", encoding='utf-8-sig') as f:
            csv.reader(f)
            for self.list in self.X:
                self.g = [0]*len(self.list)
                for self.i in range (0, len(self.list)):
                    self.g[self.i] = str(self.list[self.i])
                for self.string in self.g:
                    f.write(self.string+",")
                f.write("\n")
    def csvread(self,address):
        with open(address,"r+", encoding='utf-8-sig') as f:
            csv.reader(f)
            self.a = []
            for self.row in f:
                self.l = []
                self.x = self.row.strip().split(",")
                self.x.remove('')
                for self.i in range(0,len(self.x)):
                    self.l.append(float(self.x.pop(0)))
                self.a.append(self.l)
            self.X = np.array(self.a)
            print("Ma trận X:\n",self.X)
    def update(self):
        print("Trước update:\n",self.X)
        self.X = self.X + 5*self.K
        print("Sau update:\n",self.X)
c4 = cau4()
c4.csvsave('D:\\PythonApplication1\\PythonApplication1\\Bài 6\\cau4.csv')
c4.csvread('D:\\PythonApplication1\\PythonApplication1\\Bài 6\\cau4.csv')
c4.update()
