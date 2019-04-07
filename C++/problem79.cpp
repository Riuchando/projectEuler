//Author: Stephen Kinser
//Problem 79
//Solved by hand
#include <iostream>
#include <fstream>
#include <string>

int main()
{
  std::fstream myin("p079_keylog.txt");
  std::string passwordGuess[50];
  int i = 0;
  while (true)
  {
    myin >> passwordGuess[i];
    if (myin.eof())
      break;
    i++;
  }
  // passwordGuess[0][0]

  return 0;
}