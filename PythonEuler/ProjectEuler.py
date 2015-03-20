#!/usr/bin/env python
import random
import time
import math
from math import sqrt
from math import factorial
import fractions


#########################
# Helper functions
########################

def rawRead( filename ):
    ''' cheat for reading in files '''
    file = open(filename,'r')
    raw = file.read()
    file.close()
    return raw

def printTime( t ):
    newt = time.time()-t
    if newt < 60:
        return "\t(in " + str(round(newt,2)) + "s)"
    elif newt < 3600:
        min = int(newt//60)
        sec = round(newt%60,2)
        return "\t(in " + str(min) + "m " + str(sec) + "s)"

''' Input a string to test for Palindrome '''
def isPalindrome( s ):
    for i in range(math.ceil(len(s))):
        if( s[i] != s[-i-1] ):
            return False
    return True

def primesUnderTenMillion():
    # Generate array of primes under 10,000,000
    primes = []
    percent = 0
    t = time.time()
    for i in range(2,10000000):
        if( is_prime(i) ):
            primes.append(i)
        if(i%100000==0):
            percent += 1
            print(str(percent)+"% -",len(primes),"...")
    print("Done. Found",len(primes),"prime numbers under 10000000. time:" + str((time.time()-t)))
    return primes

def loadPrimes():
    t = time.time()
    #load pre-compiled list of prime numbers from save file
    raw = rawRead("primeCSV.txt")

    #process
    primes = []
    buff = ''
    for c in raw:
        if c == ",":
            primes.append(int(buff))
            buff = ''
        else:
            buff += c
    print("primeCSV.txt loaded in time: " + str((time.time()-t)) )
    return primes
        

''' Common factor '''
''' THIS IS VERY INEFFICIENT!!!!! '''
def commonFactor( a, b):
    # more efficient way using fractions library
    if( fractions.gcd(a,b) == 1 ):
        return False
    else:
        return True
    '''
    # Returns true if the two have a common factor, false if not
    for i in range(2, min(a,b)+1):
        if( a%i == 0 and b%i == 0 ):
            return True
    return False
    '''


'''
Print lowest prime factor
(Use recursively)
'''
def listPrimeFactors( x ):
    # base case
    if( x == 1 ):
        #print("Done.")
        tmp = []
        return tmp
    for i in range(2, x+1):  # include all numbers up to x
        if( x%i == 0 ):
            primes = []
            n = i
            primes.append(n)  # append prime number
            tmp = listPrimeFactors( x//i ) # return list of primes
            if( len(tmp) > 0 ):
                for t in tmp:
                    primes.append(t)
            return primes

def commonFactorsUnitTest():
    # do timing study on above function
    print("Test 1 to 10000")
    t = time.time()
    for i in range(1,10001):
        test = commonFactor(i,1000000)
    print("Finished in " + str(time.time()-t))

    print("Test 999900 to 1000000")
    t = time.time()
    for i in range(990000,1000000):
        test = commonFactor(i,1000000)
    print("Finished in " + str(time.time()-t))

def distinctPrimeFactors( num ):
    l = listPrimeFactors(num)
    d = {}
    for factor in l:
        d[factor] = 1
    return len(d)
    

'''
Helper function yes/no prime
'''
def areYouPrime(x):
    #determine if x is prime
    for i in range(2,x):
        if( x%i == 0 ):
            return False
    return True

''' Taken from sgruenwald snippet '''
# is this faster than mine?
def is_prime(num):
    for j in range(2,int(sqrt(num)+1)):
        if (num % j) == 0: 
            return False
    return True

''' Helper: count # of factors '''
def countFactors( num ):
    factors = 0
    maxSearch = num+1
    check = 1
    if( is_prime(num) ):
        return 2
    while( check < maxSearch ):
        if( num%check == 0 ):
            factors += 2  # add factor pair
            maxSearch = num//check   # lower search window
        check += 1
    return factors

''' Helper: count # of factors '''
def listFactors( num ):
    factors = []
    maxSearch = num+1
    check = 1
    while( check < maxSearch ):
        if( num%check == 0 ):
            #factors += 2  # add factor pair
            if( check == num//check ):
                factors.append(check)
            else:
                factors.append(check)
                factors.append(num//check)
            maxSearch = num//check   # lower search window
        check += 1
    factors.sort()
    return factors

''' helper functions for Problem 347 '''
def pe347_M( p, q, N ):
    # Largest integer <= N ony divisible by both prime p and q
    # M(2,3,100) = 96
    # M(3,5,100) = 75
    # M(2,73,100) = 0
    t = time.time()
    ''' test all numbers <= 100 '''
    for i in range(N,p*q-1,-1):
        # test if number is divisible by p and q
        if( i%q == 0 ):     # if number is divisble by larger number
            sub = i//q      # divide out first number
            if( sub%p == 0 ):   # if number is divisible by 2nd prime
                sub = sub//p    # divide out second number
                R = 0           # we will break while loop if remainder >0
                while( R == 0 ):
                    if( sub == 1 ):   # if we can divide down to 1, we found our number
                        print("Found in time: " + str((time.time()-t)) )
                        return i      # so return it!
                    elif( sub%p == 0 ):  # if p is another factor
                        sub = sub//p     # divide it out
                    elif( sub%q == 0 ):  # if not p, then q must be another factor
                        sub = sub//q     # divide it out
                    else:                # if we can't evenly divide by p or q, try next number
                        break
            else:
                pass  # try next lower number
        else:
            pass # try to divide next lower number
        
    # if we never kicked out, no number exists
    return 0


        
    if N%p != 0 or N%p != 0 :
        return 0
    else:
        return 1

def sumDigits( n ):
    sum = 0
    while( n > 0 ):
        sum += n%10
        n = n//10
        
    return sum

def pe491():
    #Double pandigital number divisible by 1
    t = time.time()

    # Notes:  to be divisible by 11, odd numbers must be multiple 11 different
    #  than sum of even numbers.
    # 3 cases where this happens:  even/odd: 23/67, 34/56, and 45/45
    # lowest (sorted) 23: 0011223347
    # highest (sortd) 23: 0011223455

    # lowest (sorted) 34: 0011223799
    # highest (sortd) 34: 1122344566

    # lowest (sorted) 45: 0011278899
    # highest (sortd) 45: 2233456677
    count = 0
    for i in range(11223799,1122344566+1):
        if( sumDigits(i) == 34 ):
            count += 1
            #print(i)
        if( i % 1000000 == 0 ):
            print(i,count," @" + str(time.time()-t))
    print(count)
        

                                                                
                                    
    
    
    
''' pe21 - d(n) = sum of the proper divisors '''
def d( n ):
    sum = 1
    if( n == 1 or n == 0 ):
        return 0
    if( is_prime(n) ):
        return 1
    maxSearch = n
    check = 2  # start checking for primes at 2, 1 is already included in the sum
    while( check < maxSearch ):
        if( n%check == 0 ):
            sum += check   # add the first divisor
            sum += n//check  # add the second divisor
            maxSearch = n//check   # lower bounds of search window
        check += 1
    return sum


def R( d ):
    # returns the resilience of a denominator
    r = 0
    b = listPrimeFactors(d)     # prime factors of denominator
    dd = {}   #empty dictionary Set
    for prime in b:
        for i in range(1, ((d-1)//prime)+1 ):
            dd[prime*i] = "1"

    r = d-len(dd)-1
    '''
    for n in range(1,d):  # 1 up to not including d
        common = False
        a = listPrimeFactors(n) # prime factors of numerator
        for item in b:
            for num in a:
                if( item == num ):
                    common = True
                    break
            if( common == True ):
                break
        if( common == False ):  # then no common denominators
            #print(n,end="..")
            r += 1
            
    #print(r,"/",d-1)
    '''
    return (r,(d-1))

def pe243():
    #Resilience
    lowest = 1
    t = time.time()
    step = 2*3*5*7*11*13*17
    for d in range(step,100000000,step):
        r_tuple = R(d)
        resilience = r_tuple[0]/r_tuple[1]
        if resilience < (15499/94744):
            print("\n\nFound d:",d)
            return
        elif( resilience < lowest ):
            lowest = resilience
            print(d,"-",r_tuple,lowest,"time: " + str(time.time()-t))
    print("\nDone.")
    


def distance(x1,y1,x2,y2):
    ''' return the distance between the two points '''
    return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))


def process102data(x1,y1,x2,y2,x3,y3):
    #print(x1,y1,x2,y2,x3,y3)
    ''' if the sum of the angles with the origin at the center = 360,
    then the origin is inside the triangle '''

    # Brute force test all three possible angle cases:
    ''' 1st case '''
    a = distance(0,0,x1,y1)
    b = distance(0,0,x2,y2)
    c = distance(x1,y1,x2,y2)
    angle1 = math.degrees(math.acos( (a*a+b*b-c*c) / (2*a*b) ))

    ''' 2st case '''
    a = distance(0,0,x1,y1)
    b = distance(0,0,x3,y3)
    c = distance(x1,y1,x3,y3)
    angle2 = math.degrees(math.acos( (a*a+b*b-c*c) / (2*a*b) ))

    ''' 3st case '''
    a = distance(0,0,x2,y2)
    b = distance(0,0,x3,y3)
    c = distance(x2,y2,x3,y3)
    angle3 = math.degrees(math.acos( (a*a+b*b-c*c) / (2*a*b) ))
    
    angles = angle1 + angle2 + angle3
    #print("Angle Sum=",angles)

    ''' needs tight tolerences for accurate answering '''
    if (359.99 < angles) and (angles < 360.001):  # this worked.  
        #print("passed")
        return 1
    else:
        #print("failed")
        return 0

def pe102():
    # Triangle Containment: read in a list of coordinates and flag
    #  whether origin is contained within them
    ''' First let's read the file in '''
    file = open('p102_triangles.txt', 'r')
    raw = file.read()
    file.close()

    # Parse into useable data structures - parse one at a time and process
    loopCounter = 0
    originCounter = 0
    buff = ''
    xyToggle = 1  # 1 = X, -1 = Y
    for c in raw:
        if c == ',':
            if xyToggle == 1:
                x1 = int(buff)
                buff = ''
                xyToggle += 1
            elif xyToggle == 2:
                y1 = int(buff)
                buff = ''
                xyToggle += 1
            elif xyToggle == 3:
                x2 = int(buff)
                buff = ''
                xyToggle += 1
            elif xyToggle == 4:
                y2 = int(buff)
                buff = ''
                xyToggle += 1
            else:
                x3 = int(buff)
                buff = ''
        elif c == '\n':
            y3 = int(buff)
            buff = ''
            xyToggle = 1
            originCounter += process102data(x1,y1,x2,y2,x3,y3)
            loopCounter += 1
        else:
            buff += c
        
    print("Counted:", originCounter, " Looped:",loopCounter)


def pe206():
    # find the unique integer whose square is of the form 1_2_3_4_5_6_7_8_9_0
    # between 1390000000
    #     and 1009950000
    
    for i in range(1009950070, 1390000000, 100):  # 30*30, or 70*70 gives 900
        x = str(i*i)    # find the square
        key = x[0]+x[2]+x[4]+x[6]+x[8]+x[10]+x[12]+x[14]+x[16]+x[18]
        #print(i, x, key)
        #return
        if( key == '1234567890' ):
            print("Found x=", x, i)
            return True
        if( (i//100)%100000 == 0 ):
            print("x-",x,key)
    print("no luck...")



''' helper function for pe131 '''
def primeCubeExists( p, n ):
    # return yes if a prime cube exists, no if one does not
    # ex: n^3 + n^2*p = (x^3)
    end = n+20000 #n*2+p
    while n < end:
        pc = n**3 + (n**2)*p
        if round(pc**(1/3),10)%1 == 0:
            print("p=",p,"n=",n,"p+n=",p+n,"cube=",round(pc**(1/3),10))
            return (True,p+n)
        n += 1
    return (False,n)

''' helper function for pe131-- take 2 '''
def pce( p, n ):
    # returns true if the given prime p just happens to work with value n
    pc = n**3 + (n**2)*p
    root = pc**(1/3)
    #if root**3 == pc:
    if round(pc**(1/3),1)**3 == pc:
        #if is_prime(p):
            #print("*p=",p,"n=",n,"p+n=",p+n,"cube=",round(pc**(1/3),10))
        #else:
            #print(" p=",p,"n=",n,"p+n=",p+n,"cube=",round(pc**(1/3),10))
        return (True,p+n)
    return (False,n)

def test_pce():
    start = 1
    count = 0
    for i in range(1,1000000):
        result = pce(i,start)
        if result[0] :
            start = result[1]
            if is_prime(i):
                count += 1
    print("Done. Counted:",count)

def pe131():
    # Prime cube partnership
    test_pce()
    return
    # first let's load some primes
    p = loadPrimes()
    t = time.time()
    start = 1
    count = 0
    for prime in p:
        #print(prime)
        if prime > 1000000:
            break
        result = primeCubeExists(prime,start)
        if result[0]:
            count += 1
            #print("Counted",count,"at p=" ,prime , printTime(t) )
            start = result[1]

    print("Counted",count,printTime(t))
    


''' Helper function for pe112() '''
def isBouncy( n ):
    sn = str(n)
    less = 0
    great = 0
    equal = 0
    for i in range(len(sn)-1):
        if( sn[i] > sn[i+1] ):
            great += 1
        elif( sn[i] < sn[i+1]):
            less += 1
        else:
            equal += 1
    if( less > 0 and great > 0 ):
        return True
    else:
        return False

''' helper function for pe125() '''
def makePalindromesUnder( evenpower ):
    # returns a list of palindromes less than given even power of 10 (i.e. 1^evenpower)
    # i.e. 10^4 => up to 9999, 10^8 => up to 99999999
    if( evenpower%2 != 0 ):
        print("Error: not even power.")
        return
    p = []  # store palindromes here
    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(1,pow(10,evenpower//2)):  # Take half of the values and flip to make palindromes
        if i < 10:  # 1-9 => Forms 1, 11
            p.append(i)
            p.append( i*10 + i )
        elif i < 100: # 10-99 => Forms 101, 1001
            a = i%10
            b = i//10
            p.append( i*10 + b )
            p.append( i*100 + a*10 + b )
        elif i < 1000:  # 100-999 => Forms 12321, 123321
            a = i//1%10   
            b = i//10%10
            c = i//100%10
            p.append( i*100 + b*10 + c )         # Form cbabc
            p.append( i*1000 + a*100 + b*10 + c) # Form cbaabc
        elif i < 10000:  # 1000-9999 => Forms 1234321, 12344321
            a = i//1%10
            b = i//10%10
            c = i//100%10
            d = i//1000%10
            p.append( i*1000 + b*100 + c*10 + d )# Form dcbabcd
            p.append( i*10000 + a*1000 + b*100 + c*10 + d)# Form dcbaabcd

    p.sort()
    return p
            
''' helper function for pe125() '''
def sumOfConsecutiveSquares( n ):
    # test to determine if n can be written as the sum of
    # consecutive squares.
    # Example: 595 = 6^2 + 7^2 + 8^2 + 9^2 + 10^2 + 11^2 + 12^2.
    
    # starting with 1, keep adding consecutive squares until we either
    # find an equal or go overboard.  Going overboard prompts us to
    # increase 'start'.  Test until 'start' > sqrt(n)
    start = 1
    while start < sqrt(n):   # while our starting sum < sqrt(number)
        sqsum = 0
        index = start
        while( sqsum < n ): # keep adding while our sum < number
            sqsum += index*index
            if( sqsum == n ):
                return True
            else:
                index += 1
            # while breaks when sum goes over
        # bump start and try again
        start += 1
        
    # if we reach here, we haven't found a consec. sqr. sum
    return False

''' helper function for pe125() - alternate approach '''
def makeSumOfConsecutiveSquares():
    # Create a list of sum of consecutive squares under n
    sos = set()
    limit = 10**8
    start = 1
    while start < int(sqrt(limit)):
        index = start
        sqsum = index*index
        index += 1
        while( sqsum < limit ):
            sqsum += index*index
            sos.add(sqsum)
            index += 1
        start += 1
    return sos
            
def pe125():
    # alternate take on problem 125 --- much better 0.371021032333374
    # Palindromic sums
    t = time.time()
    p = makePalindromesUnder(8) # 19998 palindromes under 10^8
    sos = makeSumOfConsecutiveSquares() # make list of all sums of cons. sq.

    count = 0
    sqSum = 0
    for pallys in p:
        if pallys in sos:
            count += 1
            sqSum += pallys
            #print(count,pallys,"in "+str(time.time()-t))
    print("Counted",count,"Sum=",sqSum,"in "+str(time.time()-t))
    

def pe125alt():  # ... takes 22 minutes :(
    # Palindromic sums
    t = time.time()
    p = makePalindromesUnder(8) # 19998 palindromes under 10^8

    count = 0
    sqSum = 0
    for pally in p:
        if( sumOfConsecutiveSquares(pally) ):
            count += 1
            sqSum += pally
            print(count,pally,"in "+str(time.time()-t))
    print("Counted",count,"Sum=",sqSum,"in "+str(time.time()-t))


def pe121():
    # Disc game prize fund
    # 15-turns, start with 1 R, 1 B, add a R after each turn.
    # Turn   Breakdown
    # 1,2,3  BR, BRR, BRRR
    # 3,4,5  BRRRR, BRRRRR, BRRRRRR ...
    # to win 15 turns, must have minimum of 8 Blues

    # to predict the probability of each event is easy:
    # Turn 1:  P(B) = 1/2 P(R) = 1/2
    # Turn 2:  P(B) = 1/3 P(R) = 2/3
    # Turn 3:  P(B) = 1/4 P(R) = 3/4
    # ...
    # Turn 15: P(B) = 1/16 P(R) = 15/16

    # Denominator of final winning probability will be 16! = 20922789888000
    denominator = factorial(16)
    # store numerator of probabilities for Red and Blue here:
    p_b = 1 # probability of picking a blue (numerator) is always 1
    p_r = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    # we need to determine the winning probability
    # 1st, let's try generating text strings of all possible outcomes.
    #  i.e. 111, 110, 101, 011, ...
    # For 15 turns, there will be 2**15 - 1 strings (32767)
    outcomes = []
    for i in range(2**15):
        a = bin(i)
        outcomes.append(a.replace('0b','0'*(17-len(a)),1))

    wins = []
    for o in outcomes:
        if o.count('1') > 7:
            wins.append(o)

    # Calculate the total probability of winning
    # 1 = Blue, 0 = Red
    total_prob_numerator = 0
    for outcome in wins:        # For each outcome in wins...
        turnNumber = 0
        probabilityTurn = 1
        for chip in outcome:    # Check if chip is red or blue (0 or 1)
            if chip == '0':
                probabilityTurn *= p_r[turnNumber]
                turnNumber += 1 # next chip choice
            else:
                probabilityTurn *= p_b
                turnNumber += 1
        # Now ADD this probability to total numerator
        total_prob_numerator += probabilityTurn

    print("End Probability=", total_prob_numerator, "/", denominator)
    print("Pay out < ", denominator/total_prob_numerator)
        
    return wins


def pe112():
    # Bouncy numbers
    t = time.time()
    bouncy = 0
    notbouncy = 0
    for i in range(1,100000000):
        if( isBouncy(i) ):
            bouncy += 1
        else:
            notbouncy += 1
        if( 100*bouncy == 99*(bouncy+notbouncy)):
            print("Found 99% at:",i)
            break

    print(bouncy, notbouncy, bouncy*100/(bouncy+notbouncy), "in " + str(time.time()-t))



''' Helper function for pe100 '''
def pBB( red, blue ):
    print("For case Red="+str(red)+" and Blue=" + str(blue))
    print("pBB =", blue*(blue-1)/( (blue+red)*(blue+red-1) ))
    print("Ratio =", red/blue)

def pe100():
    # Arranged probability
    blue = 1
    red  =  1
    t = time.time()
    for i in range(1000000000):
        pBBnum = 2*blue*(blue-1)
        pBBden = (blue+red)*(blue+red-1)
        #print("Red:",red,"Blue:",blue,"pBB:",pBB)
        if( pBBnum == pBBden ):
            # WHEN we find a match, use the following algorithm to 'guess' very close to next occurance
            print("R=",red/blue,"L=",len(str(red+blue)),"R/B=",red,"/",blue,"T=",blue+red,"in "+str(time.time()-t))
            if( len(str(red+blue)) == 13 ):
                break
            blue = int(blue*5.82842)
            red = int(blue*0.41421355)
            #blue += 1
        elif( pBBnum < pBBden ):
            blue += 1
        else:
            red += 1
        
    print("Done.","R:",red,"B:",blue,"in "+str(time.time()-t))


''' Helper function for pe99 '''
def bigE(number, exp ):
    # Calculate a quick approx for a large exponential number
    # returning 6 digits + a 10**nth value
    result = number
    power = 0
    for i in range(1,exp):
        result *= number
        digits = len(str(result))
        result = result//10**(digits-9)  # truncate result
        power += digits-9
    return (result,power)
    #TODO:  improve the precision!!!!


def pe99():
    # Largest Exponential
    raw = rawRead('p099_base_exp.txt')
    number = 0
    exp = 0
    buffer = ''
    lineNumber = 1
    # set default maximum values
    maxN = 0
    maxE = 0
    maxL = 0
    t = time.time()
    # parse the data
    for c in raw:
        if c == ',':
            number = int(buffer)
            buffer = ''
        elif c == '\n':
            exp = int(buffer)
            buffer = ''
            # Do our bigE test here
            result = bigE(number,exp)
            if( result[1] > maxE ):
                maxN = result[0]
                maxE = result[1]
                maxL = lineNumber
                print("Found new max on Line",lineNumber,"maxN=",maxN,"maxE=",maxE,"N/E:",number,exp,str(time.time()-t))
            elif( result[1] == maxE and result[0] > maxN ):
                maxN = result[0]
                maxE = result[1]
                maxL = lineNumber
                print("Found new max on Line",lineNumber,"maxN=",maxN,"maxE=",maxE,"N/E:",number,exp,str(time.time()-t))
            elif( result[1] == maxE ):
                print("Found CLOSE max on Line",lineNumber,"number:",number,"exp:",exp,str(time.time()-t))
            lineNumber += 1
        else:
            buffer += c

    print("Found Max on line",lineNumber)



def pe97():
    # Large non-Mersenne prime
    # find the last ten digits of this number: 28433 × 2^7830457+1.
    t = time.time()
    two = 1
    for i in range(7830457):
        two = (two*2)%10000000000
    two = (28433 * two + 1)%10000000000
    print(two,"in " + str(time.time()-t))
        





''' Helper function: sum of the squares '''
def SumSquares( n ):
    sum = 0
    sn = str(n)
    for digit in sn:
        sum += int(digit)*int(digit)
    return sum

''' Helper function: Determine if SumSquares ends in 1 or 89 '''
def processSumSquares( n ):
    # returns True if '89' is the end chain
    s = n
    while( s != 1 and s != 89 ):
        s = SumSquares( s )
        #print(s)
    if( s == 1 ):
        return False
    else:
        return True

def pe92():
    count = 0
    t = time.time()
    for i in range(1,10000000):
        if( processSumSquares(i) ):
            count += 1
        if( i%100000 == 0 ):
            print("Processed",i//100000,"%... in " + str(time.time()-t))
    print("Counted:",count)

def RomanToDecimal( s ):
    # take a string in Roman Numeral format and convert to Decimal
    # I = 1 , IV = 4 , IX = 9
    # V = 5 
    # X = 10 , XL = 40, XC = 90
    # L = 50
    # C = 100, CD = 400, CM = 900
    # D = 500
    # M = 1000
    s += " "   # pad with space to simplify array checking
    skipFlag = False
    dec = 0
    for i in range(len(s)):  # we will walk through the character array
        if( skipFlag ):
            skipFlag = False
        elif( s[i] == 'M' ):
            dec += 1000
        elif( s[i] == 'D' ):
            dec += 500
        elif( s[i] == 'C' and s[i+1] == 'M' ):
            dec += 900
            skipFlag = True
        elif( s[i] == 'C' and s[i+1] == 'D' ):
            dec += 400
            skipFlag = True
        elif( s[i] == 'C' ):
            dec += 100
        elif( s[i] == 'L' ):
            dec += 50
        elif( s[i] == 'X' and s[i+1] == 'C' ):
            dec += 90
            skipFlag = True
        elif( s[i] == 'X' and s[i+1] == 'L' ):
            dec += 40
            skipFlag = True
        elif( s[i] == 'X' ):
            dec += 10
        elif( s[i] == 'V' ):
            dec += 5
        elif( s[i] == 'I' and s[i+1] == 'X' ):
            dec += 9
            skipFlag = True
        elif( s[i] == 'I' and s[i+1] == 'V' ):
            dec += 4
            skipFlag = True
        elif( s[i] == 'I' ):
            dec += 1
    #print(dec)
    return dec

def DecimalToRoman( n ):
    # Convert a decimal to minimal Roman form
    # assume # is below 5000
    roman = ''  # empty roman string
    x1000 = n//1000
    for i in range(x1000):
        # add M's
        roman += 'M'
        
    x100 = n//100 - 10*x1000
    # Add appropriate number of 100's
    if( x100 == 9 ):    # 900
        roman += 'CM'
    elif( x100 >= 5 ):  # 5,6,7,800
        roman += 'D'
        for i in range(x100-5):
            roman += 'C'
    elif( x100 == 4 ):  # 400
        roman += 'CD'
    else:               # 0, 1, 2, 300
        for i in range(x100):
            roman += 'C'

    x10 = n//10 - 100*x1000 - 10*x100
    # Add appropriate number of 100's
    if( x10 == 9 ):    # 90
        roman += 'XC'
    elif( x10 >= 5 ):  # 5,6,7,80
        roman += 'L'
        for i in range(x10-5):
            roman += 'X'
    elif( x10 == 4 ):  # 40
        roman += 'XL'
    else:               # 0, 1, 2, 30
        for i in range(x10):
            roman += 'X'

    x1 = n%10
    # Add appropriate number of 100's
    if( x1 == 9 ):    # 9
        roman += 'IX'
    elif( x1 >= 5 ):  # 5,6,7,8
        roman += 'V'
        for i in range(x1-5):
            roman += 'I'
    elif( x1 == 4 ):  # 4
        roman += 'IV'
    else:               # 0, 1, 2, 3
        for i in range(x1):
            roman += 'I'
            
    #print(roman)
    return(roman)
    
            
    

def pe89():
    # Roman numerals
    raw = rawRead('p089_roman.txt')

    originalCount = 0
    # count initial characters
    numbers = []
    buff = ''
    for c in raw:
        if( c == '\n'):
            numbers.append(buff)
            buff = ''
        else:
            buff += c
            originalCount += 1
            
    print("Originally",originalCount,"characters.")
    print(len(numbers))

    # lets convert all the Romans!
    newCount = 0
    for n in numbers:
        r = DecimalToRoman(RomanToDecimal(n))
        newCount += len(r)
    print("New Count:",newCount)
    print("Difference:",originalCount-newCount)


''' helper function for pe85() '''
def rectCount( width, height ):
    # count the number of contained rectanges in a wxh grid
    total = 0
    for w in range(width):
        for h in range(height):
            # starts out at 1x1, calculate number of contained rectangles
            total += (width-w)*(height-h)
    return total


def pe85():
    # Counting rectangles
    t = time.time()
    best = (0,0)
    closest = 2000

    w = 2000
    h = 1
    while (w > 0 and h < 2001):
        test = rectCount(w,h)
        
        if abs(test-2000000) < closest:
            best = (w,h)
            closest = abs(test-2000000)  # save newer closest
            print("Found",w,"x",h,"=",w*h,test,"in " + str(time.time()-t))
            
        if 2000000 - test > 0:  # if count is < 2 million
            h += 1              # increase height
        else:                   # otherwise, we decrease width
            w -= 1

    print("Done.")


def pe81():
    # Path sum: two ways
    # first build 80x80 matrix into padded diamond data structure
    # second, just add paths from top to bottom
    raw = rawRead('p081_matrix.txt')

    # Form 80x80 matrix data structure
    col = []
    row = []
    buff = ''
    for c in raw:
        if c == '\n':
            row.append(int(buff))
            buff = '' 
            col.append(row)
            row = []
        elif c == ',':
            row.append(int(buff))
            buff = ''
        else:
            buff += c

    # 'col' now contains 80 x 80 matrix.
    # Time to convert to diamond data structure
    diamond = []
    for i in range(2*80-1):
        diamond.append([])   # fill with empty lists
    for i in range(2*80-1):
        for j in range(min(80,i+1)):
            if( len(col[j]) > 0 ):
                diamond[i].append( col[j].pop(0) )

    # pad top of diamond with a large weight
    diamond[0].append(99999)


    # data structure now ready...
    # first process the top of the triangle, adding weights,
    # starting at row 1 and ending at row 79 (the diagonal)
    for i in range(1,80):
        for j in range( len(diamond[i]) ):  # for all elements in the row
            if( j == 0 ):
                diamond[i][j] += diamond[i-1][j]  # first element adds weight above it
            else:
                if( diamond[i-1][j-1] > diamond[i-1][j] ):
                    diamond[i][j] += diamond[i-1][j]    # add the minimum weight above
                else:
                    diamond[i][j] += diamond[i-1][j-1]  # add the minimum weight above
        # pad this row with a large weight before processing next row
        diamond[i].append(99999 + 9*(10**i))

    # second, process the bottom half of the triangle, adding weights,
    # starting at row 80 and ending at row 159.  the final value at row 159 should
    # be the shortest path
    for i in range(80,159):
        for j in range( len(diamond[i]) ):  # for all elements in the row
            if( diamond[i-1][j] > diamond[i-1][j+1] ):
                diamond[i][j] += diamond[i-1][j+1]
            else:
                diamond[i][j] += diamond[i-1][j]

    print(diamond[158])
        
    #print(len(col),col[0])
    return(diamond)
    


def pe79():
    # Passcode derivation
    raw = rawRead('p079_keylog.txt')

    # process raw and add to dictionary
    d = {}
    buff = ''
    for c in raw:
        if( c == '\n'):
            d[buff] = 1
            buff = ''
        else:
            buff += c

    # dictionary into list:
    l = []
    for item in d:
        l.append(item)
    l.sort()
        
    return l

def pe76( number ):
    # Counting summations -- code below does NOT work. :(
    t = time.time()
    # First, create an array of 1's adding up to number
    a = []
    for i in range(number):
        a.append(1)

    count = 1   # starting counting with initial configuration

    
    while( a[1] != (number-1) ):
        # Keep processing the steps below
        a.sort(reverse=True)
        print(count,"\t",a)
        if( a[-1] == 1 and a[-2] == 1 ):
            a.pop() #a.remove(1)
            a.pop() #a.remove(1)
            a.append(2)
            #a.sort()
            count += 1
            #print(count,"\t",a)
        elif( a[-1] == 1 or a[-1] == a[-2]):
            add = a[-2] + 1
            a.pop() #a.remove(a[0])   # Remove two lowest values
            a.pop() #a.remove(a[0])
            a.append(add)    # Add the sum of lowest two
            # now for every number less than the added number, remove and pad to 1's
            b = a.copy()
            for i in b:
                if i < add:
                    a.remove(i)
            total = 0
            for i in a:
                total += i
            for i in range(total,number):
                a.append(1)
            #a.sort()
            count += 1
            #print(count,"\t",a)
        else:
            # first go down the sorted list and look for the next pair of adjacent values that equal each other
            a.sort()
            EqualFound = False
            for i in range( len(a)-1 ):
                if( a[i] == a[i+1] ):
                    add = a[i] + 1
                    tmp1 = a[i]
                    tmp2 = a[i+1]
                    a.remove(tmp1)
                    a.remove(tmp2)
                    a.append(add)
                    # now for every number less than the added number, remove and pad to 1's
                    b = a.copy()
                    for i in b:
                        if i < add:
                            a.remove(i)
                    total = 0
                    for i in a:
                        total += i
                    for i in range(total,number):
                        a.append(1)
                    a.sort()
                    count += 1
                    #print(count,"\t",a)
                    EqualFound = True

            if not EqualFound:
                add = a[1] + 1
                a.remove(a[0])   # Remove two lowest values
                a.remove(a[0])
                a.append(add)    # Add the sum of lowest two
                # now for every number less than the added number, remove and pad to 1's
                b = a.copy()
                for i in b:
                    if i < add:
                        a.remove(i)
                total = 0
                for i in a:
                    total += i
                for i in range(total,number):
                    a.append(1)
                a.sort()
                count += 1
                #print(count,"\t",a)
    a.sort(reverse=True)
    print(count,"\t",a)
    print("Counted",count, "in " + str(time.time()-t))
                
        
''' Helper function for pe74() '''
def digitalFactorialChain( n ):
    # returns the number of elements in the digitalFactorialChain
    factorial_lookup = []
    for i in range(10):
        factorial_lookup.append(math.factorial(i))
        
    chain = [n]
    nextChain = 0
    while( 1 ):
        while n != 0:
            nextChain += factorial_lookup[n%10]
            n = n//10
        if( nextChain not in chain ):
            chain.append(nextChain)
            #print(chain)
            n = nextChain
            nextChain = 0
        else:
            break
    return len(chain)
    
        
def pe74():
    # Digital factorial chains
    t = time.time()
    count = 0
    for i in range(1,1000000):   # how many numbers below 1 million...
        if( 60 == digitalFactorialChain(i) ):
            count += 1
        if( i%100000 == 0 ):
            print(i, count, "in " + str(time.time()-t))
    print("Final Count:",count,"in " + str(time.time()-t))

def pe72(D):
    # Counting Fractions
    # count the number of reduced proper fractions for d <= 1000000
    t = time.time()

    tsplit = t        # check split times
    # First, do case n = 1:
    count = D - 1

    # Second, do case for all even numerators:
    for n in range(2,D,2): # n = 2 to d-1, count by 2's
        count += (D-n)//2

    print("Finished Evens; count =",count,"in " + str(time.time()-t))

    # Lastly, consider odd cases:
    split = time.time()
    for n in range(3,D,2):   # range 2 to d-1
        if (is_prime(n)):   # if numerator is prime, add (d-n) - (d-n//n) overlap
            #print(n,"=prime +",(D - n))
            count += (D - n) - (D - n)//n
        else:          # if numerator is odd... 
            for d in range(D,n,-1):  # range d to n-1
                if fractions.gcd(n,d) == 1:  #not commonFactor(n,d):
                    count += 1
            print(n,count,"split",str(time.time()-split),"in " + str(time.time()-t))
        split = time.time()

    print("Counted:",count,"in " + str(time.time()-t))
            
    


def pe71():
    # Ordered fractions
    # find the reduced proper fraction just to the left of 3/7 for d <= 1 million
    t = time.time()
    maxRatio = 0
    maxN = 0
    maxD = 0
    case = 3/7

    # found a pattern, let's try a new test:
    for x in range(1,142856):  # range set because denominator must be <= 1000000
        n = 5+3*x              # so 12+7x <= 1000000 => x <= 142855
        d = 12+7*x
        test = n/d
        if test < case and test > maxRatio:
            maxN = n
            maxD = d
            maxRatio = test
    print("Last N=",maxN,"in "+str(time.time()-t))


''' helper function for pe69() '''
def phi( n ):
    # determine and return the number of values that are relatively prime to n
    pass



def pe69():
    # Totient maximum
    maximum = 0
    
    pass

''' helper function for pe66() '''
def Dio( D ):
    # try to solve for x,y in the equation x^2 - D*y^2 = 1
    # WARNING:: DOES NOT WORK if D is SQUARE!
    if sqrt(D)%1 == 0:
        return 0
    # Also warning.... this brute force approach will not work.
    solved = False
    x = y = 1
    while not solved:
        test = x**2 - D*(y**2)
        #print(test)
        if test == 1:
            return x
        elif test < 1:  # we need a faster method of incrementing X
            x += 1
        else:
            y += 1
            x = math.ceil(sqrt(D*(y**2)))  # This speeds up algorithm by factor 3+
        if( y%1000000 == 0 ):
            print(D,":",x,y,x/y,y*D/x)

def pe66():
    # Diophantine equation  #not 61, 109, 149,157,181
    t = time.time()

    max_x = 0
    for i in range(158,1001):
        test = Dio(i)
        if test > max_x:
            max_x = test
            print(i,max_x,printTime(t))

    print("Done.")



def pe65():
    # Convergents of e (100th)
    # e = [2; 1,2,1, 1,4,1, 1,6,1, ..., 1,2k,1 ...]
    ''' first, create an array of the 99 coefficients (the 100th will be +2) '''
    e_coef = [2]
    for i in range(1,34):  # was 34
        e_coef.append(1)
        e_coef.append(i*2)
        e_coef.append(1)

    num = 1
    den = e_coef.pop(-1)
    for i in range(len(e_coef)):  # repeat for each coefficient
        # 1st -
        new = e_coef.pop(-1)
        num = new*den + num
        # 2nd = flip numerator and denominator for next loop
        tmp = den
        den = num
        num = tmp
        print("num=",den,",den=",num)
        
        stringNum = str(den)
        mySum = 0
        for c in stringNum:
            mySum += int(c)
        print("Sum of num = ",mySum)




def pe64():
    # Odd period Square roots
    pass






''' helper function for pe63 '''
def powerLengthsOf( n ):
    # return the number of integers where x^n == length(n)
    count = 0
    for i in range(1,1000000):
        if( len(str(i**n)) == n ):
            count += 1
        elif( len(str(i**n)) > n ):
            break
    return count


def pe63():
    # Powerful digit counts
    count = 0
    for i in range(100):
        count += powerLengthsOf( i )
        
    print("Counted", count)


''' helper function for pe62() '''
def stringDigitSort( s ):
    # Returns a sorted string of digits
    # s ->   "524332"
    # return "223345"
    sorted_s = ""
    for digit in "0123456789":
        for c in s:
            if( c == digit ):
                sorted_s += c
    return sorted_s

def pe62():
    # Cubic permutations
    # ex: 41063625 (345^3) permutes into 56623104 (384^3) 66430125 (405^3)
    t = time.time()
    # cubes whos roots are 8 digits are between 216 and 464
    # 9-digit cubes have roots 465 - 1000
    # 10-digit cubes have roots 1000 - 2155
    # 11-digit cubes have roots 2155 - 4641
    # 12-digit cubes have roots 4642 - 10000
    minn = 4642
    maxx = 10000
    cube1 = 0
    cube2 = 0
    cube3 = 0
    cube4 = 0
    cube5 = 0
    for i in range(minn,maxx):
        for j in range(i+1,maxx):
            cube1 = i**3
            cube2 = j**3
            test = stringDigitSort(str(cube1))
            if test == stringDigitSort(str(cube2)):
                for k in range(j+1,maxx):
                    cube3 = k**3
                    if test == stringDigitSort(str(cube3)):
                        print(i,j,k,"--",i**3,"\t("+str(round((i-minn)*100/(maxx-minn),1))+"%)")
                        for l in range(k+1,maxx):
                            cube4 = l**3
                            if test == stringDigitSort(str(cube4)):
                                print(i,j,k,l,"--",i**3,printTime(t))
                                for m in range( l+1,maxx):
                                    cube5 = m**3
                                    if test == stringDigitSort(str(cube5)):
                                        print(i,j,k,l,m,"--",i**3,printTime(t))
                                        return
            

def pe61():
    # Cyclical figurate numbers

    # 1st, let's generate a list of all 4-digit Triangle, Square,
    # Pentagonal, Hexagonal, Heptagonal, Octagonal numbers.
    tri = []  #T
    sqr = []  #S
    pent = [] #P
    hexa = [] #X
    hept = [] #H
    octa = [] #O

    for n in range(10000):
        x = n*(n+1)//2
        if x > 999 and x < 10000 and x%100 > 9:
            tri.append(x)
        x = n*n
        if x > 999 and x < 10000 and x%100 > 9:
            sqr.append( n*n )
        x = n*(3*n-1)//2 
        if x > 999 and x < 10000 and x%100 > 9:
            pent.append( x )
        x = n*(2*n-1)
        if x > 999 and x < 10000 and x%100 > 9:
            hexa.append( x )
        x = n*(5*n-3)//2
        if x > 999 and x < 10000 and x%100 > 9:
            hept.append( x )
        x = n*(3*n-2)
        if x > 999 and x < 10000 and x%100 > 9:
            octa.append( x )

    print("lenths:",len(tri),len(sqr),len(pent),len(hexa),len(hept),len(octa))
    print("total:",len(tri)+len(sqr)+len(pent)+len(hexa)+len(hept)+len(octa))

    # make an array of the arrays
    test = [tri,sqr,pent,hexa,hept,octa]

    # create 
    patterns = []
    for a in range(6):
        for b in range(6):
            if( b != a ):
                for c in range(6):
                    if( c != a and c != b ):
                        for d in range(6):
                            if( d != a and d != b and d != c ):
                                for e in range(6):
                                    if( e!=a and e!=b and e!=c and e!=d ):
                                        for f in range(6):
                                            if( f!=a and f!=b and f!=c and f!=d and f!=e):
                                                patterns.append(str(a)+str(b)+str(c)+str(d)+str(e)+str(f))
                                                
                                    
    for pattern in patterns:
        # there are 6! (720) different combinations of number patterns... 
        for a in test[int(pattern[0])]:
            for b in test[int(pattern[1])]:
                for d in test[int(pattern[2])]:
                    if ((a%100 * 100) + b//100) == d:
                        for c in test[int(pattern[3])]:
                            for e in test[int(pattern[4])]:
                                if ((b%100 * 100) + c//100) == e:
                                    #print("Found 5!",a,d,b,e,c)
                                    for f in test[int(pattern[5])]:
                                        if ((c%100 * 100) + a//100) == f:
                                            print("**Found 6!",a,b,c,d,e,f,"=",a+b+c+d+e+f)

    print("Done...")

    return patterns



''' Helper function for pe60 '''
def isSetPrime( p1, p2 ):
    # test whether two concatenated primes are also prime
    return is_prime( int(str(p1)+str(p2)) ) and is_prime( int(str(p2)+str(p1)) )

''' Helper function for pe60 '''
def isTrioPrime( p1, p2, p3 ):
    if not isSetPrime( p1, p2 ):
        return False
    if not isSetPrime( p1, p3 ):
        return False
    if not isSetPrime( p2, p3 ):
        return False
    return True

''' Helper function for pe60 '''
def isQuatroPrime( p1, p2, p3, p4 ):
    if not isSetPrime( p1, p2 ):
        return False
    if not isSetPrime( p1, p3 ):
        return False
    if not isSetPrime( p1, p4 ):
        return False
    if not isSetPrime( p2, p3 ):
        return False
    if not isSetPrime( p2, p4 ):
        return False
    if not isSetPrime( p3, p4 ):
        return False
    return True

''' Helper function for pe60 '''
def isGroupPrime( p1, p2, p3, p4, p5 ):
    if not isSetPrime( p1, p2 ):
        return False
    if not isSetPrime( p1, p3 ):
        return False
    if not isSetPrime( p1, p4 ):
        return False
    if not isSetPrime( p1, p5 ):
        return False
    if not isSetPrime( p2, p3 ):
        return False
    if not isSetPrime( p2, p4 ):
        return False
    if not isSetPrime( p2, p5 ):
        return False
    if not isSetPrime( p3, p4 ):
        return False
    if not isSetPrime( p3, p5 ):
        return False
    if not isSetPrime( p4, p5 ):
        return False
    return True
    
def pe60():
    # Prime pair sets
    # Found: 3, 37, 67, 5923, 194119 : sum = 200149
    # ** Found Group! 13 5197 5701 6733 8389 	(in 12m 8.45s)
    # Sum= 26033
    p = loadPrimes()
    t = time.time()
    maxIndex = 500 # (roughly all primes up to 100k )  len(p)//2

    for a in range(1, 500):
        for b in range(a+1, 700):
            if isSetPrime( p[a], p[b] ):
                for c in range( b+1, 900 ):
                    if isTrioPrime( p[a], p[b], p[c] ):
                        for d in range( c+1, 1100 ):
                            if isQuatroPrime( p[a], p[b], p[c], p[d] ):
                                print("Found Quatro!",p[a],p[b],p[c],p[d],printTime(t))
                                for e in range( d+1, 1100 ):  #p[18000] = 200191
                                    if isGroupPrime( p[a], p[b], p[c], p[d] ,p[e]):
                                        print("** Found Group!",p[a],p[b],p[c],p[d],p[e],printTime(t))
                                        print("Sum=",p[a]+p[b]+p[c]+p[d]+p[e])
                                        #return



    print("Done")

def pe59():
    #XOR decryption
    raw = rawRead('p059_cipher.txt')

    cipher = []
    digit = ''
    for c in raw:
        if c == ',':
            cipher.append(int(digit))
            digit = ''
        else:
            digit += c
    cipher.append(int(digit))

    t = time.time()

    # cipher now contains the original encoded message
    key = [0,0,0]
    found = False
    for a in 'abcdefghijklmnopqrstuvwxyz':
        for b in 'abcdefghijklmnopqrstuvwxyz':
            for c in 'abcdefghijklmnopqrstuvwxyz':
                key[0] = ord(a)
                key[1] = ord(b)
                key[2] = ord(c)
                # key is generated, now we need to XOR decrypt the cypher
                # AND look for some common english words.  let's try to find 'the' first
                keyIndex = 0
                decrypt = []
                for item in cipher:
                    decrypt.append(key[keyIndex]^item)
                    keyIndex += 1
                    if( keyIndex > 2 ):
                        keyIndex = 0

                debugdecrypt = ''
                for item in decrypt:
                    debugdecrypt += chr(item)

                if( 'Gospel' in debugdecrypt ):
                    print("KEY",a+b+c)
                    #print(debugdecrypt)
                    found = True
                    break
            if(found):
                break
        if(found):break
        
    sum = 0
    for c in debugdecrypt:
        sum += ord(c)
    
    print(debugdecrypt,'\n\n' + 'in ' + str(time.time()-t))
    print("Sum=",sum)




def pe58():
    # Spiral primes
    t = time.time()
    
    # let's start a little into the square already
    diags = [3,5,7,9]
    d_primes = 3
    d_notPrimes = 2
    for i in range(4,100000,2):   # count by 2's
        #update next group of diagonals
        diags[0] = diags[3] + i
        diags[1] = diags[0] + i
        diags[2] = diags[1] + i
        diags[3] = diags[2] + i
        for d in diags:
            if( is_prime(d) ):
                d_primes += 1
            else:
                d_notPrimes += 1
        # Check if ratio is below 10%
        if( (d_primes)/(d_primes+d_notPrimes) < 0.10 ):
            print("Ratio of",d_primes,d_primes+d_notPrimes,"is",(d_primes)/(d_primes+d_notPrimes))
            print("Length =",i+1, "in " + str(time.time()-t))
            return
        
        
        



''' helper function for pe57 '''
def sqrootConv( iteration ):
    num = 1
    den = 2
    if iteration == 1:
        return (3,2)
    else:
        for times in range(1,iteration):
            # first, add 2 (2*den/den)
            num += 2*den
            # then flip
            tmp = den
            den = num
            num = tmp
        # last step, add 1 (den/den)
        num += den
    return (num,den)
        
        

def pe57():
    #Square root convergents
    t = time.time()
    count = 0
    for i in range(1,1001):
        test = sqrootConv( i )
        if( len(str(test[0])) > len(str(test[1]))):
            count += 1
    print("Counted",count,'in ' + str(time.time()-t))




''' helper function for pe56 '''
def digitSum( number ):
    # return the sum of the digits of the number
    sum = 0
    for c in str(number):
        sum += int(c)
    return sum

def pe56():
    # Powerful digit sum
    t = time.time()
    max = 0
    for a in range(1,100):
        for b in range(1,100):
            digitsum = digitSum(a**b)
            if digitsum > max:
                max = digitsum
    print("Found max of",max,"in " + str(time.time()-t))
            




''' Helper function: returns a list of permutations of number '''    
def permutationsOf( n ):
    # Assume 4-digit number here
    s = str(n)
    permutationsL = []
    permutationsD = {}
    for i in range(4):
        for j in range(4): 
            for k in range(4):
                for l in range(4):
                    if( i != j and i != k and i != l and j != k and j != l and k != l):
                        permutationsD[s[i]+s[j]+s[k]+s[l]] = 1
    for item in permutationsD:
        permutationsL.append(int(item))
        
    permutationsL.sort()
    return(permutationsL)
                        
''' Helper function: returns a distance list of all distances in given list '''
def distanceListOf( l ):
    # list should be sorted, but we'll sort again to be sure
    l.sort()

    for i in range(len(l)):
        for j in range(i+1,len(l)):
            distance = l[j]-l[i]           # first distance to check
            nextElement = l[j] + distance  # check next distance
            for item in l:
                if( item == nextElement ):
                    print("\nFor prime list:",l)
                    print("We found a match in",l[i],l[j],nextElement,distance)


def addReciprocal( num ):
    # take a number and add it's reciprocal
    rec = ''
    for i in range(len(str(num))-1,-1,-1):
        rec += str(num)[i]
    return num + int(rec)


def lychrelTest( n ):
    # Max 50 attempts to add number to reciprocal and test for palindrome
    attempt = 1
    testSum = addReciprocal(n)
    while( attempt < 50 ):
        if( isPalindrome( str(testSum) ) ):
            #print("Attempts=",attempt,"TestSum=",testSum)
            return True
        else:
            testSum = addReciprocal(testSum)
        attempt += 1
    return False

        

def pe55():
    # Lychrel numbers
    failed = 0
    f = []
    for i in range(10000):
        if( lychrelTest(i)== False ):
            failed += 1
            f.append(i)
    print("Failed:",failed)
    return f

''' helper function for pe54() '''
def processHand( hand ):
    # hand is a list of five cards where
    # the first character represents value and second character
    # represents suit
    # i.e. hand = ['5H', '5C', '6S', '7S', 'KD']
    #
    # processHand will take this hand and output a tuple with
    #  a hand ranking and a tiebreaker value
    #
    # Hand Rankings are as follows:
    # 10 - Royal Flush      5 - Straight
    #  9 - Straight Flush   4 - 3-of-a-kind
    #  8 - Four of a Kind   3 - 2 Pair
    #  7 - Full House       2 - 1 Pair
    #  6 - Flush            1 - High Card

    rank = 0
    high = 0
    pairs = 0
    threes = 0
    fours = 0

    # 1st step, separate values from suit, and check for flush
    value = []
    for card in hand:
        value.append(card[0])
    value.sort()
    # create a string to test for straights
    s = ''
    for item in value:
        s += item

    # Find high card (Generic -- need to adjust if pairs are found...)
    if 'A' in s:
        high = 14
    elif 'K' in s:
        high = 13
    elif 'Q' in s:
        high = 12
    elif 'J' in s:
        high = 11
    elif 'T' in s:
        high = 10
    else:
        high = int(s[-1])

    # count cards
    cardCount = {}
    for v in value:
        if v in cardCount:
            cardCount[v] += 1
        else:
            cardCount[v] = 1
            
    # special 2-pair tie breaker data storage:
    tie = []
    for item in cardCount:
        if( cardCount[item] == 2 ):
            pairs += 1
            high = item  # override high with 2-pair value (if double pair...still need another override)
            tie.append(item)
            tie.sort()
        elif( cardCount[item] == 3 ):
            threes += 1
            high = item  # override high with 3-pair value
        elif( cardCount[item] == 4 ):
            fours += 1
            high = item  # override high with 4-pair value

    flush = False    
    suit = {}  # Make suit a dictionary (only looking for case where length = 1 (only one suit)
    for card in hand:
        suit[card[1]] = 1
    if( len(suit) == 1 ):
        flush = True

    # Check for a straight
    # All possible combinations of a straight are ordered below:
    possibleStraights = ['23456','34567','45678','56789','6789T','789JT','89JQT','9JKQT','AJKQT']
    straight = False
    royal = False
    if s in possibleStraights:
        straight = True
        if s in 'AJKQT':
            royal = True





    #print(hand)
    # Start assigning ranks
    if( royal and flush ):
        rank = 10
    elif( straight and flush ):
        rank = 9
    elif( fours ):
        rank = 8
    elif( threes and pairs ):
        rank = 7
    elif( flush ):
        rank = 6
    elif( straight ):
        rank = 5
    elif( threes ):
        rank = 4
    elif( pairs == 2 ):
        tiestring = ''
        tie.sort()
        for t in tie:
            tiestring += t
        if 'A' in t:
            high = 14
        elif 'K' in t:
            high = 13
        elif 'Q' in t:
            high = 12
        elif 'J' in t:
            high = 11
        elif 'T' in t:
            high = 10
        else:
            high = int(t[-1])        
        rank = 3
    elif( pairs == 1 ):
        rank = 2
    else:
        rank = 1

    # screwed up allowing some high values to be strings.. need to catch at the end here
    if type(high) == str:
        if high == 'A':
            high = 14
        elif high == 'K':
            high = 13
        elif high == 'Q':
            high = 12
        elif high == 'J':
            high = 11
        elif high == 'T':
            high = 10
        else:
            high = int(high)

    ''' DEBUG:    
    print(value)
    print(suit)
    if( royal ):
        print("Royal")
    if( flush and straight ):
        print("Straight Flush Found")
    elif(flush):
        print("Flush Found")
    elif( straight ):
        print("Straight Found")  '''
    return (rank,high)
    

def pe54():
    # Poker Hands
    raw = rawRead('p054_poker.txt')

    hand1 = []
    hand2 = []
    hand1wins = 0
    buffer = ''
    card = 0
    for c in raw:
        if c == ' ' or c == '\n':
            if( card < 5 ):
                hand1.append(buffer)
                card += 1
                buffer = ''
            else:
                hand2.append(buffer)
                card += 1
                buffer = ''
            # if card == 10, time to process hands and declare a winner
            if card == 10:
                r1 = processHand(hand1)
                r2 = processHand(hand2)
                #print(r1,r2)
                if( r1[0] > r2[0] ):
                    hand1wins += 1
                elif( r1[0] == r2[0] and r1[1] > r2[1] ):
                    hand1wins += 1
                hand1 = []
                hand2 = []
                buffer = ''
                card = 0
        else:
            buffer += c

    print("Hand 1 wins",hand1wins,"times")    
    #print(raw)

def pe53():
    # Combinatoric selections
    t = time.time()
    count = 0
    for n in range(1,101):
        for r in range(1,n+1):
            ans = factorial(n)/(factorial(r)*factorial(n-r))
            if( ans//1000000 > 0 ):
                count += 1
    print("Counted",count,"in "+str(time.time()-t))
    

''' Helper function for pe52 '''
def digitsort( number ):
    # returns a string with the sorted digits of a number
    s = str(number)
    l = []
    for c in s:
        l.append(c)
    l.sort()
    new_s = ''
    for item in l:
        new_s += item
    return new_s
        
        

def pe52():
    # Permuted multiples
    # note: number must be below between 10xxxx.. and 16666x.. for 6*number to work
    for i in range(100000,166666):
        if( digitsort(i) == digitsort(2*i) ):
            if( digitsort(i) == digitsort(3*i) ):
                if( digitsort(i) == digitsort(4*i)):
                    if( digitsort(i) == digitsort(5*i)):
                        if( digitsort(i) == digitsort(6*i)):
                            print("Found",i)


''' Helper function for pe51() '''
def pe51test5( n ):
    # test a number for multiple digits & replacement primes
    # return 0 if no multple digits
    # return 'n' number of digit replacment primes
    l = len(str(n))  # holds number of digits
    digits = set()
    for i in range(l):
        digits.add( n%10 )   # add LSD
        n = n//10                # remove LSD
    if len(digits) == l:
        print("no repeats")
    else:
        print("repeats")



def pe51():
    # Prime digit replacements
    p = loadPrimes()
    t = time.time()
    
    count = 0

    return p

    


def pe50():
    # Consecutive prime sum
    p = loadPrimes()

    # Note: p[78000] is over 1 million

    NTERMS = 23

    # find a solution for n = 21 terms
    for NTERMS in range(21,1000):
        sum = 0
        startIndex = 0
        notFound = True
        while( sum < 1000000 ):
            sum = 0   # reset sum
            for i in range(startIndex,startIndex + NTERMS):
                sum += p[i]
                #print(i,p[i],sum)
            if( is_prime(sum) and sum < 1000000 ):
                print("Found",NTERMS,"solution:",sum,"starting at",startIndex)
                notFound = False
                break
            startIndex += 1
        #if( notFound ):
            #print("No Solution Found for",NTERMS)
        
    print("Done.")
    return p


def pe49():
    # Prime permutations
    primes = loadPrimes()

    p4 = []
    
    # want only the 4-digit primes
    for p in primes:
        if( p > 999 and p < 10000 ):
            p4.append(p)

    # p4 is list of 4-digit prime numbers
    tupslist = []
    for item in p4:
        test = permutationsOf( item )
        count = 0
        primesFound = []
        for t in test:
            if( t > 999 and is_prime(t) ):
                count += 1
                primesFound.append( t )
        if(count >= 3):
            primesFound.sort()
            #print("\nFound:",primesFound)
            d = distanceListOf(primesFound)
    print("Done.")


def pe47():
    # Distinct Prime factors
    t = time.time()
    for i in range(90000,300000):
        if( is_prime(i) == False and
            is_prime(i+1) == False and
            is_prime(i+2) == False and
            is_prime(i+3) == False):
            if( distinctPrimeFactors(i) == 4 and
                distinctPrimeFactors(i+1) == 4 and
                distinctPrimeFactors(i+2) == 4 and
                distinctPrimeFactors(i+3) == 4):
                print(i)
                return
        if( i%1000 == 0 ):
            print(i,"@"+str(time.time()-t))

def pe46():
    # Goldbach's other conjecture
    # What is smallest odd composite that cannot be written as
    #  the sum of a prime and twice a square?
    # c = p + 2*s
    ''' first, find some odd composite numbers '''
    for c in range(9,1000000,2):    # start with 9, count by twos
        if( is_prime(c) == False ): # NOT PRIME == Composite #
            # here, i is an odd, composite number. test Goldbach
            found = False
            for p in range(2,999999):
                if( is_prime(p) ):          # for prime numbers p ...
                    for s in range(1,225):  # for square numbers s ...
                        if( c == p + 2*s*s ):
                            found = True
                            break
                if( found ):
                    break
            if( found == False ):
                print("\nDidn't find solution for",c)
                return
        if( c%10000 == 1 ):
            print("x.",end="")


def pe45():
    iTri = 286
    iPent = 166
    iHex = 144
    T = iTri*(iTri+1)//2
    P = iPent*(3*iPent-1)//2
    H = iHex*(2*iHex-1)
    while( T != P or T != H ):
        if( T <= P and T <= H ):
            iTri += 1
            T = iTri*(iTri+1)//2
        elif( P <= T and P <= H ):
            iPent += 1
            P = iPent*(3*iPent-1)//2
        else:
            iHex += 1
            H = iHex*(2*iHex-1)
    print("T-",T,iTri,"P-",P,iPent,"H-",H,iHex)

def isPentagon( num ):
    solution = (1 + math.sqrt(1+24*num))/6
    if solution == solution//1:
        return True
    else:
        return False

def pent2dec( num ):
    if( isPentagon( num )):
        return (1 + math.sqrt(1+24*num))/6
    else:
        return -1

def pe44():
    # Pentagon numbers
    t = time.time()
    p = []
    # Create 10000 pentagon numbers
    for i in range(1,10001):
        p.append(i*(3*i-1)//2)

    for i in range(10000-1):
        for j in range(i+1,10000):
            sum = p[j]+p[i]
            if( isPentagon(sum) ):
                diff = p[j]-p[i]
                if( isPentagon(diff) ):
                    print(p[j],p[i],sum,diff)

    return p
    
    


def pe43():
    # Sub-string divisibility
    mySum = 0
    for a in range(1,10):  # can't have starting 0
        for b in range(10):
            if( b != a ):
                for c in range(10):
                    if( c != b and c != a ):
                        for d in range(10):
                            if( d != c and d != b and d != a ):
                                d234 = 100*b + 10*c + d
                                if( d234%2 == 0 ):   # FIRST TEST
                                    for e in range(10):
                                        if( e != d and e != c and e!=b and e!=a):
                                            d345 = 100*c + 10*d + e
                                            if( d345%3 == 0 ):   # SECOND TEST
                                                for f in range(10):
                                                    if( f!=e and f!=d and f!= c and f!=b and f!=a):
                                                        d456 = 100*d + 10*e +f
                                                        if( d456%5 == 0 ):    # THIRD TEST
                                                            for g in range(10):
                                                                if( g!=a and g!=b and g!=c and g!=d and g!=e and g!=f ):
                                                                    d567 = 100*e + 10*f + g
                                                                    if( d567%7 == 0 ):   # FOURTH TEST
                                                                        for h in range(10):
                                                                            if( h!=a and h!=b and h!=c and h!=d and h!=e and h!=f and h!=g):
                                                                                d678 = 100*f + 10*g + h
                                                                                if( d678%11 == 0 ):   # FIFTH TEST
                                                                                    for i in range(10):
                                                                                        if( i!=a and i!=b and i!=c and i!=d and i!=e and i!=f and i!=g and i!=h):
                                                                                            d789 = 100*g + 10*h + i
                                                                                            if( d789%13 == 0 ):
                                                                                                for j in range(10):
                                                                                                    if( j!=a and j!=b and j!=c and j!=d and j!=e and j!=f and j!=g and j!=h and j!=i):
                                                                                                        d8910 = 100*h + 10*i + j
                                                                                                        if( d8910%17 == 0 ):
                                                                                                            print(a,b,c,d,e,f,g,h,i,j)
                                                                                                            num = str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)+str(h)+str(i)+str(j)
                                                                                                            mySum += int(num)
    print("Sum",mySum)
                                                                        


def isTriangleWord( s ):
    # return TRUE if word is triangle word, False if not
    lookup = "-ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # letter value = lookupl.find( letter )
    sum = 0
    for char in s:
        sum += int(lookup.find(char))
    #print("Sum=",sum)

    # Test for Triangle Word t = n(n+1)/2
    for i in range(500):
        if( sum == i*(i+1)/2 ):
            return True

    return False
    

def pe42():
    # Coded triangle numbers
    raw = rawRead('p042_words.txt')

    wordList = []
    buff = ''
    firstParenth = True
    for c in raw:
        if( c == '"' and firstParenth == True ):
            firstParenth = False
        elif( c == '"' and firstParenth == False ):
            wordList.append(buff)
            buff = ''
            firstParenth = True
        elif( c == ',' ):
            pass
        else:
            buff += c

    count = 0
    for word in wordList:
        if( isTriangleWord( word ) ):
            count += 1
            
    print("Total=",count)
        

                        
def pe41():
    # Pandigital prime
    primes = loadPrimes()

    for p in primes:
        sp = str(p)
        a = []
        for c in sp:
            a.append(c)
        a.sort()
        sp = ''
        for item in a:
            sp += item
        #sp now has ordered text file
        if( len(sp) == 4 ):
            if( sp == '1234' ):
                print("Found:",p)
        elif( len(sp) == 5 ):
            if( sp == '12345' ):
                print("Found:",p)
        elif( len(sp) == 6 ):
            if( sp == '123456' ):
                print("Found:",p)
        elif( len(sp) == 7 ):
            if( sp == '1234567' ):
                print("Found:",p)
        elif( len(sp) == 8 ):
            if( sp == '12345678' ):
                print("Found:",p)
        elif( len(sp) == 9 ):
            if( sp == '123456789' ):
                print("Found:",p)
    print("Done.")


def pe40(max):
    # Champernowne's constant
    a = ''
    for i in range(186000):
        a += str(i)
    ans = int(a[1])*int(a[10])*int(a[100])*int(a[1000])*int(a[10000])*int(a[100000])*int(a[1000000])
    print("length =",len(a))
    print(a[1],a[10],a[100],a[1000],a[10000],a[100000],a[1000000])
    print("Answer =",ans)

''' helper function: test sliding prime'''
def isSlidingPrime( n ):
    # test primes removing right digits
    test = n
    while( test != 0 ):
        if( is_prime(test) == False ):
            return False
        test = test//10

    test = n
    while( test != 0 ):
        if( is_prime(test) == False ):
            return False
        test = test - int(str(test)[0])*10**(len(str(test))-1) 

    # test primes removing left digits
    return True
            
def pe39(num):
    # Integer right Triangles
    maxSolutions = 0
    maxP = 0
    t = time.time()
    for p in range(1,num):
        countSolutions = 0
        for a in range(1,p):
            for b in range(1,p):
                c = (p-a-b)
                if( c > 0 and a*a + b*b == c*c ):
                    countSolutions += 1
                    #print(p,"{",a,b,c,"}")
        solutions = countSolutions/2
        if( solutions > maxSolutions ):
            maxP = p
            maxSolutions = solutions
        # print a time stamp
        if( p%100 == 0 ):
            print(p,"@"+str(time.time()-t))
    
    print("Max Found:",maxP,maxSolutions)
        

def pe37():
    # Truncatable primes
    primes = loadPrimes()

    print("Primes:",len(primes))

    test = 0
    miniprimes = []
    t = time.time()
    for p in primes:
        # filter - cannot begin or end in non-prime number 
        if( str(p)[0] not in '14689' and str(p)[-1] not in '14689'):
            # cannot have even numbers in middle range
            if( '0' not in str(p)[1:-1] and '2' not in str(p)[1:-1]
                and '4' not in str(p)[1:-1] and '6' not in str(p)[1:-1]
                and '8' not in str(p)[1:-1] and p > 9):
                # first 2 digits and last 2 digits cannot be the same (/11)
                if( str(p)[0] != str(p)[1] and str(p)[-1] != str(p)[-2] ):
                    miniprimes.append(p)
    print("End 3-7:",len(miniprimes), "time@" + str(time.time()-t))

    # test miniprimes for sliding prime
    sum = 0
    for p in miniprimes:
        if( isSlidingPrime(p) ):
            sum += p
            print(p)
    print("Final Sum=",sum, "time@" + str(time.time()-t))

    


def pe36():
    total = 0   # sum of all numbers found
    for i in range(1000000):   # all numbers less than one million
        b = bin(i)
        b = b[2:len(b)]
        if( isPalindrome(str(i)) and isPalindrome(b)):
            print("Found:",i,"->",b)
            total += i
    print("Total=",total)

def rotationsOf( n ):
    # return a list of the rotations of n
    # ex: 123 returns List = [123,231,312]
    number = str(n)
    l = []   # empty list
    for i in range( len(number) ):   # repeat number of digits times
        l.append(int(number))        # put number in list
        tmp = number[0]
        number = number[1:len(number)] + tmp
    return l


def pe38():
    # Pandigital multiples
    for integer in range(1,10000):
        sum = ''
        for i in range(1,6):
            sum += str(integer*i)
        tmp = sum[0:9]             # take first 9 terms
        tmpa = []
        for c in tmp:
            tmpa.append(c)
        tmpa.sort()
        tmp = ''
        for a in tmpa:
            tmp += a
        if( tmp == '123456789' ):
            print("Found:",integer,sum)
    print("Done.")
            
        
    
            
        
def pe35():
    # circular primes
    primes = loadPrimes()
    count = 0

    t = time.time()
    
    for prime in primes:
        if( prime > 1000000 ):
            break    # only look at primes under 1 million
        L = rotationsOf( prime )
        primeCheck = 0
        for item in L:
            if( is_prime(item) ):
                primeCheck += 1
        if( primeCheck == len(L) ):
            ''' if all elements in L are prime, count it! '''
            count += 1
    print("Final Count =",count, "in time: " + str(time.time()-t) )
        
    

def pe34(maxNumber):
    # Digital Factorials
    lookup = [1,1,2,6,24,120,720,5040,40320,362880]  #1! - 9!
    total = 0
    for i in range(10,maxNumber):
        si = str(i)
        sum = 0
        for c in si:
            sum += lookup[int(c)]
        if( sum == i ):
            print("Found",i)
            total += sum
    print("Total Sum =",total)

def removeFrom2DigitString(val,string):
    # example: remove('2', '23' ) would return '3'
    # ASSUME 2-digit STRING HERE!!!
    if string.find(val) == 0:
        return string[1]
    else:
        return string[0]

def pe33():
    # Digital cancelling fractions
    count = 0
    for num in range(10,99):
        for den in range(num+1,100):
            # filter some tests:  a common number must exist in num and denom
            if( str(num)[0] in str(den) ):
                # check our cases
                tmp_d = removeFrom2DigitString(str(num)[0],str(den))
                if( int(str(num)[1])/int(tmp_d) == num/den ):
                    print("FOUND:" + str(num) + "/" + str(den))
                    count += 1
            elif( str(den)[1] != '0' and str(num)[1] in str(den) ):
                # check our cases
                tmp_d = removeFrom2DigitString(str(num)[1],str(den))
                if( int(str(num)[0])/int(tmp_d) == num/den ):
                    print("FOUND:" + str(num) + "/" + str(den))
                    count += 1

    print("count",count)

def pe32():
    # Pandigital Products
    store = {}
    for a in range(1,2000):
        for b in range(1,2000):
            c = a*b
            test = str(a) + str(b) + str(c)
            if( len(test) == 9 ):
                # sort and test for pandigital
                x = []
                for ch in test:
                    x.append(ch)
                x.sort()
                test = ""
                for i in x:
                    test += i
                if( test == "123456789" ):
                    store[c] = 1
                    print(a,"x",b,"=",c)
    sum = 0
    for item in store:
        sum += item
    print("Total Sum of products=",sum)
    

def pe31():
    # Coin sums 
    # populate a coins string with XX 1p pieces (a)
    penceNumber = 200
    coins = ''
    for i in range(penceNumber):
        coins += 'a'
    iterations = 1

    while( len(coins) > 1 ):
        # Rule #1: if two 'a's, replace with a 'b'
        if( coins.find('aa') > -1 ):
            coins = coins.replace('aa','b',1)  # replace 1 time
            coins = ''.join(sorted(coins))[::-1]
            iterations += 1
            #print(coins)
        # Rule #2: if no 1's left, (all 2's), convert to 5's and backfill 1's
        elif( coins.find('bba') > -1 ):
            coins = coins.replace('bba','c',1)  # replace 2's with a 5
            coins = coins.replace('b','a'*2)     # and replace all 2's with 1's
            coins = ''.join(sorted(coins))[::-1]
            iterations += 1
            #print(coins)
        elif( coins.find('bbb') > -1 ):
            coins = coins.replace('bbb','ca',1)  # replace 2's with a 5
            coins = coins.replace('b','a'*2)      # and replace all 2's with 1's
            coins = ''.join(sorted(coins))[::-1]
            iterations += 1
            #print(coins)
        # Rule #3: if no 1's/2's, convert 5's to 10's and backfill 1's
        elif( coins.find('cc') > -1 ):
            coins = coins.replace('cc','d',1)   # replace 5's with a 10
            coins = coins.replace('c','a'*5)  # and convert rest to 1's
            coins = ''.join(sorted(coins))[::-1]
            iterations += 1
            #print(coins)
        # Rule #4: if no 1,2,5's, convert 10's to 20's and backfill 1's
        elif( coins.find('dd') > -1 ):
            coins = coins.replace('dd','e',1)   # replace 10's with a 20
            coins = coins.replace('d','a'*10)  # and convert rest to 1's
            coins = ''.join(sorted(coins))[::-1]
            iterations += 1
            #print(coins)
        # Rule #5: convert 20's to 50's and backfill 1's
        elif( coins.find('eed') > -1 ):
            coins = coins.replace('eed','f',1)  # replace 2's with a 5
            coins = coins.replace('e','a'*20)     # and replace all 20's with 1's
            coins = ''.join(sorted(coins))[::-1]
            iterations += 1
            #print(coins)
        elif( coins.find('eee') > -1 ):
            coins = coins.replace('eee','faaaaaaaaaa',1)  # replace 2's with a 5
            coins = coins.replace('e','a'*20)     # and replace all 20's with 1's
            coins = ''.join(sorted(coins))[::-1]
            iterations += 1
            #print(coins)
        # Rule #6: convert 50's to 100 and backfill 1's
        elif( coins.find('ff') > -1 ):
            coins = coins.replace('ff','g',1)   # replace 5's with a 10
            coins = coins.replace('f','a'*50)  # and convert rest to 1's
            coins = ''.join(sorted(coins))[::-1]
            iterations += 1
            #print(coins)
        # Rule #7:  convert 100's to 200's and backfill 1's
        elif( coins.find('gg') > -1 ):
            coins = coins.replace('gg','h',1)   # replace 10's with a 20
            coins = coins.replace('g','a'*100)  # and convert rest to 1's
            coins = ''.join(sorted(coins))[::-1]
            iterations += 1
            #print(coins)
        else:
            break
    print("Iterations=",iterations)

def pe30():
    # digital fifth powers
    sum = 0
    for n in range(100,1000000):  # all four-digit numbers
        a = n//100000
        b = n//10000 - a*10
        c = n//1000 - a*100 - b*10
        d = n//100 - a*1000 - b*100 - c*10
        e = n//10 - a*10000 - b*1000 - c*100 - d*10
        f = n%10
        if( n == (a**5 + b**5 + c**5 + d**5 + e**5 + f**5)):
            print(a,b,c,d,e,f,n)
            sum += n
    print("Total:",sum)

def pe29():
    # Distinct Powers
    # use dictionary as adt to store set of terms
    d = {}
    for i in range(2,101):
        for j in range(2,101):
            d[i**j] = 'a'
    print("Terms count=",len(d))

def pe28(number):
    index = 1   # current number to add
    size  = 1   # current size of matrix
    step = 2    # how much we are incrementing each time
    sum = 1
    while (size < number):
        # do 4 times:
        for i in range(4):
            index += step
            #print("adding",index)
            sum += index

        size += 2 # next size up
        step += 2
    print("pe28 sum=",sum)
            

def pe27():
    # Quadratic primes in form n^2 + an + b, |a|<1000, |b|<1000
    maxA = 0
    maxB = 0
    maxChain = 0
    t = time.time()
    for a in range(-999,1000):
        for b in range(-999,1000):
            chain = 0
            for n in range(1000):
                # we are going to see if we can generate 1000 primes in a row!
                p = n*n + a*n + b
                if( p > 0 and is_prime( p ) ):  # if current n is prime
                    chain += 1                    # increment chain
                else:
                    if( chain > maxChain ):       # if we chain is broken, see if new max
                        maxA = a
                        maxB = b
                        maxChain = chain
                        print("New Max Chain",maxChain,"for",maxA,"and",maxB, "in: " + str(time.time()-t))
                    break
    print("Final product =", maxA*maxB, "in time: " + str(time.time()-t) )
    

def pe26_misnamed():
    # find last ten digits of the power series SUM{n^n}, n = 1000
    sum = 0
    for i in range(1,1001):
        sum += (i**i)%10**10
    print("Answer for pe26 is:",sum%10**10)


def longD(d):
    s = "0."
    R = 10
    for i in range(10000):
        s += str(R//d)
        R = (R%d)*10
    #print(s)
    return s

def pe26():
    # Reciprocal cycles
    savedD = 0
    maxRepeat = 0
    for i in range(1,1000):
        s = longD(i)
        a = s.find(s[10:16],0)
        b = s.find(s[10:16],a+1)
        length = b - a
        if( length > maxRepeat ):
            savedD = i
            maxRepeat = length
            print("Found",i,"gives repeat length",length)
    print("Done.")
    


def pe25():
    # 1st Fibonacci sequence term to have 1000 digits
    a = 1
    b = 1
    for i in range(3, 10000):
        # i = Fi term
        c = a + b  # i-th term
        if c//10**999 > 0:
            print("i=",i,", term=",c)
            break
        a = b
        b = c
        

def pe24():
    # 1 millionth Lexicographic permutation of 1-10
    # try to print out indexes of remaining numbers
    R = 1000001   # remainder..
    s = '' # keep string of indexes
    a = [0,1,2,3,4,5,6,7,8,9]
    for i in range(9,-1,-1):
        s += str(a.pop(R//math.factorial(i)))
        R = R%math.factorial(i)
    print(s)
    

def sumDivisors( n ):
    l = listFactors(n)
    sum = (-1)*n
    for item in l:
        sum += item
    return sum

def pe23():
    # Non-abundant sums
    abundant_numbers = []
    t = time.time()
    for i in range(1,28123):
        s = sumDivisors(i)
        if( s > i ):
            abundant_numbers.append(i)
    print("Found",len(abundant_numbers),"abundant numbers","@"+str(time.time()-t))

    # create a list of possible abundant sums:
    solutions = []
    for i in range(1, 28124):
        solutions.append(i)

    print("Created full solution set, length",len(solutions), "@" + str(time.time()-t))

    # try creating a list of all the sums of abundant numbers!
    abundant_solutions = {}
    for i in range(len(abundant_numbers)):
        for j in range(len(abundant_numbers)):
            abundant_solutions[abundant_numbers[i]+abundant_numbers[j]] = 1

    print("Abundant solutons=",len(abundant_solutions),"@"+str(time.time()-t))
            
    # NOW remove from solutions...
    for key in abundant_solutions:
        try:
            solutions.remove(key)
        except:
            pass
        if(len(solutions)%1000 == 0):
            print("Solutions remaining:",len(solutions),"@"+str(time.time()-t))

    # abundant solutions removed
    '''
    # remove sums of abundant numbers:
    for i in range(len(abundant_numbers)):
        for j in range(i,len(abundant_numbers)):
            asum = abundant_numbers[i]+abundant_numbers[j]
            try:
                solutions.remove(asum)
            except:
                pass
            #if( solutions.count(asum) > 0 ):  # if number exists in solution set
            #    solutions.remove(asum)        # then remove it
        print(i,len(solutions),"@"+str(time.time()-t))
    '''    
    print("Remaining solutions:",len(solutions), "@" + str(time.time()-t))
    sum = 0
    for s in solutions:
        sum += s
    print("Final Sum:",sum)
        
    return solutions


def pe22():
    # name scores
    raw = rawRead('p022_names.txt')
    # format: "NAME","...",...

    firstParenthesis = False
    buff = ''
    names = []
    for c in raw:
        if( c in ',' ):
            pass
        elif( c == '"' and firstParenthesis == False ):
            firstParenthesis = True
        elif( c == '"' and firstParenthesis == True ):
            firstParenthesis = False
            names.append(buff)
            buff = ''
        elif( firstParenthesis ):
            buff += c

    names.sort()
    # Sorted list of names complete.  now we need to get a score
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # build dictonary
    d = {}
    i = 1
    for l in letters:
        d[l] = i
        i+=1

    i = 1
    totalSum = 0
    for eachName in names:
        score = 0
        for eachLetter in eachName:
            score += d[eachLetter]
        totalSum += i*score
        i+=1
    
    print("Length:",len(d),"Processed:",i-1,"TotalSum:",totalSum)
    return names        
    


def pe21():
    # find the sum of all amicable numbers under 10000
    ''' first lets try to find an amicable number pair '''
    for a in range(10001):
        b = d(a)   # find first d()
        c = d(b)
        if( a == c ):
            print("Amicable pair:",a,b)
        
        
        

def pe20():
    a = math.factorial(100)
    sum = 0
    for c in str(a):
        sum += int(c)
    print("The Sum of the digits of 100! is", sum)
    

def pe19():
    # 1 Jan 1900 was a Monday
    # Leap year on any year evenly divisible by 4
    #            Ja  Fe  Ma  Ap  My  Ju  Jy  Au  Sp  Oc  No  De
    month  = [    1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12]
    dmonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    lmonth = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year = 1  # Year starts at 1, goes up to 100
    day = 2   # 1901 starts on a TUESDAY
    sundays = 0
    # for years 1 to 100
    for y in range(1,101):
        # Leap Year case:
        if y%4 == 0:
            for m in month:
                day += lmonth[m]
                if( day%7 == 0 ):
                    sundays += 1
                    print(y+1900, m+1)
        # Regular Year case:
        else:
            for m in month:
                day += dmonth[m]
                if( day%7 == 0 ):
                    sundays += 1
                    print(y+1900, m+1)
    print("We have", sundays, "Sundays.")
    

def pe18(): # also pe67() !!
    # open file triangle_pe18.txt and process into arrays
    #file = open('triangle_pe18.txt', 'r')
    file = open('p067_triangle.txt', 'r')
    raw = file.read()
    file.close()

    # need a 2D array
    col = []
    row = []

    buff = ""
    for c in raw:
        if c == " ":
            row.append(int(buff))
            buff = ""
        elif c == "\n":
            row.append(int(buff))
            col.append(row)
            row = []
            buff = ""
        else:
            buff += c

    # lets flip this triangle upside down:
    col.reverse() # now we can deal with the path top to bottom

    # i = each column row, biggest to smallest, starting with second biggest
    for i in range(1,len(col)):
        # j is range of row 
        for j in range(len(col[i])):
            # check row above. depending on larger element, add that to
            #  the lower row path weight
            if col[i-1][j] > col[i-1][j+1] :
                col[i][j] += col[i-1][j]
            else:
                col[i][j] += col[i-1][j+1]
    
    # flip back
    col.reverse()
    print("Answer is:", col[0][0])
    return col
            

    


def spellNumber(number):
    # WILL WORK UP TO NUMBER 1000
    # used in problem do17
    spell_digits = ["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    spell_tens = ["","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

    # start bulding output string
    spell = ""
    tmp = number;

    if( number >= 1000 ):
        spell += "onethousand"
        print(spell)
        return(len(spell))

    if( tmp//100 > 0 ):
        spell += spell_digits[tmp//100] + "hundred"
        tmp = number - (number//100)*100  # tmp now last two digits
        if( tmp > 0 ):
            spell += "and"
    if( tmp >= 20 ):
        spell += spell_tens[tmp//10]
        tmp = tmp - 10*(tmp//10)
        spell += spell_digits[tmp]
    else:
        spell += spell_digits[tmp]

    print(spell)
    return(len(spell))
        
def do17(number):
    sum = 0
    if( number > 1000 ):
        number = 1000

    for i in range(number):
        sum += spellNumber(i+1)

    print("The Answer is",sum)
    

def do16(size):
    two = 2
    sum = 0
    for i in range(size-1):
        two = 2*two
    for c in str(two):
        sum += int(c)
    print("Answer is:", sum)


def do15(size):
    # build this array out to 40 and return maximum:
    #     1
    #    1 1
    #   1 2 1
    #  1 3 3 1
    # 1 4 6 4 1
    a = [1,1]
    for i in range(size*2-1):
        tmp = [1]
        for j in range(len(a)-1):
            tmp.append(a[j]+a[j+1])
        tmp.append(1)
        a = list(tmp)
    print("Answer is:", max(a))

    
def do14(testNumber):
    s = time.time()
    largestChain = 0
    chainId = 0
    for i in range(testNumber):
        x = i   # work with this number
        steps = 1
        while( x > 1 ):
            if x%2 == 0:
                x = x/2
            else:
                x = 3*x + 1
            steps += 1
        if steps > largestChain:
            largestChain = steps
            chainId = i
            
    print(chainId, "-yields->",largestChain, "in %s" % str((time.time() - s)))
    

def pe13():
    dumb = [37107287533902102798797998220837590246510135740250,
46376937677490009712648124896970078050417018260538,
74324986199524741059474233309513058123726617309629,
91942213363574161572522430563301811072406154908250,
23067588207539346171171980310421047513778063246676,
89261670696623633820136378418383684178734361726757,
28112879812849979408065481931592621691275889832738,
44274228917432520321923589422876796487670272189318,
47451445736001306439091167216856844588711603153276,
70386486105843025439939619828917593665686757934951,
62176457141856560629502157223196586755079324193331,
64906352462741904929101432445813822663347944758178,
92575867718337217661963751590579239728245598838407,
58203565325359399008402633568948830189458628227828,
80181199384826282014278194139940567587151170094390,
35398664372827112653829987240784473053190104293586,
86515506006295864861532075273371959191420517255829,
71693888707715466499115593487603532921714970056938,
54370070576826684624621495650076471787294438377604,
53282654108756828443191190634694037855217779295145,
36123272525000296071075082563815656710885258350721,
45876576172410976447339110607218265236877223636045,
17423706905851860660448207621209813287860733969412,
81142660418086830619328460811191061556940512689692,
51934325451728388641918047049293215058642563049483,
62467221648435076201727918039944693004732956340691,
15732444386908125794514089057706229429197107928209,
55037687525678773091862540744969844508330393682126,
18336384825330154686196124348767681297534375946515,
80386287592878490201521685554828717201219257766954,
78182833757993103614740356856449095527097864797581,
16726320100436897842553539920931837441497806860984,
48403098129077791799088218795327364475675590848030,
87086987551392711854517078544161852424320693150332,
59959406895756536782107074926966537676326235447210,
69793950679652694742597709739166693763042633987085,
41052684708299085211399427365734116182760315001271,
65378607361501080857009149939512557028198746004375,
35829035317434717326932123578154982629742552737307,
94953759765105305946966067683156574377167401875275,
88902802571733229619176668713819931811048770190271,
25267680276078003013678680992525463401061632866526,
36270218540497705585629946580636237993140746255962,
24074486908231174977792365466257246923322810917141,
91430288197103288597806669760892938638285025333403,
34413065578016127815921815005561868836468420090470,
23053081172816430487623791969842487255036638784583,
11487696932154902810424020138335124462181441773470,
63783299490636259666498587618221225225512486764533,
67720186971698544312419572409913959008952310058822,
95548255300263520781532296796249481641953868218774,
76085327132285723110424803456124867697064507995236,
37774242535411291684276865538926205024910326572967,
23701913275725675285653248258265463092207058596522,
29798860272258331913126375147341994889534765745501,
18495701454879288984856827726077713721403798879715,
38298203783031473527721580348144513491373226651381,
34829543829199918180278916522431027392251122869539,
40957953066405232632538044100059654939159879593635,
29746152185502371307642255121183693803580388584903,
41698116222072977186158236678424689157993532961922,
62467957194401269043877107275048102390895523597457,
23189706772547915061505504953922979530901129967519,
86188088225875314529584099251203829009407770775672,
11306739708304724483816533873502340845647058077308,
82959174767140363198008187129011875491310547126581,
97623331044818386269515456334926366572897563400500,
42846280183517070527831839425882145521227251250327,
55121603546981200581762165212827652751691296897789,
32238195734329339946437501907836945765883352399886,
75506164965184775180738168837861091527357929701337,
62177842752192623401942399639168044983993173312731,
32924185707147349566916674687634660915035914677504,
99518671430235219628894890102423325116913619626622,
73267460800591547471830798392868535206946944540724,
76841822524674417161514036427982273348055556214818,
97142617910342598647204516893989422179826088076852,
87783646182799346313767754307809363333018982642090,
10848802521674670883215120185883543223812876952786,
71329612474782464538636993009049310363619763878039,
62184073572399794223406235393808339651327408011116,
66627891981488087797941876876144230030984490851411,
60661826293682836764744779239180335110989069790714,
85786944089552990653640447425576083659976645795096,
66024396409905389607120198219976047599490197230297,
64913982680032973156037120041377903785566085089252,
16730939319872750275468906903707539413042652315011,
94809377245048795150954100921645863754710598436791,
78639167021187492431995700641917969777599028300699,
15368713711936614952811305876380278410754449733078,
40789923115535562561142322423255033685442488917353,
44889911501440648020369068063960672322193204149535,
41503128880339536053299340368006977710650566631954,
81234880673210146739058568557934581403627822703280,
82616570773948327592232845941706525094512325230608,
22918802058777319719839450180888072429661980811197,
77158542502016545090413245809786882778948721859617,
72107838435069186155435662884062257473692284509516,
20849603980134001723930671666823555245252804609722,
53503534226472524250874054075591789781264330331690]
    sum = 0
    for d in dumb:
        sum += d
    print(sum)


def pe12(number):
    max = 0
    t = time.time()
    for i in range(1,number+1):
        # calculate the triangle number
        n = i*(i+1)//2
        f = countFactors(n)
        if( f > max ):
            max = f    # save new max factor count
            print(i,"=>#",n,"has",f,"factors - time:" + str((time.time()-t)) )
    print("done")



def pe11():
    raw = rawRead("pe11_square.txt")
    a = []
    row = []
    buff = ''
    for c in raw:
        if c == " ":
            row.append(int(buff))
            buff = " "
        elif c == "\n":
            row.append(int(buff))
            a.append(row)
            row = []
            buff = ''
        else:
            buff += c

    largest_product = 0
    # check 4 cases for largest sum:
    ''' 4 in a horizontal row... '''
    for c in range(20):
        for r in range(16):
            tmp = a[c][r]*a[c][r+1]*a[c][r+2]*a[c][r+3]
            if tmp > largest_product:
                largest_product = tmp # save new highest
    print("Largest so far:", largest_product)

    ''' 4 in a vertical row... '''
    for r in range(20):
        for c in range(16):
            tmp = a[c][r]*a[c+1][r]*a[c+2][r]*a[c+3][r]
            if tmp > largest_product:
                largest_product = tmp # save new highest
    print("Largest so far:", largest_product)

    ''' 4 in a \ row '''
    for c in range(16):
        for r in range(16):
            tmp = a[c][r]*a[c+1][r+1]*a[c+2][r+2]*a[c+3][r+3]
            if tmp > largest_product:
                largest_product = tmp # save new highest
    print("Largest so far:", largest_product)

    ''' 4 in a / row '''
    for c in range(4,20):
        for r in range(16):
            tmp = a[c][r]*a[c-1][r+1]*a[c-2][r+2]*a[c-3][r+3]
            if tmp > largest_product:
                largest_product = tmp # save new highest
    print("Largest so far:", largest_product)

    return    
        




    

def pe10():
    sum = 0
    t = time.time()
    for i in range(2,2000000):
        if( is_prime(i) ):
            sum += i
        if( i%100000==0 ):
            print(i, " time:" + str((time.time()-t)))
    print("Sum=", sum, " time:" + str((time.time()-t)))
    return



def pe09():
    print("pe09")
    for a in range(500):
        for b in range(500):
            if (( a + b + sqrt(a*a + b*b) ) == 1000 ):
                print(a,b, sqrt(a*a + b*b), a*b*sqrt(a*a + b*b))
    print("done")
    return



def pe08(number):
    # 13 adjacent digits with greatest product
    # read file pe8_number.txt
    raw = rawRead('pe8_number.txt')

    # clean up raw data
    clean = ''
    for c in raw:
        if c == '\n':
            doNothing = 0
        else:
            clean += c

    best = 0
    for i in range(len(clean)-number):
        product = 1
        for j in range(number):
            product *= int(clean[i+j])
        if( product > best ):
            best = product
            
    print("Out of",number,", greatest product is", best)





def pe07(maxp):
    # 10001st prime number
    t = time.time()

    count = 0
    start = 1
    while count < maxp:
        start += 1
        if is_prime(start):
            count += 1

    print("Found",maxp,"prime:", start, printTime(t))



def pe06(number):
    # Sum Square Difference
    sumsquared = 0
    squaredsum = 0

    for i in range(number+1):
        sumsquared += i*i
        squaredsum += i
    squaredsum *= squaredsum
    print("Answer is:",squaredsum-sumsquared)
    

def pe05():
    # smallest number divisible by all numbers 1 to 20
    # note: must be divisible by 11-20 to = same case
    for i in range(21):
        print(listPrimeFactors(i))
    print("Just Pull out highest combos of prime factors")
        


def pe04():
    # largest palindrome of product of 3 numbers
    # 100*100 = 10000
    # 999*999 = 998001
    count = 0
    for i in range(998001,900000,-1):
    #for i in range(10000,998001):
        if( isPalindrome(str(i)) ):
            factors = listPrimeFactors(i)
            if( max(factors) < 1000 ):
                print(i, factors)
            count += 1
    print(count)




'''
Print lowest prime factor
(Use recursively)
'''
def printPrimeFactors( x ):
    # base case
    if( x == 1 ):
        print("Done.")
        return
    for i in range(2, x+1):  # include all numbers up to x
        if( x%i == 0 ):
            n = i
            print(n)
            printPrimeFactors( x//i )
            return


def pe03():
    # largest prime factor of 600851475143
    printPrimeFactors(600851475143)
    

def pe02():
    fibby = [1,1]
    # first generate a Fibonacci sequence whos values are < 4 million
    breaky = 0
    while( breaky < 4000000 ):
        breaky = fibby[-1] + fibby[-2]
        fibby.append(breaky)
    print("Size of fibby array is", len(fibby))
    # now sum up the even valued terms:
    sum = 0
    for f in fibby:
        if f%2 == 0:
            sum += f

    print("The sum of evens is", sum)
    

def pe01():
    sum = 0
    for i in range(1000):
        if( i%3 == 0 or i%5 == 0):
            sum += i
    print("The Answer is", sum)
    

        
        
    
if __name__ == '__main__':
    print("GO")
    out = pe131()


