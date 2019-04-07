//Author: Stephen Kinser
//problem 92

/*
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
*/
#include <iostream>
#include <string>
#include <math.h>

bool chain(long long i);
int main()
{

  int answer = 0;
  for (long long i = 1; i <= 10000000; i++)
  {

    if (chain(i) == true)
    {
      answer++;
    }
  }
  std::cout << answer;
  return 0;
}
bool chain(long long i)
{
  std::string temp = std::to_string(i);
  long long value = 0.0;
  while (value != 1)
  {
    value = 0;
    for (int i = 0; i < temp.length(); i++)
    {
      value += pow((int)(temp[i] - '0'), 2);
    }
    temp = std::to_string(value);
    if (value == 89)
    {
      return true;
    }
  }
  return false;
}