//Author: Stephen Kinser
//Problem 67

#include<iostream>
#include<fstream>
#include<vector>
int main(){
	std::fstream myfs;
	myfs.open("p067_triangle.txt");
	if (!myfs){
		std::cout << "error\n";
	}
	int dildo;
	
	myfs >> dildo;
	std::vector<int> hart_s_anus;
	int toilet[100]{};
	
	
	hart_s_anus.push_back(dildo);
	while (true){
		myfs >> dildo;
		
		if (myfs.eof()){
			break;
		}
		hart_s_anus.push_back(dildo);
	}
	myfs.close();
	//toilet[0] += hart_s_anus[0];
	//toilet[0] += hart_s_anus[1];
	//toilet[1] += hart_s_anus[2];
	int count = 0;
	for (int ring = 1; ring <= 100; ring++){
	int pos = (ring*(ring - 1) / 2);
		for (int stain = ring-1; stain>=0; stain--){
			if (stain == 0){
				toilet[0] += hart_s_anus[pos];
			}
			else if (stain == ring - 1){
				toilet[stain] = hart_s_anus[pos + stain] + toilet[ring-2];
			}
			else{
				toilet[stain] = toilet[stain] > toilet[stain - 1] ? toilet[stain] + hart_s_anus[pos + stain] : toilet[stain-1] +hart_s_anus[pos + stain];
			}
			count++;
		}
	}
	int answer = 0;
	for (int i = 0; i < 100; i++){
		if (toilet[i] > answer){
			answer = toilet[i];
		}
	}
	std::cout << answer;
	
	return 0;
}