//Author: Stephen Kinser
//Problem 70
/*******************************
Not sovled



*******************************/

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <math.h> /* sqrt */

bool permutation(int one, int two);
int gcd(int one, int two);
int main()
{
  /*std::ofstream primeOut("PrimeNumbers.txt");
	std::vector<double> primeNumbers;
	std::vector<double>::iterator myit;
	primeNumbers.push_back(2);//to avoid confusion
	primeOut << 2.0<<'\t';
	int size = 1;//since it already has 2, used to avoid iterators when unnessary
	for (double i = 3; i <= pow(10,7)+1; i++){
		double upperbound = sqrt(i);//to short curcuit
		bool flag = true;//to avoid the iterator==pimenumber.end
		for (myit = primeNumbers.begin(); (*myit) <= upperbound; myit++){
			if (fmod(i, (*myit)) == 0.0){
				flag = false;// the current number is NOT a prime
				break;
			}
		}
		if (flag == true){// if it got through the entire loop
			primeNumbers.push_back(i);//the number is prime
			primeOut<<std::to_string(i)<<'\t';
			size++;
		}
	}*/
  std::fstream primeIn("PrimeNumbers.txt");
  double prime;
  double upperbound = pow(10, 7);
  std::vector<double> primeList;
  while (true)
  {
    primeIn >> prime;
    if (prime > upperbound || primeIn.eof())
    {
      break;
    }
    if (prime > 9300000)
    {
      primeList.push_back(prime);
    }
  }
  int totient = 1;
  int answer = 0;
  for (int l = primeList.size() - 1; l > 0; l--)
  {
    for (int j = primeList[l] - 1; j >= 2; j--)
    {
      if (gcd((int)primeList[l], j) == 1)
      {
        totient++;
      }
    }
    if (permutation((int)primeList[l], totient))
    {
      answer = primeList[l];
      std::cout << answer << '\n';
    }
  }
  return 0;
}
bool permutation(int one, int two)
{
  std::string str_one = std::to_string(one);
  std::string str_two = std::to_string(two);
  for (int i = 0; i < str_one.length(); i++)
  { //str_one.length SHOULD == str_two length
    bool flag = false;
    for (int j = 0; j < str_two.length(); j++)
    {
      if (str_one[i] == str_two[j])
      {
        flag = true; //used for short curcuit
        break;
      }
    }
    if (flag == false)
    { //short curcuit
      return false;
    }
  }

  /////////////////////////////////////////////////////////
  return true;
}
int gcd(int a, int b)
{
  int temp;
  while (a % b != 0)
  {
    temp = b;
    b = a % b;
    a = temp;
  }
  return b;
}