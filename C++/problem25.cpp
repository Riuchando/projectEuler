//Author:Stephen Kinser
//Problem 25
/*
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?
*/

#include <iostream>
#include <string>

class bigNum
{
private:
  int *myNum;
  int digitAmount;
  int capacity;

public:
  void initialize(unsigned int i)
  {
    myNum[0] = i;
    int k = 0;
    for (; myNum[k] % 10 > 10; k++)
    {

      //if the next most signifigant digit is defined, then add the overflow to it, otherwise, initialize it
      myNum[k + 1] = int(myNum[k] / 10);
      myNum[k] = myNum[k] % 10;
    }
    digitAmount = k + 1;
  }
  bigNum()
  {
    myNum = new int[1100];
    capacity = 1100;
    for (int i = 0; i < capacity; i++)
    {
      myNum[i] = -1;
    }
    digitAmount = 1;
  }
  int getSize() const
  {
    return digitAmount;
  }
  void setSize(int in)
  {
    digitAmount = in;
  }
  int sumDigits()
  {
    int answer = 0;
    for (int j = 0; myNum[j] != -1; j++)
    {
      answer += myNum[j];
    }
  }
  std::string toString() const
  {
    std::string temp = "";
    for (int i = digitAmount; i != 0; i--)
    {
      temp = temp + (char)(myNum[i - 1] + '0');
    }
    return temp;
  }
  void print()
  {
    printf("%c", toString());
  }

  bigNum operator+(const bigNum &b)
  {
    //bigNum temp;
    int k;
    for (int i = 0; i < this->getSize(); i++)
    {
      myNum[i] = myNum[i] + b.myNum[i];
      for (k = i; myNum[k] >= 10 || myNum[k + 1] != -1; k++)
      {
        //if the next most signifigant digit is defined, then add the overflow to it, otherwise, initialize it
        if (myNum[k] >= 10)
        {
          myNum[k + 1] = myNum[k + 1] != -1 ? myNum[k + 1] + 1 : 1;
          myNum[k] = myNum[k] % 10;
        }
      }
    }

    digitAmount = k + 1;
    return *this;
  }
  bigNum operator=(const bigNum &rhs)
  {
    int i;
    for (i = 0; i < rhs.digitAmount; i++)
    {
      myNum[i] = rhs.myNum[i];
    }
    digitAmount = i;
    return *this;
  }
};
std::ostream &operator<<(std::ostream &os, const bigNum &obj)
{
  os << obj.toString();
  return os;
}

int main()
{
  /*int fibonacci;
	int num=1;
	int num2=1;

	while(digits != 1000){
	fibonacci = num + num2;
	num = num2;
	num2 = fibonacci;
	}
	*/
  bigNum fibonacci;
  bigNum num;
  bigNum num2;
  int answer = 1;
  num.initialize(1);
  num2.initialize(1);
  int i = 2;
  while (fibonacci.getSize() != 1000)
  {
    fibonacci = num + num2;
    num = num2;
    num2 = fibonacci;
    i++;
    //std::cout << fibonacci << '\n';
  }
  std::cout << fibonacci << i << '\n';
  return 0;
}