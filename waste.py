import numpy as np
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[7,8,9],[10,11,12]])
c=a+b
print("element wise:")
print(c)
d=a+10
print("broadcasting types:\n",d)
print("slicing example:\n",a[:,1:])

