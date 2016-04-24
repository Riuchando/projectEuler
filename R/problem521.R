setwd("C:\\Users\\Stephen\\Documents\\GitHub\\projectEuler\\R")

library("Rmpfr")
Primes <-mpfr(scan("PrimeNumbers.txt"),128)
length(Primes)
Primes[length(Primes)]
Prime <- rev(Primes)

rep(Primes,(floor((10^12)/Primes))) 
things <- read.table("problem521.txt")
number =things$V1*things$V2
sum(number)
