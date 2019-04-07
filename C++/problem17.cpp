//Author: Stephen Kinser
//Problem 17

#include <iostream>

int main()
{
  // empty, one, two, three, four, five, six, seven, eight, nine
  int single[10] = {0, 3, 3, 5, 4, 4, 3, 5, 5, 4};
  // ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen
  int teen[10] = {3, 6, 6, 8, 8, 7, 7, 9, 8, 8};
  //twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety
  int doubledigit[8] = {6, 6, 5, 5, 5, 7, 6, 6};

  double wordTotal = 0.0;
  for (int i = 1; i <= 1000; i++)
  {
    if (i / 1000 >= 1 && i / 1000 <= 9)
    {
      int thousands = i / 1000;
      //eg 600= SIX THOUSAND= 11 letters
      wordTotal = wordTotal + single[thousands] + 8;
    }
    if (i / 100 >= 1 && i / 100 <= 9)
    { //done this way for readability
      int hundreds = i / 100;
      //eg 600= SIX HUNDRED= 10 letters
      wordTotal = wordTotal + single[hundreds] + 7;
      if (i % 100 > 0)
      {
        //eg 601= six hundred AND one
        wordTotal += 3;
      }
    }
    if ((i % 100) / 10 == 1)
    { //teens  eg 115 = one hundred and FIFTEEN
      wordTotal += teen[i % 10];
    }
    else if ((i % 100) / 10 > 1)
    { // double digit numbers eg 125= one hundred and TWENTY FIVE
      wordTotal += doubledigit[((i % 100) / 10) - 2];
      wordTotal += single[i % 10];
    }
    else
    { //(i%100) /10 ==0 eg 101 = one hundred and ONE
      wordTotal += single[i % 10];
    }
  }
  std::cout << wordTotal << '\n';
  return 0;
}