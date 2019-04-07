//Author:Stephen Kinser
//Problem 19
//
#include <iostream>

int main()
{
  //ja, fe, ma, ap, my, ju, jl, au, sp, oc, no, dc
  int regularYear[12]{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
  int leapYear[12]{31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
  int currCount = 2;   // 1 Jan 1901 was a tuesday.
  int sundayCount = 0; //initialization
  for (int year = 1901; year < 2001; year++)
  {
    for (int month = 0; month < 12; month++)
    {
      if (currCount % 7 == 0)
      {                //if it lands on the first of the week, it is a sunday
        currCount = 0; //reset to prevent overflow
        sundayCount++;
      }
      // the following line of code is: if it is a leap year, add the amount of days from a leap year, otherwise use regular year
      currCount += year % 4 == 0 ? leapYear[month] : regularYear[month]; // proving I know c++
                                                                         // not needed in this problem, but SHOULD WORK in extreme cases
                                                                         // currCount += year % 4 == 0 && (year%100!=0  || year%400==0) ? leapYear[month] : regularYear[month];// proving I know c++
    }
  }
  std::cout << sundayCount << '\n';
  return 0;
}