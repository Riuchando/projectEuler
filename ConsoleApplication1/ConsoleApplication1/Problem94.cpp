//Author: Stephen Kinser
//problem 94
/*
It is easily proved that no equilateral triangle exists with integral length sides and integral area. However, the almost equilateral triangle 5-5-6 has an area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose perimeters do not exceed one billion (1,000,000,000).
*/
#include<iostream>
#include<string>
int main(){
	//reimagine the nearly equalateral triangle as a rectangle, with its diagonal
	//cut triangle in half so that the outside edges would be 1/2(n+1) and sqrt(n^2-(1/2(n+1)))
	//if it is an integer then sum +1/2(n+1)
	unsigned long long answer = 0;
	double upperbound = 14;
	double otherbound = 14;
	for (double i = 5; upperbound < pow(10, 9); i++){
		double var = sqrt((pow(i, 2)) - pow((.5 *(i + 1)),2));
		double var2 = sqrt((pow(i, 2)) - pow((.5 *(i - 1)), 2));
		upperbound = (2 * i) + (i + 1);
		otherbound = (2 * i) + (i - 1);
		double area1 = var/2* (i + 1);
		double area2 = var2/2* (i - 1);
		if ( area1 == trunc(area1)){
			
			answer += upperbound;
		}
		if (area2 == trunc(area2)){

			answer += otherbound;
		}
	}
	std::string realAnswer = std::to_string(answer);
	std::cout << realAnswer << '\n';

	return 0;
}