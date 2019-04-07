//Author: Stephen Kinser
//Problem 66
/*
code from 64
*/
#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h> /* sqrt */

struct pair
{
  int c;
  int q;
  int d;
  int a;
  bool operator==(pair rhs)
  {
    return (c == rhs.c) && (q == rhs.q) && (d == rhs.d) && (a == rhs.a);
  }
};
int main()
{
  int answer = 0;
  int maxlength = 0;
  for (int i = 2; i <= 1000; i++)
  {
    if (sqrt(i) != trunc(sqrt(i)))
    {
      int approx = sqrt(i);
      int curr = 0;
      std::vector<pair> myvector;
      std::vector<pair>::iterator cIt;
      int den, b;
      int num = 1;
      /*
			given a/(sqrt(currentNum)-b)
			let approx= sqrt(currentNum)
			start for
			let denominator= (currentNum - pow(approx, 2))/ numerator
			let nextapprox= (sqrt(currentNum)+ approx)/den // this line of code took forever for me to figure out and then afterwards I felt dumb
			let numerator -= denominator*b
			search for c and q
			if not found period ++
			let approx = numerator
			make the numerator the denominator(pretend flip)
			end for
			*/
      while (true)
      {
        den = (i - pow(approx, 2)) / abs(num);

        b = (sqrt(i) + approx) / den;
        num = approx;
        num -= den * b;
        pair improper;
        improper.c = b;
        improper.q = -1 * num;
        improper.d = den;
        improper.a = approx;
        cIt = find(myvector.begin(), myvector.end(), improper);
        if (cIt != myvector.end())
        {
          break;
        }
        else
        {
          myvector.push_back(improper);
          curr++;
          approx = abs(num);
          num = den;
        }
      }
      if (curr > maxlength)
      {
        maxlength = curr;
        answer = i;
      }
    }
  }

  std::cout << answer << '\n';

  return 0;
}