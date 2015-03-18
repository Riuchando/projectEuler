//Author: stephen Kinser
/*
By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:


Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.


*/
#include<iostream>
unsigned long long modifiedFactorial(unsigned long long one, unsigned long long two);
int main(){
	unsigned long long rectangle=0;
	for (int i = 3; i < 10000; i++){
		for (int j = 2; j < 10000; j++){
			for (int k = 1; k <= j; k++){
				for (int l = 1; l <= i; l++){
					rectangle +=ceil(j/k)* modifiedFactorial(i, l);
				}
			}

		}
	}




	return 0;
}
unsigned long long modifiedFactorial(unsigned long long one, unsigned long long two){
	unsigned long long three = one - two;
	/*
	consider 23! which is 23*22*21*20.....
	23!/23!= 1
	23!/22!= 23 : you would subtract all the factorials, since they overlap
	23!/21= 23*22
	23!/20!= 23*22*21
	... and so on
	given 23!/n!(23-n)!:
	
	consider 23!/10!(23-10)!
	from 23 to 10
	factorial =(23 /10)*(22/9)*(21/8)*(20/7)*(19/6)*(18/5)....
	
	*/
	double fact = 1;
	bool flag = false;
	while (true){			//could make while true and add a break statement later
		fact *= (double)one / two;
		one--;
		two--;
		if (one == three){
			break;
		}
	}
	return (unsigned long long)fact;
}