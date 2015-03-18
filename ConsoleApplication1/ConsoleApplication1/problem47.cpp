//Author: Stephen Kinser
//Problem 47
/*
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
*/
#include<iostream>
#include<queue>
int distinct(double value);
int main(){
	
	int amount = 4;
	std::queue<double> mystack;
	for (double i = 13043; i < 10000000; i++){
		if (distinct(i) == amount ){
			mystack.push(i);
			
		}
		else{
			for (int i = 0; i < mystack.size(); i++){
				mystack.pop();
			}
		}
			
		if (mystack.size() == amount){
			std::cout << mystack.front() << '\n';
		}
	}
	
	return 0;
}
int distinct(double value){
	int length = 0;
	//int upperbound = sqrt(value);
	double oldValue=value;
	for (int i = 2; value!=1; i++){
		if (fmod(value,i) == 0){		//normally if()

			length++;
			while (fmod(value,i) == 0){
				value /= i;//this is normally in while loop
			}
			
		}
	}
	return length;
}