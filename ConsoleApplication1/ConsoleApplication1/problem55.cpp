//Author:Stephen Kinser
//Problem 55
/*
If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. A number that never forms a palindrome through the reverse and add process is called a Lychrel number. Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise. In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).

Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

How many Lychrel numbers are there below ten-thousand?

*/
#include<iostream>
#include<string>
double reverse(double in);
bool lychrel(double in);
bool palindrome(std::string in);
 int main(){
	double answer = 0;
	for (int i = 10; i < 10000; i++){
		if (lychrel(i)){
			answer++;
		}
	}
	std::cout << answer << '\n';
	return 0;
}
double reverse(double in){//get the reverse of an doubleeger
	std::string tempnum = std::to_string(in);
	std::string reverse = "";
	std::size_t thing = tempnum.find('.');
	for (int i = thing-1; i >= 0; i--){
		reverse += tempnum[i];
		tempnum.erase(tempnum.begin()+thing);
	}
	
	return std::stod(reverse);
}
bool lychrel(double in){//to see if the sum of an unsigned integer and it's reverse is palindromic
	for (int i = 0; i < 50; i++){
		double sumOfOandR = in + reverse(in);
		std::string answer= std::to_string(sumOfOandR);// JESUS CHRIST!
		std::size_t pos = answer.find('.');//no thanks
		std::string intAnswer = answer.substr(0, pos);//how does this even work?
		if (palindrome(intAnswer)){
			return false;
		}
		in = sumOfOandR;
	}
	return true;
}
bool palindrome(std::string in){//to see if is the same front and back
	for (int i = 0; i < in.length() / 2; i++){
		if (in[i] != in[in.length() - i - 1]){
			return false;
		}
	}
	return true;
}