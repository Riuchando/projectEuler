import math
import time
from math import log
from primes import isPrime

''' Taken from: http://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python'''
def factors(n):    
    result = set()
    for i in range(1, int(n ** 0.5) + 1):
        div, mod = divmod(n, i)
        if mod == 0:
            result |= {i, div}
    return result

def pe357():
    # Prime generating Numbers
    t = time.time()
    split = t
    #Find the sum of all positive integers not exceeding 100 000 000
    # such that for every divisor d of n, d+n/d is prime
    sum = 1
    percent = 0
    pbreak = False
    lastN = 0
    for n in range(99999998,1,-4):
        facts = factors(n)
        for d in facts:         # for each divisor in factors set...
            pbreak = isPrime(d+n/d) # if d+n/d is not prime, goto next n
            if( not pbreak ):
                break
        # if all divisors were prime, add n to sum
        if pbreak:
            sum += n
            #print("n=",n,"\tlastN=",lastN,"\tdiff=",lastN-n,"\tin {0:.3f}s" .format(time.time()-t))
            #lastN = n
        
        if((n-2)%100000==0 ):
            percent += 1
            print(percent/10,"% complete, sum =",sum, "in {0:.3f}s / split {1:.3f}s" .format(time.time()-t,time.time()-split))
            remain = (1000-percent)*(time.time()-split)/60
            print("Estimated finish time in:", remain ,"minutes (" + str(remain/60) + "hours)")
            split = time.time()
    print("Final Sum =",sum, "in {0:.3f}s" .format(time.time()-t))

    

''' helper function for 183() '''
def D(N):
    tmp = M(N)
    if tmp[2] == False:
        return N
    else:
        return -N

''' helper function for 183() '''
def T(n,d):
    # Does the fraction n/d terminate?
    # example 11/5 -> terminates
    # example 8/3 -> does not
    checkDigits = log(n,2)+1  # check 100 digits for termination (may need to increase?)
    div = n
    while( checkDigits > 0 ):
        if div%d == 0:
            return True  # this fraction terminated
        else:
            div = (div%d)*10
        checkDigits -= 1
    return False # Did NOT terminate after checkDigits


''' helper function for 183() '''
def M(N):
    # return stats on maximum condtion of P() below
    pMax = (0,0,0)
    iMax = 0
    #for i in range(1,N+1):
    for i in range(int(N*.29)//1,N+1):
        tmp = P(N,i)
        if tmp[0] > pMax[0]:
            pMax = tmp
            iMax = i
        else:
            return(pMax[0],iMax,T(pMax[1],pMax[2]))

''' helper function for 183() '''
def P(N, k):
    num = N**k
    den = k**k
    loggy = k*log(N/k,10)
    return (loggy,num,den)  # num/den fails at large numbers
    

def pe183():
    # Maximum product of parts
    t = time.time()
    mySum = 0
    for i in range(5,10001):
        mySum += D(i)
        if( i%500 == 0 ):
            print(i, mySum, "in "+str(time.time()-t))

    print("Sum =",mySum)
    




    

def pe68():
    # Magic 5-gon ring
    t = time.time()
    count = 0
    solutions = []
    for a in range(1,11):
        for b in range(1,10):
            if b not in {a}:
                for c in range(1,10):
                    if c not in {a,b}:
                        for d in range(1,11):
                            if d not in {a,b,c}:
                                for e in range(1,10):
                                    if e not in {a,b,c,d} and (a+b+c)==(c+d+e):  # first two spokes ==
                                        #print("found 2")
                                        for f in range(1,11):
                                            if f not in {a,b,c,d,e}:
                                                for g in range(1,10):
                                                    if g not in {a,b,c,d,e,f} and (a+b+c)==(e+f+g): # first 3 ==
                                                        #print("found 3")
                                                        for h in range(1,11):
                                                            if h not in {a,b,c,d,e,f,g}:
                                                                for i in range(1,10):
                                                                    if i not in {a,b,c,d,e,f,g,h} and (a+b+c)==(g+h+i): # first 4 ==
                                                                        #print("found 4")
                                                                        for j in range(1,11):
                                                                            if j not in {a,b,c,d,e,f,g,h,i} and (a+b+c)==(b+i+j): # solution!
                                                                                if a < min(d,f,h,j):
                                                                                    solutions.append( ((a,b,c),(d,c,e),(f,e,g),(h,g,i),(j,i,b)) )
                                                                                elif d < min(a,f,h,j):
                                                                                    solutions.append( ((d,c,e),(f,e,g),(h,g,i),(j,i,b),(a,b,c)) )
                                                                                elif f < min(a,d,h,j):
                                                                                    solutions.append( ((f,e,g),(h,g,i),(j,i,b),(a,b,c),(d,c,e)) )
                                                                                elif h < min(a,d,f,j):
                                                                                    solutions.append( ((h,g,i),(j,i,b),(a,b,c),(d,c,e),(f,e,g)) )
                                                                                else:
                                                                                    solutions.append( ((j,i,b),(a,b,c),(d,c,e),(f,e,g),(h,g,i)) )
                                                                                #count += 1
    #print("Found",count,"solutions!")

    #return
    
    '''
    for i in range(1,7):
        for j in range(1,7):
            if j not in {i}:
                for k in range(1,7):
                    if k not in {i,j}:
                        for l in range(1,7):
                            if l not in {i,j,k}:
                                for m in range(1,7):
                                    if m not in {i,j,k,l} and (i+j+k)==(l+k+m):
                                        for n in range(1,7):
                                            if n not in {i,j,k,l,m} and (i+j+k)==(j+l+n):
                                                if i < m and i < n:
                                                    solutions.append( ((i,j,k),(m,k,l),(n,l,j)) )
                                                elif m < i and m < n:
                                                    solutions.append( ((m,k,l),(n,l,j),(i,j,k)) )
                                                else:
                                                    solutions.append( ((n,l,j),(i,j,k),(m,k,l)) )
    '''


    solutions.sort()
    #for s in solutions:
    #    print(s)
    print("SOLUTION IS:",solutions[-1],"in " + str(time.time()-t))
                

    

if __name__ == '__main__':
    print("GO.")
    #test
    pe357()
