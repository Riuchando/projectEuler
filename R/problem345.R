is.installed <- function(mypkg){
	     is.element(mpkg, installed.packages()[,1])
}
if(!is.installed("clue")){
	install.packages("clue")
}

library(clue)

mydata = read.table("largeSet.txt")

x <- as.matrix(mydata)
y<- solve_LSAP(x, maximum=T)
sum(x[cbind(seq_along(y),y)])