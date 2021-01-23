import numpy as np 
a=[2,1,3,4]
b=np.asarray(a)
print(b)

x = [(1,2,3),(4,5)]
y=np.asarray(x)
print(x)

#k='Mayank Awasthi'
#p=np.frombuffer(k,dtype='S1')
#print(p)

v_list=range(5)
print(v_list)
it=iter(v_list)
x = np.fromiter(it, dtype = float) 
print (x)