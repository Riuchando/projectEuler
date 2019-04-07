//Author: Stephen Kinser
//Problem 24
/*
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
*/
#include <iostream>
#include <string>
double factorial(int one);

int main()
{
  std::string original = "0123456789";
  std::string previous = original;
  int position = 999999;
  int whichSwaps[9];
  int amountOfSwaps[9];
  for (int i = 8; i >= 0; i--)
  {
    whichSwaps[i] = factorial(i + 1);
  }

  for (int k = 8; k >= 0; k--)
  {
    amountOfSwaps[k] = position / whichSwaps[k];
    position = position % whichSwaps[k];
  }

  std::string empty = "";
  for (int k = 0; k < 9; k++)
  {
    char temp = original[amountOfSwaps[8 - k]];
    original.erase(original.begin() + amountOfSwaps[8 - k]);
    empty += temp;
  }
  empty += original[0];

  return 0;
}
double factorial(int one)
{
  double answer = 1.0;
  for (int i = one; i >= 2; i--)
  {
    answer *= i;
  }
  return answer;
}
