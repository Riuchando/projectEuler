//Author: Stephen Kinser
//Problem 74

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
int digitFactorial(int in);
int main()
{

  std::vector<int>::iterator myit;
  std::string digits;
  int link;
  int total = 0;
  for (int i = 1; i <= 1000000; i++)
  {
    std::vector<int> temp;

    int length = 1;
    digits = std::to_string(i);
    while (true)
    {
      link = 0;

      for (int j = 0; j < digits.length(); j++)
      {
        link += digitFactorial(((int)digits[j] - '0'));
      }
      myit = find(temp.begin(), temp.end(), link);
      if (myit == temp.end())
      {
        temp.push_back(link);
        length++;
        digits = std::to_string(link);
      }
      else
        break;
    }
    if (length == 60)
    {
      total++;
    }
  }

  std::cout << total;

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