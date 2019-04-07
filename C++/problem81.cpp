//Author: Stephen Kinser
//Problem 81

#include <iostream>
#include <fstream>

int main()
{
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
  //int row = 0;
  //int col = 0;
  int sum[80] = {};
  sum[0] = matrix[0][0];
  for (int i = 1; i < 80; i++)
  {
    int row = 0;
    for (int col = i; col >= 0; col--)
    {
      if (col == i)
      {
        sum[col] = sum[col - 1] + matrix[0][col];
      }
      else if (col == 0)
      {
        sum[0] += matrix[i][0];
      }
      else
      {
        sum[col] = sum[col] < sum[col - 1] ? matrix[row][col] + sum[col] : sum[col - 1] + matrix[row][col];
      }
      row++;
    }
  }
  //half way there!!!!
  int j = 1;
  for (int i = 79; i > 0; i--)
  {
    int col = j;
    int row = 79;
    for (int l = 0; l < i; l++)
    {

      sum[l] = sum[l] < sum[l + 1] ? matrix[row][col] + sum[l] : sum[l + 1] + matrix[row][col];
      row--;
      col++;
    }
    j++;
  }
  int answer = sum[0];

  std::cout << answer << '\n';
  return 0;
}