import hammatran as cal
import numpy as np
x = [1,10]
z = [10,2]
y = [5,6]
t = [13,4]
a = np.array([y,t])
b = np.array([x,z])
try:
    cal.add(a,b)
    cal.sub(a,b)
    cal.mult(a,b)
    cal.div(a,b)
except ValueError:
    print("Ma trận không hợp lệ")