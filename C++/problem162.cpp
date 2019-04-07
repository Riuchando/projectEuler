//Author: Stephen Kinser
//problem 162

#include <iostream>
#include <iomanip>
#include <sstream>

int main()
{
  double fact16 = 1;
  int j = 3;
  for (int i = 16; i > 13; i--)
  {
    fact16 *= j > 1 ? (double)i / j : i;
    j--;
  }
  std::stringstream answer;
  answer << std::hex << (long long)fact16;
  std::string result(answer.str());
  std::cout << result << '\n';
  return 0;
}