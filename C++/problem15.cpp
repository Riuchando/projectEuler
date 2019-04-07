//Author:Stephen Kinser
//Problem 15
#include <iostream>
double latticepaths(int one);
int main()
{
  double answer = latticepaths(20);

  std::cout << answer << '\n';
  return 0;
}
double latticepaths(int one)
{
  double *myArray = new double[one + 1];
  for (int i = 0; i < one + 1; i++)
  {
    myArray[i] = 1;
  }
  for (int j = 1; j < one + 1; j++)
  {
    myArray[j] *= 2;
    for (int k = j + 1; k < one + 1; k++)
    {
      myArray[k] += myArray[k - 1];
    }
  }
  double answer = myArray[one];
  return answer;
}