//Author: Stephen Kinser
//Problem 97
/*
The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime of the form 26972593−1; it contains exactly 2,098,960 digits. Subsequently other Mersenne primes, of the form 2p−1, have been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433×27830457+1.

Find the last ten digits of this prime number.

*/
#include<iostream>

int main(){
	long long value = 28433;
	long long modVal = 10000000000;//amount of required digits
	
		long long temp = 2;	// not nessarilly needed it is used to hold the number while a secondary number is the base eg 2^5: temp holds 2*2*2*2*2, but through each iteration something holds 2;

		for (int j = 2; j <= 7830457; j++){//modular expansion
			temp = temp * 2 % modVal;
		}
		value = (value * temp) % modVal;
		value++;
	std::cout << value;


	return 0;
}