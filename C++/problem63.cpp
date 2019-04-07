//Author: Stephen Kinser
//Problem 63
/*
The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?

*/

#include <iostream>
#include <string>
#include <math.h> /* sqrt */

int main()
{
  int answer = 0;
  for (int i = 0; i < 10; i++)
  {
    for (int j = 1; j < 50; j++)
    {
      long long temp = pow(i, j);
      std::string temp_string = std::to_string(temp);
      if (temp_string.length() == j)
      {
        answer++;
      }
    }
  }

  std::cout << answer << '\n';
  return 0;
}