#include<Rcpp.h>
#include<iostream>
#include<math.h>

unsigned int primes[]={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47};
//primes length=13
RcppExport SEXP nodsq(SEXP a){
  Rcpp::NumericVector xa(a);
  int n_xa = xa.size();
  for(int i=0; i<n_xa; i++){
    long nod =1;
    long exponent;
    long remain = xa[i];
    for(int j=2; j <xa[i] * log2(xa[i]); j++){
      if(j * j > xa[i]){
        xa[i]=nod*2;
        break;
}
      exponent =1;
      while(remain % j == 0){
        exponent+=2;
        remain = remain / j;
}
      nod*= exponent;
   if(remain == 1){
      xa[i]=nod;
      break;
}
}
//xa[i]= nod; 
}
return xa;

}
RcppExport SEXP localmax(SEXP a){
  Rcpp::NumericVector xa(a);
  int n_xa = xa.size();
  Rcpp::NumericVector answer(27);
  int max=0;
  int count=0;
  for(int i=0; i<n_xa; i++){
    if(xa[i] > max){
      max = xa[i];
      answer[count]=xa[i];
      count++;
}
}
  return answer;
}
//int primes[]={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47};
RcppExport SEXP boundsChecker(){
  Rcpp::NumericVector answer(50);
  int count =0;
  int thing=8000001;
//  thing
  while(count < 50){
    if((thing % 405)== 0){
      answer[count]=thing;
      count++;
}
    thing+=2;
}
//answer[0]=thing;
return answer;
/*  for(int i= 1; i< 24; i++){
    answer[i]= answer[i-1]* 2;

}*/
//primes 3x
/*  for(int i= 1; i< 6; i++){
    answer[i]= answer[i-1]* primes[i];
}
//primes 3x + 1 time 5x
for(int i= 6; i< 12; i++){
    answer[i]=answer[i-6]*2;

}
//primes 3x + 1 time 5x
for(int i= 12; i< 18; i++){
    answer[i]=answer[i-12]*3;

}
//primes 3x + 1 time 7x
for(int i= 18; i< 24; i++){
    answer[i]=answer[i-12]*2;

}
//primes 3x +1 time 25x
for(int i= 24; i< 30; i++){
    answer[i]=answer[i-18]*3;

}
for(int i= 30; i< 36; i++){
    answer[i]=answer[i-30]*5;

}
*/
return answer;
}
