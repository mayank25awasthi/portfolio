import numpy as np 
def get_identity(num1,num2):
	a =np.eye(num1,num2)
	np.set_printoptions(legacy='1.13')
	print(a)

a,b=int(input()).split()
get_identity(a,b)
