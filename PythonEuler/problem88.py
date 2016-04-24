from decimal import *
getcontext().prec=102

def sumNum(n,repl=True):
  if repl:
    return sum([int(x) for x in list(str(n)[:-2].replace(".",""))])
  else:
    return sum([int(x) for x in list(str(n).replace(".",""))])
x= [sumNum(Decimal(i).sqrt()) for i in range(1,101)]
#print zip(x,range(1,101))
print sum(x)

