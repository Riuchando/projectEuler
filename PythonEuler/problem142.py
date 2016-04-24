# -*- coding: utf-8 -*-
#Find the smallest x + y + z with integers x > y > z > 0 such
#that x + y, x − y, x + z, x − z, y + z, y − z are all perfect squares.
import numpy
import math
x=math.sqrt(10)
x%1
x==int(x)
squarepairs={}

def Checkmemo(i,j):
  if i in squarepairs :
    squarepairs[i].append(j)
  else:
    squarepairs[i]=[j]

def smallest(upperBound):
  for i in range(1,upperBound):
    for j in range(1,i):
      one=math.sqrt(i+j)
      two=math.sqrt(i-j)
      if one==int(one) and two == int(two):
        Checkmemo(i,j)
        for k in range(1,j):
          three=math.sqrt(i+k)
          four=math.sqrt(i-k)
          if three==int(three) and four == int(four):
              return i+j+k

smallest(10000)
10-6
10+6
6+5
6-5
squarepairs[str(1)+","+str(2)]=True

