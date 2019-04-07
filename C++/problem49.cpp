//Author: Stephen Kinser
//problem 49
#include <iostream>
#include <string>
#include <math.h> /* sqrt */

bool prime(int answer);
bool permutation(int one, int two);
int main()
{
  std::string answer = "";
  for (int i = 1013; i < 3333; i += 2)
  { //primes are always odd, cut work in half
    if (prime(i))
    {
      for (int j = 3000; j < 3332; j++)
      {
        if (prime(i + j) && prime(i + (2 * j)))
        {
          if (permutation(i, i + j) && permutation(i + (2 * j), i + j) && permutation(i + (2 * j), i))
          {
            answer = std::to_string(i) + std::to_string(i + j) + std::to_string(i + (2 * j));
          }
        }
      }
    }
  }
  std::cout << answer << '\n';
  return 0;
}
bool prime(int answer)
{ // this will hopefully never contemplate whether 1 or 2 is prime

  for (int i = 2; i <= sqrt(answer); i++)
  {
    if (answer % i == 0)
    {
      return false;
    }
  }

  return true;
}
bool permutation(int one, int two)
{
  std::string str_one = std::to_string(one);
  std::string str_two = std::to_string(two);
  for (int i = 0; i < str_one.length(); i++)
  { //str_one.length SHOULD == str_two length
    bool flag = false;
    for (int j = 0; j < str_two.length(); j++)
    {
      if (str_one[i] == str_two[j])
      {
        flag = true; //used for short curcuit
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