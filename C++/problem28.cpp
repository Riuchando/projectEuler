//Author: Stephen Kinser
//Problem 28

#include <iostream>

int main()
{
  int previous = 1;
  int spiral = 1;
  int sum = 1;

  while ((spiral * 2) < 1001)
  {
    for (int i = 0; i < 4; i++)
    {
      previous = previous + 2 * spiral;
      sum += previous;
    }
    spiral++;
  }
  std::cout << sum << '\n';
  return 0;
}