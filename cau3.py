import numpy as np
class cau3:
    a = np.array([[2,3],[4,5]])
    b = np.array([[3,8],[7,8]])
    t1 = a.transpose()
    t2 = b.transpose()
    def dinhthuc(self):
        self.c = np.float32(np.linalg.det(self.a))
        self.d = np.float32(np.linalg.det(self.b))
        print("Định thức của a: \n",self.c)
        print("Định thức của b: \n",self.d)
    def nghichdao(self):
         self.md = np.matrix(self.a)
         self.mk = np.matrix(self.b)
         self.md = self.md.I
         self.mk = self.mk.I
         print("Nghịch đảo của a: \n",self.md)
         print("Nghich đảo của b: \n",self.mk)
         
var1 = cau3()
print("a:\n", var1.a)
print("b:\n", var1.b)
var1.dinhthuc()
var1.nghichdao()