library(Rcpp)
#library(surveillance)
library(TTR)

dyn.load('nodsquared.so')
##primes= c(2,3,5,7,11,13,17,19)

numbers = seq(1, 200000, by=1)
#primes <- .Call('boundsChecker')
#primes


numofPFsq = .Call('nodsq',numbers)
pos <- which((numofPFsq +1) /2 >1000)
pos
#things =lapply(primes,  primeFactors())


#NOD= .Call('nodsq',primes)
#NOD
#localmax = .Call('localmax', numofPFsq)
#localmax


lROC = ROC(localmax, type="discrete")*100
lROC


#pdf("numofPF.pdf")
#plot(numofPFsq)

pdf("localmaxroc.pdf")
plot(lROC, col ="red", main="rate of change in growth of a Diophantine Reciprocal")
lines(lROC, col="red")
dev.off()