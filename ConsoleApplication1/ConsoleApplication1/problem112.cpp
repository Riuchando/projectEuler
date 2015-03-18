//Author: Stephen Kinser
// Proble 112
/*
Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.
*/

#include<iostream>
#include<string>
bool bouncy(std::string number);
int main(){
	double ratio = 0.0;
	int bouncyAmount = 0;
	int num;
	for ( num = 100; ratio != .99; num++){
		if (bouncy(std::to_string(num))){
			bouncyAmount++;
		}
		ratio = (double)bouncyAmount / num ;
	}
	std::cout << num << '\n';

	return 0;
}
bool bouncy(std::string number){
	bool increasing = true;
	bool decreasing = true;
	char first;
	for (int i = 0; i < number.length()-1; i++){
		if (increasing == true&& number[i]<number[i+1]){
			increasing = false;
		}
		if (decreasing == true && number[i]>number[i + 1]){
			decreasing = false;
		}
	}
	return !increasing && !decreasing;
	
}