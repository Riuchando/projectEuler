//Author: Stephen Kinser
//Problem 56

#include <iostream>
#include <string>
#include <vector>
#include <math.h> /* sqrt */

int sumDigits(std::string in);
int main()
{
  std::vector<int> sums;
  for (int i = 9; i <= 9; i++)
  {
    for (int j = 40; j <= 100; j++)
    {
      sums.push_back(sumDigits(std::to_string(pow(i, j))));
    }
    //std::cout << '\n';
  }

  return 0;
}
int sumDigits(std::string in)
{
  int answer = 0;
  for (int i = 0; in[i] != '.'; i++)
  {
    answer += (int)in[i] - '0';
  }

  return answer;
}