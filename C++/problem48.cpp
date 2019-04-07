//Author: Stephen Kinser
//problem 48

#include <iostream>
#include <math.h> /* sqrt */

int main()
{
  long long value = 0;
  long long modVal = 10000000000;
  for (int i = 1; i <= 1000; i++)
  {
    long long temp = i;

    for (int j = 2; j <= i; j++)
    {
      temp = temp * i % modVal;
    }
    value = (value + temp) % modVal;
  }
  std::cout << value;
  return 0;
}