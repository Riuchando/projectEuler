//Author: Stephen Kinser
//Some source code ripped from :http://stackoverflow.com/questions/22746429/c-decimal-to-binary-converting
//I didn't know how bit set worked....

//Problem  36
#include <iostream>
#include <string>
#include <bitset>
#include <limits>
bool palindrome(std::string in);
int main()
{
	
	int answer = 0;
	for (unsigned long long x = 5; x < 1000000; x++){
		if (palindrome(std::to_string(x))){
			std::string s =
				std::bitset<std::numeric_limits<unsigned long long>::digits>(x).to_string();
			std::string::size_type n = s.find('1');
			if (palindrome(s.substr(n))){
				answer += x;
				
			}
		}
	}
		
		std::cout <<answer << std::endl;
		return 0;
}
bool palindrome(std::string in){
	for (int i = 0; i < in.length()/2; i++){
		if (in[i] != in[in.length() - i - 1]){
			return false;
		}
	}
	return true;
}