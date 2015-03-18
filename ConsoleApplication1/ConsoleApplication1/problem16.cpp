//Author: Stephen Kinser
//Problem 16
//find the sum of the digits of 2^1000

#include"bigNum.h"
#include<iostream>

int main(){
	bigNum two;
	two.initialize(2);//since I'm too lazy to include this in the default constructor

	two.bPow(1000);//2^1000
	int answer = two.sumDigits();//sum the digits
	std::cout<<"Actual Number: "<<two<<'\n'<<"answer: "<< answer << '\n';
	return 0;
}