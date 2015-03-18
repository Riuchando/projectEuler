//Author: Stephen Kinser
//Problem 185
#include<iostream>
#include<string>
#include<fstream>
#include<vector>
#include<algorithm>
struct pair{
	std::string value;
	int correctvalues;

};
struct correctGuess{
	int value;
	int pos;
	int amount;
	bool operator==(correctGuess rhs){
		return (value == rhs.value) && (pos == rhs.pos);
	}

};
bool compare(correctGuess lhs,correctGuess rhs){
	return lhs.amount > rhs.amount;
}
int main(){
	std::vector<correctGuess> trial;
	std::vector<correctGuess>::iterator myit;
	pair myguesses[22];
	bool wrong[16][10];
	std::fstream myin("problem185.txt");
	if (!myin){
		std::cerr << "bad" << '\n';
		return 0;
	}
	int i = 0;
	pair tempin;
	while (true){
		myin >> tempin.value;
		if (myin.eof()) break;
		myin>> tempin.correctvalues;
		if (myin.eof()) break;
		myguesses[i].correctvalues = tempin.correctvalues;
		myguesses[i].value = tempin.value;
		i++;
	}
	for (int r = 0; r < 16; r++){
		for (int s = 0; s < 10; s++){
			wrong[r][s] = true;
		}
	}
	for (int k = 0; k < i; k++){
		if (myguesses[k].correctvalues == 0){
			k++;
		}
		for (int l = k+1; l < i; l++){
			if (myguesses[l].correctvalues == 0){
				for (int n = 0; n<(myguesses[l].value.length());n++){
					wrong[n][(int)myguesses[l].value[n] - '0'] = false;
				}
			}
			else{
				for (int m = 0; m < myguesses[k].value.length(); m++){
					if (myguesses[k].value[m] == myguesses[l].value[m] && wrong[m][(int)myguesses[l].value[m] - '0'] == true){
						correctGuess temp;
						temp.pos = m;
						temp.value = (int)myguesses[k].value[m] - '0';
						temp.amount = 0;
						myit = find(trial.begin(), trial.end(), temp);
						if (myit == trial.end()){
							temp.amount++;
							trial.push_back(temp);
						}
						else{
							(*myit).amount++;
						}
					}

				}
			}
		}
	}
	std::sort(trial.begin(), trial.end(), compare);
	//std::cout << trial[0].amount << '\n';
	std::string temp = "EEEEEEEEEEEEEEEE";
	for (int q = 0; q < trial.size(); q++){
		temp[trial[q].pos] = (char)trial[q].amount+'0';

		for (int z = q+1; z < trial.size(); z++){
			bool valid = true;
			if (temp[trial[z].pos]=='E'){
				temp[trial[z].pos] = (char)trial[z].amount + '0';
			}
			for (int b = 0; b < i; b++){
				int stuff = myguesses[b].correctvalues;
				for (int m = 0; m < myguesses[b].value.length(); m++){
					if (temp[m] == myguesses[b].correctvalues){
						stuff--;
					}
				}
				if (stuff < 0){
					valid = false;
					break;
				}
			}
			if (valid == true){

			}
			else{

			}
		}
	}
	return 0;
}