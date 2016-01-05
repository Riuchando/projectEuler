#Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
#Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.
#Peter and Colin roll their dice and compare totals: the highest total wins. The result is a draw if the totals are equal.
#What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer rounded to seven decimal places in the form 0.abcdefg

truthTable=table(sapply(1:6 ,function(x){x>1:4}))
#get the amount of truth
truth=as.data.frame(truthTable)[2,2]
#the probability of any given event happenening is 1/4*1/6, so the probability is 
sprintf("probability %7f",truth*(1/24))
#for multiple dice it would be: 
#for peter
acc=1:4
for(i in 1:8){
acc=sapply(acc, function(x){x+1:4})
}
peter=as.data.frame(table(acc))
peter$acc=as.numeric(levels(peter$acc))
#for colin
acc=1:6
for(i in 1:5){
  acc=sapply(acc, function(x){x+1:6})
}

colin=as.data.frame(table(acc))
colin$acc=as.numeric(levels(colin$acc))
truthTable=sapply(colin$acc ,function(x){x<peter$acc})

colin$probs=sapply(colin$Freq, function(x) { x/sum(colin$Freq)})
peter$probs=sapply(peter$Freq, function(x) { x/sum(peter$Freq)})
probsTable=sapply(colin$probs ,function(x){x*peter$probs})
sprintf("probability %.7f",sum(probsTable[truthTable]))
