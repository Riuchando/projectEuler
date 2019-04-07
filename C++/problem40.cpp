//Author: Stephen Kinser
//Problem 40
/*
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 � d10 � d100 � d1000 � d10000 � d100000 � d1000000


*/

#include <iostream>
#include <string>

int main()
{
  std::string Champernowne = "";
  for (long long i = 1; Champernowne.length() <= 1000001; i++)
  {
    Champernowne += std::to_string(i);
  }
  int answer = ((int)Champernowne[0] - '0') * ((int)Champernowne[10 - 1] - '0') * ((int)Champernowne[100 - 1] - '0') * ((int)Champernowne[1000 - 1] - '0') * ((int)Champernowne[10000 - 1] - '0') * ((int)Champernowne[100000 - 1] - '0') * ((int)Champernowne[1000000 - 1] - '0');
  std::cout << answer << '\n';

  return 0;
}