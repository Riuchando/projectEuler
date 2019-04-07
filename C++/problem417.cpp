//Author: Stephen Kinser
//Problem 417

#include <iostream>
#include <vector>
#include <math.h> /* sqrt */

struct pair
{
  int div;
  int rem;
  bool operator==(pair rhs)
  {
    return (div == rhs.div) && (rem == rhs.rem);
  }
};

int find(std::vector<pair> trex, pair value);
int main()
{
  unsigned long long answer = 0;
  unsigned long long maxCycle = 0;
  for (unsigned long long i = 2; i < 1000000; i++)
  {
    std::vector<pair> velociraptor;
    unsigned long long cycleLength = 0;
    pair temp;
    temp.div = i;
    temp.rem = i;
    unsigned long long end = 0;
    unsigned long long initial = pow(10, ceil(log10(i)));
    temp.div = initial / i;
    temp.rem = initial - temp.div * i;
    velociraptor.push_back(temp);
    end++;
    while (temp.rem != 0)
    {

      temp.div = (10 * temp.rem) / i;
      temp.rem = (10 * temp.rem) - temp.div * i;

      int start = find(velociraptor, temp);
      if (start == end)
      {
        velociraptor.push_back(temp);
        end++;
      }
      else
      {
        cycleLength = end - start;
        break;
      }
    }
    if (cycleLength != 0)
    {
      answer += cycleLength;
    }
  }
  std::cout << answer << '\n';
  return 0;
}
int find(std::vector<pair> trex, pair value)
{
  int pos = 0;
  while (pos != trex.size())
  {
    if (trex[pos] == value)
    {
      return pos;
    }
    pos++;
  }
  return pos;
}