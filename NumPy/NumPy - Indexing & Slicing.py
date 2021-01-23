import numpy as np 
a=np.arange(10)
s=slice(2,7,2)
print(a,a[2:7:2],a[s],a[9])

b = np.array([[1,2,3],[3,4,5],[4,5,6]]) 
print(b )
print(b[1:])
print('\n')
print(b[...,1])
print('\n')
print(b[...,1:])
print('\n')

x = np.array([[1, 2], [3, 4], [5, 6]]) 
y = x[[0,1,2], [0,1,0]] 
print (y)

m = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]]) 
   
print('Our array is:' )
print (m)
print ('\n') 

rows = np.array([[0,0],[3,3]])
cols = np.array([[0,2],[0,2]]) 
n= m[rows,cols] 
print(n)
print('\n')
k= np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]]) 
print(k[1:4])
print(k[1:3])
print(k[1:4,1:3])
print('\n')

p=np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]]) 
print(p[p>5])