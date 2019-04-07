//Author: Stephen Kinser
// Problem 142
/*
unsolved
*/
#include <iostream>
#include <math.h> /* sqrt */
int main()
{
  int answer = 0;
  int upperbound = 1000;
  for (int i = 2; i < upperbound; i++)
  {
    long long z = pow(i, 2);
    for (int j = i + 1; j < upperbound; j++)
    {
      long long y = pow(j, 2);
      if ((double)sqrt(y - z) == (int)sqrt(y - z) && (double)sqrt(z + y) == (int)sqrt(z + y))
      {
        for (int k = j + 1; k < upperbound; k++)
        {
          long long x = pow(k, 2);
          if ((double)sqrt(x - z) == (int)sqrt(x - z) && (double)sqrt(x + z) == (int)sqrt(x + z) && (double)sqrt(x + y) == (int)sqrt(x + y) && (double)sqrt(x - y) == (int)sqrt(x - y))
          {
            answer = x + y + z;
          }
        }
      }
    }
  }

  std::cout << answer << '\n';
  return 0;
}