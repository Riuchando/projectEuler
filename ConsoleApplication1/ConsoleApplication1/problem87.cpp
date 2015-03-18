//Author: Stephen Kinser
//Problem 87

#include<iostream>
#include<vector>
#include<fstream>
#include<algorithm>
int main(){
	std::fstream primeIn("PrimeNumbers.txt");
	std::vector<double> primeNumbers;
	std::vector<long> possibilities;
	std::vector<long>::iterator myit;
	double temp;
	int size = 1;
	primeNumbers.push_back(2);

	while (true){
		primeIn >> temp;
		if (temp > 7200) break;
		primeNumbers.push_back(temp);
		size++;
	}
	primeIn.close();
	for (int i = 0; i < size; i++){
		long term_one = pow(primeNumbers[i], 2);
		if (term_one > 50000000){
			break;
		}
		for (int j = 0; j < size; j++){
			long term_two = pow(primeNumbers[j], 3);
			if (term_two + term_one > 50000000){
				break;
			}

			for (int k = 0; k < size; k++){
				long term_three = pow(primeNumbers[k], 4);
				if (term_one + term_two + term_three > 50000000)
				{
					break;
				}
				long sum = term_one + term_two + term_three;
				myit = find(possibilities.begin(), possibilities.end(), sum);
				if (myit == possibilities.end()&& sum<50000000){
					possibilities.push_back(sum);

				}
			}
		}
	}
	std::cout << possibilities.size() << '\n';
	return 0;
}