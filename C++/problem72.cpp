//Author: Stephen Kinser
//Problem 72

#include <iostream>
#include "reducibleFractions.h"
#include <vector>

int calculate(rF reduced, int original, std::vector<int> &mine);
int main()
{
  double answer = 0.0;

  std::vector<int> myRF;
  for (int d = 2; d <= 1000000; d++)
  {
    rF reduced(d, true);
    int c = calculate(reduced, d, myRF);
    answer = answer + c;
  }
  std::cout << answer << '\n';

  return 0;
}
/*
consider 11: it has 10 combinations 1/11, 2/11. 3/11, 4/11, etc 
now consider 12: it has 11 combinations 1/12, 2/12, 3/12, 4/12, etc
however 2/12, 3/12, and 4/12 can be reduced so don't count.
part of RF's job is to keep track of ALL divisors of a given number
12 has 4 unique divisors: 11 to begin with, 1 that overlaps with x/2, 2 that overlap with x/3, 2 that overlap with x/4, 2 for x/6
so a number that is composite, ie that is not prime, has (num-1)- all the overlaps from the divisor
*/
int calculate(rF reduced, int original, std::vector<int> &myVector)
{
  int answer = original - 1;
  if (reduced.isPrime())
  {
    myVector.push_back(answer);
    return answer;
  }
  else
  {
    int i = 0;
    while (i < reduced.getLength())
    {
      answer -= myVector.at(reduced.getD(i) - 2);
      i++;
    }
    myVector.push_back(answer);
    return answer;
  }
}