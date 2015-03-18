//Author:Stephen Kinser
//Problem 5
/*
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
*/

#include<iostream>
#include<iomanip>
bool divisible(int i);

int main(){
	double i;
	double upper = 20000000000000000000000.0;
	for (i = 100; i < upper; i ++){
		if (divisible(i)==true){
			std::cout <<std::setprecision(160)<< i << '\n';
			//break;
		}

	}

	return 0;
}
bool divisible(int i){
	for (int j = 2; j < 20; j++){
		if (i%j != 0){
			return false;
		}

	}
	return true;
}