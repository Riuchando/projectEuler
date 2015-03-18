//Author : Stephen Kinser
//Problem 73
//find all reduced fractions between 1/2 and 1/3
#include"reducibleFractions.h"
#include<iostream>

int main(){
	const double upperbound = 0.5;
	const double lowerbound = 0.33333333333;
	int answer = 0;
	int num;
	//efficiently brute force it, there's probably an algebraic solution similar to 72
	for (int d = 4; d <= 12000; d++){
		rF mine(d, true);
		num = d / 2;//the number to the immidiate left is the cross multiplication of these numbers
		double temp = (double)num / d;// find the number that closely approximates it
		
		while (temp > lowerbound){
			if (!mine.reducible(num)){
			answer++;
		}
			num--;
			temp = (double)num / d;
		}
		

	}
	std::cout << answer << '\n';


	return 0;
}