//Author: Stephen Kinser
//Problem 34

#include <iostream>
#include <string>

int digitFactorial(int in);
int main()
{
  std::string digits;
  int value = 0;
  int answer = 0;
  for (int i = 3; i < 1000000; i++)
  {
    digits = std::to_string(i);
    value = 0;
    for (int j = 0; j < digits.length(); j++)
    {
      value += digitFactorial(((int)digits[j] - '0'));
    }
    if (i == value)
    {
      answer += i;
    }
  }
  std::cout << answer << '\n';

  return 0;
}
int digitFactorial(int in)
{
  switch (in)
  {
  case 0:
    return 1;
    break;
  case 1:
    return 1;
    break;
  case 2:
    return 2;
    break;
  case 3:
    return 6;
    break;
  case 4:
    return 24;
    break;
  case 5:
    return 120;
    break;
  case 6:
    return 720;
    break;
  case 7:
    return 5040;
    break;
  case 8:
    return 40320;
    break;
  case 9:
    return 362880;
    break;
  }
}