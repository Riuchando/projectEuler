//Author: Stephen Kinser
//Problem 39
/*
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

*/
#include<iostream>
#include<cmath>
#include<math.h>

int main(){
	int answer = 0;
	int max = 0;
	//Eulicid formula:  a = m^2 - n^2 ,\ \, b = 2mn ,\ \, c = m^2 + n^2 
	//thus a + b + c= 1000, can be re written as 2m* (m +n)=1000 or m* (m+n) =500
	for (int h = 5; h <= 1000; h++){
		int numOfSolutions = 0;
		for (int k = 2; k < sqrt(h); k++){
			for (int i = 2; i < sqrt(h); i++){
				for (int j = 2; j < sqrt(h); j++){
					if (k*i*(j + i) == h / 2){
						numOfSolutions++;
					}
				}
			}
			
		}
		if (numOfSolutions > max){
			answer = h;
			max = numOfSolutions;
		}
	}
	std::cout << answer << '\n';
	return 0;
}