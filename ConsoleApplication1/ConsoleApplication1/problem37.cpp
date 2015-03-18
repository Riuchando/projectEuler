//Author: Stephen Kinser
//problem 37
/*
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
*/

#include<iostream>//for out put, also it includes fmod() now?
#include<string>//because I hate char*, also to_string is useful
#include<math.h>//for trunc(), which takes care of remainders in doubles
bool prime(double answer);
bool truncatable(double answer);
int main(){
	
	int answer= 0;//self explainitory
	double answers[11]{};//for debugging purposes
	int count = 0;//problem says there are EXACTLY 11 primes
	double i = 11;// it says that the first 4 primes don't count
	while (count < 11){
		if (truncatable(i)==true){
			answers[count] = i;
			answer+= i;
			count++;
			
		}
		int leastsig = fmod(i , 10);
		//the least signifigant digit for primes will ALWAYS end in either 1,3,7,9 it can't be 9, becuase when truncated, 9 isn't prime
		if (leastsig == 1){
			i += 2;
		}
		else{ //should be 3 or 7
			i += 4;// this will make 3->7 and 7->1
		}

	}
	std::cout << answer << '\n';

	return 0;
}
bool prime(double answer){
	if (answer == 1){//special case
		return false;
	}
	if (answer == 2){//because I'm lazy in my algoritm to fix it
		return true;
	}
	for (int i = 2; i < sqrt(answer) + 1; i++){
		if (fmod(answer, i) == 0){
			return false;
		}
	}
	return true;
}
bool truncatable(double answer){
	double left = answer;
	double right = answer;
	while (left > 0){
		if (!prime(left)){
			return false;
		}
		left = trunc(left/10);//delete the least signifigant digit
	}
	while (right > 0){
		if (!prime(right)){
			return false;
		}
		std::string mostSig = std::to_string(right);//make it a string
		mostSig.erase(mostSig.begin());//delete the most signifigant digit
		right = std::stod(mostSig);//convert it back
	}
	return true;
}