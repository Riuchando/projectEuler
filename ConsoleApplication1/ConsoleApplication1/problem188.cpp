//Author:Stephen Kinser
//Problem 188

#include<iostream>

long long gcd(long long, long long);
long long findTotient(long long);
int main(){
	/*long long answer = 1777;
	long long currenteval=1;
	long long sigDigits = pow(10, 9);
	for (int j = 1855; j > 0; j--){
		for (int i = answer; i > 0; i--){
			currenteval = (1777 * currenteval) % sigDigits;
		}
		answer = currenteval;
	}*/

	long long answer = findTotient(1855);

	std::cout << answer << '\n';
	return 0;
}
long long gcd(long long a, long long b){
	/*finds the greatest common divisor of two numbers, meaning which number would 
	evenly divide two numbers eg 3, 6 = 3*/
	long long temp;
	while (a%b != 0){
		temp = b;
		b = a%b;
		a = temp;
	}
	return b;
}
long long findTotient(long long upperbound){
	/*
	there is a term called co-prime, if the greates common divisor of two numbers is 1, it is said these two numbers are co-prime
	there is another term called totient, which is the amount of numbers that are co prime with the starting number
	it can be proven that all prime numbers' totient is equal to the prime number-1

	*/
	long long totient;
		totient = 1;
		
			for (int j = upperbound - 1; j >= 2; j--){
				if (gcd(upperbound, j) == 1){
					totient++;
				}
			}
			return totient;

	}