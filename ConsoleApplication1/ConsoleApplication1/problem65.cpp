//Author: Stephen Kinser
//Problem 65
/*

ERRORS WITHIN CODE


*/
#include<iostream>
#include<string>
#include"bigNum.h"
int main(){
	long long convergent = 1;
	long long iteration = 2;
	bigNum curr_num, prev_num, next_num;
	bigNum curr_den, prev_den, next_den;
	prev_num.initialize(3);
	prev_den.initialize(1);
	curr_num.initialize(8);
	curr_den.initialize(3);
	while (convergent <= 100){
		if (convergent % 3 == 0){
			bigNum temp;
			temp.initialize(iteration * 2);
			
			next_num = prev_num + temp*curr_num;
			//next_den = prev_den + (iteration * 2)*curr_den;
			iteration++;
		}
		else{
			next_num = prev_num + curr_num;
			next_den = prev_den + curr_den;
		}
		prev_den = curr_den;
		prev_num = curr_num;
		curr_num = next_num;
		curr_den = next_den;
		convergent++;
	}
	int answer = curr_num.sumDigits();
	
	std::cout << answer << '\n';
	return 0;
}