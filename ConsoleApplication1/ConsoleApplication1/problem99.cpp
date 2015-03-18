//Author: Stephen Kinser
//Problem 99

#include<iostream>
#include<fstream>
int main(){
	std::fstream myin("p099_base_exp.txt");
	double base, exp;
	int line = 0;
	double max = 0;
	int i = 0;
	while (true){
		myin >> base >> exp;
		if (myin.eof()){
			break;
		}
		double answer = exp* log10(base);
		i++;
		if (answer > max){
			max = answer;
			line = i;
		}
	}
	std::cout << line << '\n';
	return 0;
}