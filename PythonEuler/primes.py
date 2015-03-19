from math import sqrt


def isPrime( n ):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    i = 3
    sqrtOfNumber = sqrt(n)
    
    while i <= sqrtOfNumber:
        if n % i == 0:
            return False
        i = i+2
        
    return True  
