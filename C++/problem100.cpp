//Author: Stephen Kinser
//Problem 100, problems with insuffecient precision
/*
If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)�(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 10^12 = 1,000,000,000,000 discs in total, determine the number of blue discs that the box would contain.

*/

#include <iostream>
#include <math.h> /* sqrt */

int main()
{
  //okay, so the general format is (n/x)*(n-1/x-1)=1/2, where x> pow(10,12)
  //the correlation between n and x is n*(n-1)=(x-1)*x/2
  double answer = 0.0;
  for (double begin = pow(10, 12); true; begin++)
  {
    double other = (begin / 2) * (begin - 1);
    double n = other / trunc(sqrt(other));
    if (other == n * (n - 1))
    {
      answer = n;
      break;
    }
  }

  std::cout << answer << '\n';

  return 0;
}