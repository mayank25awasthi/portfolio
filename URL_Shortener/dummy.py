from math import ceil, log2
from primesieve import nth_prime
from random import randint
def abc():
	p=4294967311
	a = randint(1, p - 1)
	b = randint(0, p - 1)
	return lambda x: ((a * x + b) % p) % 2

print(abc())

print(randint(5,10))

print((2119%4294967311)%50)
T = [0] * 50
for i in range(5):
	T[i]+=1
print(T)
