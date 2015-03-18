//Stephen Kinser
//Problem 9
#include<iostream>
#include"reducibleFractions.h"
int main(){
	int x, y, z;
	int r, s, t;
	int answer;
	/* //Using dickson's method
	for (int i = 2; i < 333; i++){
		r = pow(i, 2)/2;
		rF mine(r, true);
		for (int j = 0; j < mine.getLength() / 2; j++){
			s = mine.getD(j);
			t = mine.getD(mine.getLength() - j-1);
			x = r + s;
			y = r + t;
			z = r + s + t;
			if (x + y + z == 1000){
				answer = x*y*z;
			}
		}
	}*/
	//Eulicid formula:  a = m^2 - n^2 ,\ \, b = 2mn ,\ \, c = m^2 + n^2 
	//thus a + b + c= 1000, can be re written as 2m* (m +n)=1000 or m* (m+n) =500
	for (int i = 2; i < 22; i++){
		for (int j = 2; j < 40; j++){
			if (i*(j + i) == 500){
				//literal
				//answer = ((i*i) - (j*j))*(2 * i*j)*((i*i) + (j*j));
				answer = (2 * i*j)* (pow(i, 4) - pow(j, 4));
			}
		}
	}
	std::cout << answer << '\n';
	return 0;
}