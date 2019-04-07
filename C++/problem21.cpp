//Author:Stephen Kinser
//Problem 21
/*
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
*/

#include <iostream>
int d(int a);
int main()
{

  int answer = 0; // the sum of all amicable numbers
  for (int a = 1; a < 10000; a++)
  {
    int b = d(a); //the proper divisors of a
    if (d(b) == a && b != a)
    {              // the the inverse is true
      answer += a; //add them together
    }
  }
  std::cout << answer << '\n';
  return 0;
}
int d(int a)
{
  int answer = 1;
  for (int div = 2; div < a; div++)
  {

    if (a % div == 0)
    {                // a proper divisor
      answer += div; //sum of the divisors
    }
  }
  return answer;
}