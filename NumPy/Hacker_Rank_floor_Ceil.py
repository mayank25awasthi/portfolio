import numpy as np 
def get_result(arr):
	a=np.array(arr,dtype=float)
	np.set_printoptions(legacy='1.13')
	print(np.floor(a), np.ceil(a),np.rint(a), sep='\n')

k='1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9'.split(' ')
get_result(k)