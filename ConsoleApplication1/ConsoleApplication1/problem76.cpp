//Stephen Kinser
//Problem 76
/*
4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1
*/
#include<iostream>
#include<vector>


int table[150][150];

int partition(int sum, int largestNumber){
	int i, j;

	for (i = 1; i <= sum; i++){
		for (j = 1; j <= largestNumber; j++){
			if (i - j<0){
				table[i][j] = table[i][j - 1];
				continue;
			}
			table[i][j] = table[i][j - 1] + table[i - j][j];
		}
	}

	return table[sum][largestNumber];
}

int main(){
	int sum = 100;
	int largestNumber = 99;
	int i;

	/*initialize table with base cases*/
	for (i = 0; i <= sum; i++)
		table[i][0] = 0;
	for (i = 1; i <= largestNumber; i++)
		table[0][i] = 1;
	
	
	int answer= partition(sum, largestNumber);

	std::cout <<answer<< '\n';
	return 0;
}
