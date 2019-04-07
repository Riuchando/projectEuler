//Author: Stephen Kinser
//Problem 187

#include <iostream>
#include <fstream>
#include <vector>
//#include"primeNumbers.h"
#include <math.h> /* sqrt */

int main()
{
  //PrimeNumber in(6*pow(10,7));
  std::fstream primeIn("PrimeNumbers.txt");
  double tempPrime;
  unsigned long long maxSize = 0;
  unsigned long long midPoint = 0;
  //std::vector<long long> primeList;
  int *primeList = new int[5000000];
  //std::vector<long long> primeList2;
  unsigned long long answer = 0;
  bool flag = false;
  unsigned long long upperbound = pow(10, 8) / 2;
  int k = 0;
  while (true)
  {

    primeIn >> tempPrime;

    if (tempPrime < upperbound)
    {
      primeList[k] = tempPrime;
      if (tempPrime > 11000 && flag == false)
      {
        flag = true;
        midPoint = k;
      }
      k++;
    }
    else
    {
      break;
    }
  }
  for (int i = 0; i <= midPoint; i++)
  {
    unsigned long long temp = pow(primeList[i], 2);
    //unsigned long long other = primeList[i] * (primeList[k]);
    for (int j = i; temp < pow(10, 8); j++)
    {
      temp = primeList[i] * primeList[j];
      if (temp < pow(10, 8))
      {
        answer++;
      }
    }
  }
  std::cout << answer << '\n';

  return 0;
}
