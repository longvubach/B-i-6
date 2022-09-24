import numpy as np
def sub(m1,m2):
    c = m1 - m2
    print("Trừ: ")
    print(c)
def add(m1,m2):
    c = m1 + m2
    print("Cộng: ")
    print(c)
def mult(ma,mb):
    sa = ma.shape
    sb = mb.shape
    if sa[1] == sb[0]:
        c = ma @ mb
    else:
        print("Kích thước không phù hợp")
    c = np.float16(c)
    print("Kết quả sau khi nhân 2 ma trận:")
    print(c,"\n")
def div(ma,mb):
    c = np.linalg.det(mb)
    if c != 0:
        md = np.matrix(mb)
        md = md.I
        print("Ma trận đảo: ")
        print(md)
        sa = ma.shape
        sd = md.shape
        if sa[1] == sd[0]:
            d = ma @ md
        else:
            print("Kích thước không phù hợp")
    else:
        print("Không có giá trị phù hợp")
    d = np.float16(d)
    print("Kết quả sau khi chia 2 ma trận: ")
    print(d)