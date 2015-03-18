//Stephen Kinser
//Problem 78
/*
Not Solved
*/
#include<iostream>
#include<vector>


std::vector<std::vector<long long>> table;

long long partition(int sum, int largestNumber){
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
	int sum = 5;
	int largestNumber = sum-1;
	int i;
	int answer = 0;
	/*initialize table with base cases*/
	std::vector<long long> temp;
	for (i = 0; i <= sum; i++){
		//table[i][0] = 0;
		temp.push_back(0);
	}
		

	while (true)
	{
		for (i = 1; i <= largestNumber; i++){
			table[0][i] = 1;
		}
		long long temp = partition(sum, largestNumber)+1;
		if (temp % 1000000==0){
			answer = temp;
			break;
		}
		else{
			sum++;
			largestNumber = sum - 1;
		}

	}
	


	

	std::cout << answer << '\n';
	return 0;
}
