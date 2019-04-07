//Author: Stephen Kinser
//Problem 60
/*****************************

Not solved

*********************************/
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <math.h> /* sqrt */

bool isprime(long long Num);
int main()
{
  std::fstream primeIn("PrimeNumbers.txt");
  double prime = 0;
  std::vector<int> primeNumbers;
  //since 2 is not included, normally I would push back here, but for this problem concatenating 2 to the end of any number would make it even thus not prime
  while (true)
  {
    primeIn >> prime;
    if (prime > 100000)
    {
      break;
    }
    primeNumbers.push_back((int)prime);
  }
  int catPrimes[5];
  catPrimes[0] = 3;
  //making 5 the end of anything makes it divisible by 5
  catPrimes[1] = 7;
  int knownPrimes = 1;
  int actualNum = 1;
  int i;
  while (knownPrimes < 5)
  {
    knownPrimes = 2;
    for (i = actualNum; i < primeNumbers.size(); i++)
    {
      bool flag = false;
      for (int j = 0; j < knownPrimes; j++)
      {
        std::string conCat = std::to_string(catPrimes[j]) + std::to_string(primeNumbers[i]);
        std::string conCat_two = std::to_string(primeNumbers[i]) + std::to_string(catPrimes[j]);
        long long intgerconCat = stoll(conCat);
        long long intgerconCat_two = stoll(conCat_two);
        if (!isprime(intgerconCat) || !isprime(intgerconCat_two))
        {
          flag = true;
          break;
        }
      }
      if (flag == false)
      {
        catPrimes[knownPrimes] = primeNumbers[i];
        if (knownPrimes == 2)
        {
          actualNum = i + 1;
        }
        knownPrimes++;
      }
    }
  }
  int answer = 0;
  for (int i : catPrimes)
  {
    answer += i;
  }
  std::cout << answer << '\n';
  return 0;
}
bool isprime(long long answer)
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