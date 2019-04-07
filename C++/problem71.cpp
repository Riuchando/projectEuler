//Author: Stephen Kinser
//Problem 71
/*
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.

*/
#include "reducibleFractions.h" //not used
#include <iostream>
#include <math.h> /* sqrt */

int main()
{
  const double upperbound = 0.42857142857;
  int answer = 0;
  int num;
  double lowerbound = 0.42;
  for (int d = 700000; d <= 1000000; d++)
  {
    //rF reduced(d, false);//not used
    //if (reduced.isPrime()){//not used, but should be
    num = d * 3 / 7;               //the number to the immidiate left is the cross multiplication of these numbers
    double temp = (double)num / d; // find the number that closely approximates it
    if (temp < upperbound && temp > lowerbound)
    {
      lowerbound = temp;
      answer = num;
    }
    //}
  }
  std::cout << answer << '\n';

  return 0;
}