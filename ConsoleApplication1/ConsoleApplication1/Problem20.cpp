//Author:Stephen Kinser
//Problem 20
/*

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

*/
#include <iostream>
#include<math.h>//no longer needed
#include<iomanip>//no longer needed
int main(){
	int answer=0;
	/*long long int fact = 1;
	for (int i = 2; i <= 100; i++){// definition of 100!
		fact = fact*i;
	}
	*/
	int fact[1000];
	fact[0] = 1;
	for (int i = 2; i <= 100; i++){
		
		//note: the following line of code is dangerous, because it assumes uninisialized values are negative
		for (int j = 0; fact[j] > -1; j++){
			fact[j] *= i;
		}
		for (int k = 0; fact[k] > 10 || fact[k+1] >-1 ;k++){
			//if the next most signifigant digit is defined, then add the overflow to it, otherwise, initialize it
			fact[k + 1] = fact[k + 1] > -1 ? fact[k + 1] + int(fact[k] / 10) : int(fact[k] / 10);
			fact[k] = fact[k] % 10;
			
		}
	}
	/*while (fact > 0){
		answer += std::fmod(fact, 10);// should get the least signifigant digit
		fact = trunc(fact / 10);// should drop off the least signifgant digit

		}*/
	//it asked for the summation of each digit of the essentially the string
	for (int j = 0; fact[j] > -1; j++){
		answer += fact[j];
	}
	

	std::cout <<answer << '\n';


	return 0;
}