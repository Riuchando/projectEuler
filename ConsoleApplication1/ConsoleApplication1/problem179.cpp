//Author: Stephen Kinser
// Problem 179
#include<iostream>
#include"reducibleFractions.h"
int main(){
	int prev = 1;
	int answer = 0;
	for (long long i = 2; i < pow(10, 7); i++){
		rF curr(i, true);
		if (curr.getLength() == prev){
			answer++;
		}
		prev = curr.getLength();
	}

	std::cout << answer << '\n';

	return 0;
}