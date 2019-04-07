//Author: Stephen Kinser
//Problem 82

#include <iostream>
#include <fstream>

int main()
{
  // read it in
  std::fstream matrixin("p081_matrix.txt");
  int matrix[80][80];
  int temp;
  for (int i = 0; i < 80; i++)
  {
    for (int j = 0; j < 80; j++)
    {
      matrixin >> matrix[i][j];
    }
  }
  int sum[80]{};

  for (int i = 0; i < 80; i++)
  {
    sum[i] = matrix[i][0] + matrix[i][1];
    int col = 0;
    for (int j = i; j < 80; j++)
    {
      if (j == 0)
      {
        sum[0] += matrix[0][col];
      }
      if (j == 79)
      {
      }
    }
  }
  return 0;
}