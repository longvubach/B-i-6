import hammatran as cal
import csv
import numpy as np
matrix1 = open("matrix1.csv", "r", encoding='utf-8-sig')
matrix2 = open("matrix2.csv", "r", encoding='utf-8-sig')
csv.reader(matrix1)
csv.reader(matrix2)
a = []
b = []
for row in matrix1:
    l = []
    x = row.strip().split(",")
    for i in range(0,len(x)):
        l.append(int(x.pop(0)))
    a.append(l)
a = np.array(a)
print(a)
for row in matrix2:
    l = []
    x = row.strip().split(",")
    for i in range(0,len(x)):
        l.append(int(x.pop(0)))
    b.append(l)
b = np.array(b)
print(b)
try:
    cal.add(a,b)
    cal.sub(a,b)
    cal.mult(a,b)
    cal.div(a,b)
except ValueError:
    print("Ma trận không hợp lệ")
