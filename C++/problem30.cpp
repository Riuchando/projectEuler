//Stephen Kinser
//Problem 30
/*
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

*/
#include <iostream>
#include <string>
#include <math.h> /* sqrt */
bool digitFifth(int input);
int main()
{
  //conjecture: let the upper bound be 9^n+1, when n is the power being looked at;
  int answer = 0;
  int upperbound = pow(9, 6);
  for (int in = 2; in < upperbound; in++)
  {
    if (digitFifth(in))
    {
      answer += in;
    }
  }

  std::cout << answer << '\n';
  return 0;
}
bool digitFifth(int input)
{
  std::string temp = std::to_string(input);
  int sum = 0;
  for (int i = 0; i < temp.length(); i++)
  {
    sum += pow((int)temp[i] - '0', 5);
  }
  return sum == input ? true : false;
}