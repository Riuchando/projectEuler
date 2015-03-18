//Author:Stephen Kinser



#include<iostream>
#include<string>
#include<fstream>
int main(){
	std::ofstream dataOut("problem110_analysis.txt");
	int upperbound = 1000;
	int answer = 0;
	int primes[] = { 2, 3, 5, 7, 11, 13, 17, 19, 23,29 };
	int currmax = 0;
	unsigned long long maxSize = 100000000;
	unsigned long long* otherarray= NULL;
	otherarray= new unsigned long long[maxSize];
	for (int i = 0; i < maxSize;i++){
		otherarray[i] = 0;
	}
	
		for (long long i = 2; i <= maxSize; i++){
			
			for (long long j = i; j <= i*(i - 1); j++){

				if ((i*j) % (i + j) == 0){
					unsigned long long value = (i*j) / (i + j);
					otherarray[value]++;
					if ( otherarray[value]> currmax){
						
						currmax = otherarray[value];
						if (answer != value){
							answer = value;
							dataOut << std::to_string(answer) << '\t' << std::to_string(currmax - 1 )<< '\n';
						}
						break;
					}
				}
				
			}
		}

	std::cout << answer;
	return 0;
}