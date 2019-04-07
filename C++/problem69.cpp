//Author: Stephen Kinser
//Problem 69
/*
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.

n	Relatively Prime	φ(n)	n/φ(n)
2	1					1		2
3	1,2					2		1.5
4	1,3					2		2
5	1,2,3,4				4		1.25
6	1,5					2		3
7	1,2,3,4,5,6			6		1.1666...
8	1,3,5,7				4		2
9	1,2,4,5,7,8			6		1.5
10	1,3,7,9				4		2.5
It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.


*/
#include <iostream>
#include <fstream>
#include <math.h> /* sqrt */

int gcd(int a, int b);
bool prime(int a);
int main()
{
  std::fstream primeIn("PrimeNumbers.txt");
  int upperbound = 1000000;
  double max = 0.0;
  double answer = 2;
  double temp = 0;
  while (true)
  {
    primeIn >> temp;
    if (temp * answer > upperbound)
    {
      break;
    }
    answer *= temp;
  }
  int totient = 1;
  for (int j = answer - 1; j >= 2; j--)
  {
    if (gcd(answer, j) == 1)
    {
      totient++;
    }
  }
  double ndivPhi = (double)answer / totient;
  /**************************************************			   	   				   			   
				   brute force(ineffecient)
******************************************************/
  /*for (int i = 12; i <= upperbound; i++){
			int totient=1;
			if (prime(i)){
				totient = i - 1;
			}
			else{
				for (int j = i - 1; j >= 2; j--){
					if (gcd(i, j) == 1){
						totient++;
					}
				}
			}
		double ndivPhi = (double)i / totient;
		if (ndivPhi > max){
			max = ndivPhi;
			answer = i;
		}

	}*/
  std::cout << answer << '\n';

  return 0;
}
int gcd(int a, int b)
{
  int temp;
  while (a % b != 0)
  {
    temp = b;
    b = a % b;
    a = temp;
  }
  return b;
}
bool prime(int answer)
{ // this will hopefully never contemplate whether 1 or 2 is prime
  if (answer == 2)
  {
    return true;
  }
  for (int i = 2; i <= sqrt(answer); i++)
  {
    if (answer % i == 0)
    {
      return false;
    }
  }

  return true;
}