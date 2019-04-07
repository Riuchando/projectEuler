//Author: Stephen Kinser
//problem 107

#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

int weight(int matrix[][40]);
bool find(int vector[], int length, int num);
int main()
{
  int size = 40;
  std::fstream matrixin("p107_network.txt");
  int matrix[40][40];
  int temp;
  for (int i = 0; i < size; i++)
  {
    for (int j = 0; j < size; j++)
    {
      matrixin >> matrix[i][j];
    }
  }
  int max = weight(matrix);
  int currentMax = 0;

  for (int startNode = 0; startNode < size; startNode++)
  {
    int pathLengths[40]{};
    int positions[40]{};
    int visitedNodes[40]{};
    for (int k = 0; k < size; k++)
    {
      pathLengths[k] = matrix[startNode][k];
      positions[k] = startNode;
    }

    visitedNodes[0] = startNode;
    int length = 1;
    for (int l = 0; l < size; l++)
    {
      //find min value
      int min = 9999;
      int pos = 0;
      for (int i = 0; i < size; i++)
      {
        if (pathLengths[i] < min && !find(visitedNodes, length, i))
        {
          min = pathLengths[i];
          pos = i;
        }
      }
      visitedNodes[length] = pos;
      length++;
      for (int i = 0; i < size; i++)
      {
        if (matrix[pos][i] < pathLengths[i] && !find(visitedNodes, length, i))
        {
          pathLengths[i] = matrix[pos][i];
          positions[i] = pos;
        }
      }
    }
    int tempWeight = 0;
    for (int stuff : pathLengths)
    {
      tempWeight += stuff;
    }
    tempWeight -= 99999;
    if (max - tempWeight > currentMax)
    {
      currentMax = max - tempWeight;
    }
  }
  std::cout << currentMax << '\n';
  return 0;
}
int weight(int matrix[][40])
{
  int max = 0;
  for (int i = 0; i < 40; i++)
  {
    for (int j = i; j >= 0; j--)
    {
      max += matrix[i][j] == 99999 ? 0 : matrix[i][j];
    }
  }
  return max;
}
bool find(int vector[], int length, int num)
{
  for (int i = 0; i < length; i++)
  {
    if (vector[i] == num)
    {
      return true;
    }
  }
  return false;
}
