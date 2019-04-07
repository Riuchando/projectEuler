//Author: Stephen Kinser
//Problem 57

#include <iostream>
#include <string>
#include <math.h> /* sqrt */

int main()
{

  long double next = 2;
  long double answer = 0;
  /*
	genereic for all continued fractions
	*/
  for (int i = 1; i <= 1000; i++)
  {
    long double num = 1;
    long double den = 2;
    long double next = 2;
    for (int j = i; j >= 0; j--)
    {
      if (j == 0)
      {
        next = 1;
      }
      if (j != i)
      {
        long double temp = num;
        num = den;
        den = temp;
      }

      num += den * next;
    }
    //std::string num_string = std::to_string(num);
    //std::string den_string = std::to_string(den);
    if ((int)log10(num) > (int)log10(den))
    {
      answer++;
    }
  }
  std::cout << answer << '\n';
  return 0;
}