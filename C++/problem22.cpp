//Author: Stephen Kinser
//Problem 22

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
int main()
{
  std::fstream myfs;
  myfs.open("p022_names.txt");
  std::string temp;
  std::vector<std::string> namelist;
  //std::vector<std::string>::iterator myitr;
  int size = 0;
  int answer = 0;
  while (true)
  {
    myfs >> temp;
    namelist.push_back(temp);
    size++;
    if (myfs.eof())
    {
      break;
    }
  }
  std::sort(namelist.begin(), namelist.end());
  for (int i = 0; i < size; i++)
  {
    int wordVal = 0;
    for (int k = 0; k < namelist[i].length(); k++)
    {
      wordVal += (int)namelist[i][k] - 'A' + 1;
    }
    answer += (i + 1) * wordVal;
  }

  std::cout << answer << '\'n';
  return 0;
}