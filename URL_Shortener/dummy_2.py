from math import ceil, log2
from primesieve import nth_prime #will get nth prime number [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
from random import randint

class UniversalHashing:
  """ N = #bins
      p = prime number st: p >= N 
	nth_prime(1, 1 << max(32, ceil(log2(N))))
	nth_prime(1,1<<max(32),ceil(log2(2)))))
	nth_prime(1,2**32)
	nth_prime(1,4294967296)
	=4294967311   
	assert:- Returns Error if condition not satisfied 
	<< operatior:-  multiply with 2the power like 2<<2 =2*2'2=8 or 7*2'3=56 and ceil will give the exact value or next vlue ceil(1)=1 , ceil(1.1)=2
	randint:- Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1). """
  def __init__(self, N, p = None):
    self.N = N
    if p is None:
      p = nth_prime(1, 1 << max(32, ceil(log2(N))))  
    assert p >= N, 'Prime number p should be at least N!'
    self.p = p

  def draw(self):
    a = randint(1, self.p - 1)
    b = randint(0, self.p - 1)
    return lambda x: ((a * x + b) % self.p) % self.N

if __name__ == '__main__':
  N = 50       #bins
  n = 100000   #elements
  H = UniversalHashing(N)
  h = H.draw()
  T = [0] * N
  for _ in range(n):
    x = randint(0, n * 10)
    T[h(x)] += 1
  for i in range(len(T)):
    print(T[i] / n)    # This should be approximately equal