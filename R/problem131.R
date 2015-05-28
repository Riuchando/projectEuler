library(matlab)

counter=0
a= 2
b=a-1
prime=( a^3 %% b^2 )
while(prime <100){
b=a-1
	while(b < a){
	prime=( a^3 %% b^2 )
	if (as.logical(isprime(prime))== T){
	counter= counter +1
}
	b= b+1
}
	a= a +1
}

counter