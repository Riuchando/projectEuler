//Author: Stephen Kinser
// problem 89

#include <iostream>
#include <fstream>
#include <string>

struct romanNumeral
{
  std::string originalInput;
  int decimalValue[4]{};
};
int main()
{
  romanNumeral list[1000];
  std::fstream myin("p089_roman.txt");
  int i = 0;
  int answer = 0;
  while (true)
  {
    myin >> list[i].originalInput;
    if (myin.eof())
      break;
    i++;
  }
  for (int j = 0; j < 1000; j++)
  {
    //list[j].decimalValue[0] = 0;
    int reduced = 0;
    //std::string minimal = "";
    int letter = 0;
    for (int k = 0; k < list[j].originalInput.length(); k++)
    {
      bool rFlag = false;
      if (list[j].originalInput[k] == 'M')
      {
        list[j].decimalValue[letter] += 1;
        rFlag = true;
      }
      else if (list[j].originalInput[k] == 'D')
      {
        letter = 1;
        list[j].decimalValue[letter] += 5;
      }
      else if (list[j].originalInput[k] == 'C')
      {
        letter = 1;
        if (list[j].originalInput[k + 1] == 'M')
        {
          list[j].decimalValue[letter] += 9;
          k++;
          rFlag = true;
        }
        else if (list[j].originalInput[k + 1] == 'D')
        {
          list[j].decimalValue[letter] += 4;
          k++;
          rFlag = true;
        }
        else
        {
          list[j].decimalValue[letter] += 1;
        }
      }
      else if (list[j].originalInput[k] == 'L')
      {
        letter = 2;
        list[j].decimalValue[letter] += 5;
      }
      else if (list[j].originalInput[k] == 'X')
      {
        letter = 2;
        if (list[j].originalInput[k + 1] == 'L')
        {
          list[j].decimalValue[letter] += 4;
          k++;
          rFlag = true;
        }
        else if (list[j].originalInput[k + 1] == 'C')
        {
          list[j].decimalValue[letter] += 9;
          k++;
          rFlag = true;
        }
        else
        {
          list[j].decimalValue[letter] += 1;
        }
      }
      else if (list[j].originalInput[k] == 'V')
      {
        letter = 3;
        list[j].decimalValue[letter] += 5;
      }
      else if (list[j].originalInput[k] == 'I')
      {
        letter = 3;
        if (list[j].originalInput[k + 1] == 'V')
        {
          list[j].decimalValue[letter] += 4;
          k++;
          rFlag = true;
        }
        else if (list[j].originalInput[k + 1] == 'X')
        {
          list[j].decimalValue[letter] += 9;
          k++;
          rFlag = true;
        }
        else
        {
          list[j].decimalValue[letter] += 1;
        }
      }
      if (rFlag == false)
      {
        if (list[j].decimalValue[letter] == 4)
        {
          //IIII->IV
          reduced += 2;
        }
        else if (list[j].decimalValue[letter] == 9)
        {
          //VIIII-> IX
          reduced += 3;
        }
      }
    }
    answer += reduced;
  }
  std::cout << answer << '\n';
  return 0;
}