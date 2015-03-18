//Author: Stephen Kinser
//Problem 41

/*
	We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
*/
#include<iostream>
#include<string>
bool prime(double one);
double factorial(int one);
int main(){
	std::string original = "1234567";
	int size = original.length()-1;
	int* whichSwaps= new int[size];
	int* amountOfSwaps= new int[size];
	double answer = 0;
	for (int i = size-1; i >= 0; i--){
		whichSwaps[i] = factorial(i + 1);

	}
	long long position = factorial(size+1) - 1;
	long long position2 = factorial(size + 1) - 1;
	for (int l = 0; l<position2; l++){
		position = factorial(size+1) - 1- l;
		original = "1234567";
		for (int k = size-1; k >= 0; k--){
			amountOfSwaps[k] = (int)position / whichSwaps[k];
			position = fmod(position, whichSwaps[k]);
		}
		std::string empty = "";
		for (int k = 0; k < size; k++){
			char temp = original[amountOfSwaps[size-1 - k]];
			original.erase(original.begin() + amountOfSwaps[size-1 - k]);
			empty += temp;
		}
		empty += original[0];
		//empty += '\0';
		//std::string::size_type sz;   // alias of size_t
		//const std::string why = empty;
		answer = std::stod(empty);
		if (prime(answer)){
			break;
		}

	}
	std::cout << answer << '\n';
	return 0;
}
double factorial(int one){
	double answer = 1.0;
	for (int i = one; i >= 2; i--){
		answer *= i;
	}
	return answer;
}
bool prime(double answer){

	for (int i = 2; i < sqrt(answer)+1; i++){
		if (fmod(answer,i) == 0){
			return false;
		}
	}
	return true;
}