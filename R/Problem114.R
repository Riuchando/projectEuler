#A row measuring seven units in length has 
#red blocks with a minimum length of three units placed on it, 
#such that any two red blocks 
#(which are allowed to be different lengths) are separated by at least one black square.
#There are exactly seventeen ways of doing this.
sapply(0:2 , function(x){choose(7-x,x)})
sapply(0:4 , function(x){choose(7,x)})
sum(sapply(0:16 , function(x){choose(50-x,x)}))
#sapply(0:6 , function(x){choose(6,x)})

#sapply(0:7, function(x){combn(7,x)})
library(permute)
pers=permn(c(1,2,3,4,5,6,7,8,9))
pers[1]
isPrime <-function(x){
  return(!any(x%%(2:x^(1/2))==0))
}

#sapply(3:100,function(x){isPrime(x)})

log(10:512)
sumdigits <-function(num){
return(sum(sapply(strsplit( as.character(num) , ""),function(y){as.integer(y)})))
}
log(512,8)

this=which(sapply(10:248155780267521 , function(x){
        y=log(x,sumdigits(x))
        return (y==as.integer(y))}
       )
)
length(this)
log(248155780267521,sumdigits(248155780267521))

system=cbind(
c(1,1,0),
c(1,-1,0),
c(1,0,1),
c(1,0,-1),
c(0,1,1),
c(0,1,-1))
apply(system*c(1,2,3),2,function(x){return(log2(sum(x)))})
log2(4:10)
