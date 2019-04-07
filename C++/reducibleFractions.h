//Author: Stephen Kinser
#include <vector>
#include <math.h> /* sqrt */

class rF
{
private:
  std::vector<int> denominator;
  bool prime;
  bool composite;
  int possibleFractions;
  int length;

public:
  rF()
  {
    length = 0;
    int bigNum = 100;
    for (int i = 2; i < bigNum; i++)
    {
      while (bigNum % i == 0)
      {
        denominator.push_back(i);
        bigNum = bigNum / i;
        length++;
      }
    }
    prime = false;
    composite = true;
  }
  rF(int d, bool c)
  {
    length = 0;

    if (c == false)
    {
      int oldD = d;
      for (int i = 2; i < d; i++)
      {
        if (d % i == 0)
        { //normally if()
          denominator.push_back(i);
          length++;
          while (d % i == 0)
          {
            d /= i; //this is normally in while loop
          }
        }
      }
      prime = length == 0 ? true : false;
    }
    else
    {
      for (int i = 2; i <= sqrt(d); i++)
      {
        if (d % i == 0)
        {
          denominator.push_back(i);
          int other = d / i;
          if (i != other)
          {
            denominator.push_back(d / i);
            length++;
          }
          length++;
        }
      }
      prime = length == 0 ? true : false;
    }

    composite = c;
  }
  rF(long long d, bool c)
  {
    length = 0;

    if (c == false)
    {
      int oldD = d;
      for (int i = 2; i < d; i++)
      {
        if (d % i == 0)
        { //normally if()
          denominator.push_back(i);
          length++;
          while (d % i == 0)
          {
            d /= i; //this is normally in while loop
          }
        }
      }
      prime = length == 0 ? true : false;
    }
    else
    {
      for (int i = 2; i <= sqrt(d); i++)
      {
        if (d % i == 0)
        {
          denominator.push_back(i);
          int other = d / i;
          if (i != other)
          {
            denominator.push_back(d / i);
            length++;
          }
          length++;
        }
      }
      prime = length == 0 ? true : false;
    }

    composite = c;
  }
  bool reducible(int numerator)
  {
    std::vector<int>::iterator myit = denominator.begin();
    while (myit != denominator.end())
    {
      if (numerator % (*myit) == 0)
      {
        return true;
      }
      myit++;
    }
    return false;
  }
  int getLength()
  {
    return length;
  }
  bool isPrime()
  {
    return prime;
  }
  int getPF()
  {
    return possibleFractions;
  }
  int getD(int i)
  {
    return denominator[i];
  }
  void setPF(int inPF)
  {
    possibleFractions = inPF;
  }
  int sum()
  {
    int answer = 1;
    for (int i = 0; i < length; i++)
    {
      answer += denominator[i];
    }
    return answer;
  }
  bool abundant(int original)
  {
    return original < sum();
  }
};