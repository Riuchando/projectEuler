//Author: Stephen Kinser
//for dealing with integers beyond 2^16 with maximum precision

#include <iostream>
#include <string>

class bigNum
{
private:
  int *myNum;      // a large array or integers
  int digitAmount; //the highest order of 10 this integer is
  int capacity;    // defined at the beginning, arrays are the best way (simplest) to deal with it
public:
  void initialize(unsigned int i)
  { //easier than putting it in the constructor
    myNum[0] = i;
    int k = 0;
    while (myNum[k] >= 10 || myNum[k + 1] != -1)
    {

      //if the next most signifigant digit is defined, then add the overflow to it, otherwise, initialize it
      myNum[k + 1] = int(myNum[k] / 10);
      myNum[k] = myNum[k] % 10;
      i /= 10;
      k++;
    }
    digitAmount = k + 1;
  }
  bigNum()
  {                        //default constructor
    myNum = new int[1000]; //dynamic allocate
    capacity = 1000;
    for (int i = 0; i < capacity; i++)
    { //force ALL non used items to be 0
      myNum[i] = -1;
    }
    digitAmount = 1;
  }
  int getSize() const
  { //needed in some problems
    return digitAmount;
  }
  void setSize(int in)
  { // not used
    digitAmount = in;
  }
  int sumDigits()
  { //used in some problems
    int answer = 0;
    //will get each power of 10 and add them together
    //eg 12345= 1+2+3+4+5=15
    for (int j = 0; myNum[j] != -1; j++)
    {
      answer += myNum[j];
    }
    return answer;
  }
  std::string toString() const
  {                        //ah yes Java
    std::string temp = ""; //empty string
    for (int i = digitAmount; i != 0; i--)
    {
      temp = temp + (char)(myNum[i - 1] + '0');
    }
    return temp;
  }
  void print()
  { //incase include iostream is bad
    printf("%c", toString());
  }
  int overFlow(int i)
  {
    int k;
    for (k = i; myNum[k] >= 10 || myNum[k + 1] != -1; k++)
    { // built to handle the overflow
      //if the next most signifigant digit is defined, then add the overflow to it, otherwise, initialize it
      if (myNum[k] >= 10)
      { //if it DOES overflow
        myNum[k + 1] = myNum[k + 1] != -1 ? myNum[k + 1] + 1 : 1;
        myNum[k] = myNum[k] % 10;
      }
    }
    return k;
  }
  void bPow(int inNum)
  {
    bigNum temp_one;
    temp_one = *this;
    for (int i = 2; i <= inNum; i++)
    {
      *this *= temp_one;
    }
    //return *this;
  }
  bigNum &operator++()
  {
    int k;
    myNum[0]++;
    k = this->overFlow(0);
    digitAmount = k + 1;
    return *this;
  }
  bigNum &operator+(const bigNum &b)
  { //adds two big nums together

    int k; //the position of the most signifigant digit
    for (int i = 0; i < this->getSize(); i++)
    {
      myNum[i] = myNum[i] + b.myNum[i]; //bassic integer addition

      k = this->overFlow(i);
    }

    digitAmount = k + 1;
    return *this;
  }

  bigNum &operator=(const bigNum &rhs)
  {
    int i; // the most signifigant digit

    for (i = 0; i < rhs.digitAmount; i++)
    {
      myNum[i] = rhs.myNum[i];
    }
    digitAmount = i;
    return *this;
  }
  /*bigNum& operator*(const int& rhs){
		bigNum temp;
		temp = *this;
		for (int i = 0; i < rhs; i++){
			*this  = *this + temp ;
		}

		return *this;
	}*/
  bigNum &operator*=(const bigNum &rhs)
  {
    bigNum temp_two;
    int k;
    for (int i = 0; i < rhs.digitAmount; i++)
    {
      if (i == 0)
      { //for multiplication of 10^0 , also for initialization
        for (int j = 0; j < /*this->digitAmount */ digitAmount; j++)
        {
          temp_two.myNum[j] = myNum[j] * rhs.myNum[i];
        } //endfor
      }   //endif
      else
      { //all places above 10^0
        for (int j = 0; j < /*this->digitAmount */ digitAmount; j++)
        {
          temp_two.myNum[j + i] += myNum[j] * rhs.myNum[i];
        } //endfor
      }   //endif
      k = temp_two.overFlow(i);
      //temp.print();
    }
    temp_two.digitAmount = k + 1;
    *this = temp_two;
    return *this;
  }
};
std::ostream &operator<<(std::ostream &os, const bigNum &obj)
{
  os << obj.toString();
  return os;
}
bigNum operator*(bigNum lhs, const bigNum &rhs)
{
  return lhs *= rhs;
}
