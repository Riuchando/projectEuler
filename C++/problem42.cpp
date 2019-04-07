//Author: Stephen Kinser
//Problem 42

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <math.h> /* sqrt */

int main()
{
  std::vector<int> triangle;
  std::vector<int>::iterator myit;
  for (int i = 1; i < 100; i++)
  {
    triangle.push_back((i * (i - 1) / 2));
  }
  std::fstream myin("p042_words.txt");
  std::string temp;
  int total = 0;
  while (true)
  {
    myin >> temp;
    int value = 0;
    for (char i : temp)
    {
      value += (int)i - 'A' + 1;
    }
    myit = find(triangle.begin(), triangle.end(), value);
    if (myit != triangle.end())
    {
      total++;
    }
    if (myin.eof())
    {
      break;
    }
  }
  myin.close();
  return 0;
}