//Author: Stephen Kinser
//Problem 53
/*
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr =n!/r!(n−r)!
,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?


*/

#include<iostream>

bool modifiedFactorial(int one, int two);
int main(){
	int fact = 1;
	int i;
	int answer = 0;
	/*for ( i = 1; fact < 1000000; i++){
		fact = i*fact;
	}
	std::cout << i;
	//proof that 10! is >1,000,000
	// not necessary with new formula
	*/
	for (int j = 10; j <= 100; j++){
		for (int k = j-1; k >= 2 ; k--){
			if (modifiedFactorial(j, k)){
				answer++;
			}
		}
	}
	std::cout << answer << '\n';
	return 0;
}
bool modifiedFactorial(int one, int two){
	int three = one - two;
	/*
	consider 23! which is 23*22*21*20.....
	23!/23!= 1
	23!/22!= 23 : you would subtract all the factorials, since they overlap
	23!/21= 23*22
	23!/20!= 23*22*21
	... and so on
	given 23!/n!(23-n)!:
	from 23 to n, figure out which ones are above 1,000,000
	consider 23!/10!(23-10)!
	from 23 to 10
		factorial =(23 /10)*(22/9)*(21/8)*(20/7)*(19/6)*(18/5)....
		if factorial > 1000000, then return true, for this problem
	*/
	double fact = 1;
	bool flag = false;
	while( true){			//could make while true and add a break statement later
		fact *= (double) one / two;
		if (fact > 1000000){
			flag = true;
			break;
		}
		one--;
		two--;
		if (one == three){
			break;
		}
	}
		return flag;
}