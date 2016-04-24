import math

def factorialMod(n, modulus):
    ans=1
    for i in xrange(1,n+1):
      if i % 10 != 0:
          ans = ans * i % modulus
      if ans % 10 == 0:
          #print ans
          ans/=10
    return ans % modulus

#print factorialMod(1000,10)

class PrimeFactorizer:
    #your code here
    def __init__(self,n):
        self.number=n
        self.factor={}
        i=2
        while self.number>=i:
          while self.number%i==0:
            self.number=self.number/i
            if self.factor.get(i) is not None:
              self.factor[i]=self.factor[i]+1
            else:
              self.factor[i]=1
          i=i+1

#know before hand that this mod needs to be 12(from the trailing 0)+5
#x= PrimeFactorizer(1000000000000)
#print x.factor
print factorialMod(20,10**6)
#print factorialMod(1000000000000,10**6)
#print factorialMod(10,10**6)
#print factorialMod(100,10**6)
#print factorialMod(1000,10**6)
print factorialMod(10**4,10**6)
#print factorialMod(10**5,10**6)
