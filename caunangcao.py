import numpy as np
import math
import csv
class tienlai:
    def laisuat(self,address):
        self.a = float(input("Nhập số tiền gửi: "))
        if self.a <=0:
            print("Nhập số tiền lớn hơn 0")
            return(tienlai.laisuat())
        self.n = int(input("Nhập tháng gửi: "))
        if self.n <=0:
            print("Số tháng gửi phải lớn hơn 0")
            return(tienlai.laisuat())
        self.t = 0
        for self.i in range(0,self.n):
            with open(address,'w+', encoding='utf-8-sig') as f:
                csv.reader(f)
                for number in f:
                    x = float(number)
                    print(x)
                self.a = self.a + x
                self.t = self.a*pow(1+0.0058,self.i)
        print(self.t)
cnc = tienlai()
cnc.laisuat('D:\\PythonApplication1\\PythonApplication1\\Bài 6\\cnc.csv')
