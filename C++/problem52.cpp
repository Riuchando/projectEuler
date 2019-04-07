//Author: Stephen Kinser
//problem 52
/*
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive doubleeger, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
*/
#include <iostream>
#include <string>
#include <math.h> /* sqrt */

bool permutation(double one, double two);

int main()
{

  double answer = 0;
  for (double i = 61824; i < 40000000; i++)
  {
    if (permutation(i * 2, i) && permutation(i * 3, i * 2) && permutation(i * 4, i * 3) && permutation(i * 5, i * 4))
    {
      answer = i;
      break;
    }
  }

  std::cout << answer << '\n';

  return 0;
}
bool permutation(double one, double two)
{
  std::string str_one = std::to_string(one);
  std::string str_two = std::to_string(two);
  for (int i = 0; str_one[i] != '.'; i++)
  { //str_one.length SHOULD == str_two length
    bool flag = false;
    for (int j = 0; str_two[j] != '.'; j++)
    {
      if (str_one[i] == str_two[j])
      {
        flag = true; //used for short curcuit
        str_two.erase(str_two.begin() + j);
        break;
      }
    }
    if (flag == false)
    { //short curcuit
      return false;
    }
  }

  /////////////////////////////////////////////////////////
  return true;
}