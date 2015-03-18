//Author:Stephen Kinser
//Problem 23
/*
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

*/
#include<iostream>
#include"reducibleFractions.h"
#include<vector>
#include<algorithm>
int main(){
	//int answer = 253; //n*(n-1)/2 //23*22/2
	int answer = 0;
	std::vector<int> abundant;
	std::vector<int>::iterator aIt, alt;
	for (int i = 1; i < 28123; i++){
		rF temp(i, true);
		
		if (temp.abundant(i)){
			abundant.push_back(i);	
		}
		bool possible = true;
		int pos = 0;
		for (aIt = abundant.begin(); aIt != abundant.end() && (*aIt) <= i / 2 ; aIt++){
			alt = find(abundant.begin() + pos, abundant.end(), i - (*aIt));
			if (alt != abundant.end())
				break;
			else
				pos++;
		}
		if (aIt == abundant.end() || (*aIt) > i / 2){
			answer += i;
		}
	}

	std::cout << answer << '\n';
	return 0;
}