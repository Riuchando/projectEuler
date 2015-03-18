//Author:Stephen Kinser
//Problem 29
//not finished
#include<iostream>
#include<vector>
#include<algorithm>
int powerOf(int one);
int rootOf(int one);
int main(){
	int answer = 0;
	std::vector<double> lololol;
	std::vector<double>::iterator myitr;
	for (int i = 2; i <= 100; i++){
		for (int j = 2; j <= 100; j++){
			double cool = j*log2(i);
			myitr = find(lololol.begin(), lololol.end(), cool);
			if (myitr == lololol.end()){
				lololol.push_back(cool);
			}
		}
	}

	//int upperbounds = 7;
	//int lowerbounds = 2;
	//int pos = upperbounds - lowerbounds + 1;
	/*std::vector<std::vector<int>> allKnownPowers;
	std::vector<int> currentRow;
	std::vector<int>::iterator myIt;
	for (int i = lowerbounds; i <= upperbounds; i++){
		int movement = powerOf(i);
		if (movement == 1){
			currentRow.push_back(i);
			for (int j = lowerbounds; j <= upperbounds; j++){
				currentRow.push_back(j);
				answer++;
			}
			allKnownPowers.push_back(currentRow);
		}
		else{
			int row = rootOf(i);
			int i;
			for (i = 0; i < allKnownPowers.size(); i++){
				//returns the row
				if (row == allKnownPowers[i][0]){
					break;
				}
			}
			for (int k = lowerbounds; k < upperbounds; k++){
				if (k*movement != allKnownPowers[i][k*movement - 1]){
					allKnownPowers[i].push_back(k*movement);
				}
			}
		}
		
	}*/
	/*
	previous idea for algebraeic solution
	for (int i = lowerbounds; i <= upperbounds; i++){
		
		int overlap = powerOf(i);
		answer +=overlap==1? pos: (pos- pos/overlap);
		if ((pos / overlap)){

		}
	}*/
	answer = lololol.size();
	std::cout << answer<<'\n';


	return 0;
}
int powerOf(int one){
	int answer=1;
	for (int den = 2; den < one; den++){
		int two = one;
		answer = 1;
		while (two%den == 0){
			two /= den;
			answer++;
		}
		if (two == 1){
			return answer-1;
		}
	}
	return answer;

}
int rootOf(int one){
	int den;
	for (den = 2; den < one; den++){
		int two = one;
		
		while (two%den == 0){
			two /= den;

		}
		if (two == 1){
			return den;
		}
	}
	return den;

}