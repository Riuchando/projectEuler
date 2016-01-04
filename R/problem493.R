#70 colored balls are placed in an urn, 10 for each of the seven rainbow colors.
#What is the expected number of distinct colors in 20 randomly picked balls?
#Give your answer with nine digits after the decimal point (a.bcdefghij).
#sum(sapply(0:20 ,function(x){choose(70-x,x)*((1/7)^(70-x))*((6/7)^x) }))

sprintf("%.9f",7*(1-choose(60,20)/choose(70,20)))

