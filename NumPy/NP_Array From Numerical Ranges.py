import numpy as np 
a=np.arange(5)
b=np.arange(5,10)
c=np.arange(5,10,2)
print(a,b,c)
p=np.linspace(10,2)
q=np.linspace(10,20,5)
r=np.linspace(10,20,5,endpoint=False)
s=np.linspace(10,20,5,retstep=True)
print(p,q,r,s)

m=np.logspace(1,2,num=10)
n=np.logspace(1,10,num=10,base=2)
print(m,n)