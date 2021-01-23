import numpy as np 
def fn_numpy_math(num1,num2,x,y):
	a=np.array(num1).reshape(x,y)
	b=np.array(num2).reshape(x,y)
	print(a+b)
	print(a-b)
	print(a*b)
	print(np.floor_divide(a,b))
	print(a%b)
	print(a**b)

x,y=input().split()
m=tuple(map(int, input().split()))
n=tuple(map(int, input().split()))
fn_numpy_math(m,n,int(x),int(y))