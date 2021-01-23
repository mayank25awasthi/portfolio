import numpy as np 
def get_result(a,b,c,d):
	k=np.array([a,b]).reshape(c,d)
	o=np.sum(k,axis=0)
	print(np.prod(o))

x,y= '22'    #input().split()
m, n = (np.array([input().split() for _ in range(int(x))], dtype=int) for _ in range(2))
get_result(m,n,int(x),int(y))


import numpy as np 
def get_result(a,b,c,d):
    k=np.array( [a,b]).reshape(c,d)
    o=np.sum(k,axis=0)
    print(np.prod(o))

x,y=input().split()
a, b = (np.array([input().split() for _ in range(int(x))], dtype=int) for _ in range(2))
get_result(a,b,int(x),int(y))
