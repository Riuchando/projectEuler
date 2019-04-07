//Author: Stephen Kinser
//Problem 50

#include <iostream>
#include <vector>
#include <math.h> /* sqrt */

bool prime(double answer);
int main()
{

  std::vector<double> primeNumbers;
  std::vector<double>::iterator myit;
  primeNumbers.push_back(2); //to avoid confusion
  int size = 1;              //since it already has 2, used to avoid iterators when unnessary
  for (double i = 3; i <= 100000; i++)
  {
    double upperbound = sqrt(i); //to short curcuit
    bool flag = true;            //to avoid the iterator==pimenumber.end
    for (myit = primeNumbers.begin(); (*myit) <= upperbound; myit++)
    {
      if (fmod(i, (*myit)) == 0.0)
      {
        flag = false; // the current number is NOT a prime
        break;
      }
    }
    if (flag == true)
    {                            // if it got through the entire loop
      primeNumbers.push_back(i); //the number is prime
      size++;
    }
  }
  double sum = 0.0;
  int max = 0;
  int chain = 0;
  double maxSum = 0.0;
  //sum numbers until sum > 1,000,000
  // if the length > the highest length, save it
  //reset start at the second number forward
  for (int k = 0; k < size; k++)
  {
    sum = primeNumbers[k];
    for (int l = k + 1; l < size - 1; l += 2)
    {
      sum += primeNumbers[l]; //ALL primes aside from 2 are odd, so , chains have to be odd, it starts as 1, then adds 2
      sum += primeNumbers[l + 1];
      if (sum > 1000000)
      { //short curcuit
        break;
      }
      if (prime(sum))
      {
        chain = l - k;
        if (chain > max)
        {
          max = chain;
          maxSum = sum;
        }
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