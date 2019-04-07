//Author: Stephen Kinser
//Problem 35 from project Euler
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <math.h>

bool circular(std::vector<int> &primes, long currValue);
void rotate(int &number, int amount);
int main()
{
  std::vector<int> primeNumber;    //stores all previous primes
  int answer = 0;                  // stores the summation of all primes
  std::vector<int>::iterator myit; // iterator for all primes
  std::fstream primeIn("PrimeNumbers.txt");

  for (myit = primeNumber.begin(); myit != primeNumber.end(); myit++)
  {
    long noOverwrite = (*myit);
    if (circular(primeNumber, noOverwrite))
    { //see how many prime numbers are circular
      // std::cout<<(*myit)<<'\t';
      answer++;
    }
  }
  std::cout << answer << '\n';
  return 0;
}
bool circular(std::vector<int> &myVector, long multiple)
{
  if (multiple < 10)
  { // don't waste time
    return true;
  }
  std::string mulString = std::to_string(multiple);

  char temp; //hopefully this works
  //int rotatedNum;
  std::vector<int>::iterator tempit;

  for (int i = 0; i < mulString.size(); i++)
  {
    if (multiple > 100)
    {
      temp = mulString[0]; //store this, wait until the end to re insert
      for (int j = 0; j < mulString.size() - 1; j++)
      { //rotate all the values
        /*
				example 12345:
				1 gets stored in temp
				after this for loop string : 23455
				instruction after for loop: 23451
				*/

        mulString[j] = mulString[j + 1];
      }
      mulString[mulString.size() - 1] = temp;
      //ss(mulString);//because g++ doesn't support to_string
      std::cout << mulString << '\n';
    }
    else
    {
      temp = mulString[0];
      mulString[0] = mulString[1];
      mulString[1] = temp;
    }
    long rotatedNum = stol(mulString);
    //  std::cout<< rotatedNum<<'\n';//for debugging purposes
    double upperbound = sqrt(rotatedNum); //testing theorem
    for (tempit = myVector.begin(); tempit != myVector.end(); tempit++)
    {

      if (fmod(rotatedNum, (*tempit)) == 0)
      { //is divisible, will leave on next term
        return false;
      }
      if ((*tempit) > upperbound)
      { //short curcuit, only need to check values up to sqrt of curr number
        break;
      }
    }
    mulString = std::to_string(rotatedNum);
  }

  return true;
}
