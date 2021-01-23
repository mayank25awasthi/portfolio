import numpy as np 
a = np.array([[1,2,3],[4,5,6]]) 
a.shape=(2,3)
b = a.reshape(3,2)
print(a,b)

k=np.arange(9)
p=k.reshape(3,3)
print(f'\n {p}')

x = np.array([1,2,3,4,5], dtype = np.int8) 
print(x)
y=np.array([[1,2,3],[7,8,9]], dtype = np.float32)
print(y)
print(y.flatten())