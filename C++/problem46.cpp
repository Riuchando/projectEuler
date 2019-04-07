//Author: Stephen Kinser
//Problem 46

#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <math.h>

bool prime(double answer);
int main()
{
  std::ifstream myin("PrimeNumbers.txt");

  std::vector<double> primeNumbers;
  double temp;
  int max = 2000000;
  int size = 0;
  while (true)
  {
    myin >> temp;
    if (temp > max)
    {
      break;
    }
    primeNumbers.push_back(temp);
    size++;
  }
  myin.close();
  for (double i = 9; i < max; i += 2)
  {
    if (!prime(i))
    {
      bool flag = true;
      for (int k = 0; k < size; k++)
      {
        double tempt = sqrt((i - primeNumbers[k]) / 2);
        if (tempt == trunc(tempt))
        {
          flag = false;
          break;
        }
      }
      if (flag == true)
      {
        std::cout << i << '\n';
        break;
      }
    }
  }
  return 0;
}
bool prime(double answer)
{ // this will hopefully never contemplate whether 1 or 2 is prime

  for (int i = 2; i <= sqrt(answer); i++)
  {
    if (fmod(answer, i) == 0)
    {
      return false;
    }
  }

  return true;
}