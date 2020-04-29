import numpy as np
a=np.array([2,3,4,5],dtype=np.int)    #定义一个数组
print(a.dtype)

a=np.zeros((3,4))   #定义一个三行四列的零矩阵
print(a)

b=np.ones((3,4))   #定义一个三行四列的全为1的矩阵
print(b)

c=np.arange(12).reshape((3,4))
print(c)
d=c**2
print(d)


#矩阵的运算      np.dot(a,b)