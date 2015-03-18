#include<vector>
#include<fstream>
#include<string>
class PrimeNumber{
public:	PrimeNumber(){
		std::ofstream primeOut("PrimeNumbers.txt");
		std::vector<double> primeNumbers;
		std::vector<double>::iterator myit;
		primeNumbers.push_back(2);//to avoid confusion
		primeOut << 2.0 << '\t';
		int size = 1;//since it already has 2, used to avoid iterators when unnessary
		for (double i = 3; i <= pow(10, 5) + 1; i++){
			double upperbound = sqrt(i);//to short curcuit
			bool flag = true;//to avoid the iterator==pimenumber.end
			for (myit = primeNumbers.begin(); (*myit) <= upperbound; myit++){
				if (fmod(i, (*myit)) == 0.0){
					flag = false;// the current number is NOT a prime
					break;
				}
			}
			if (flag == true){// if it got through the entire loop
				primeNumbers.push_back(i);//the number is prime
				primeOut << std::to_string(i)<<'\t';
				size++;
			}
		}
	}
	PrimeNumber(unsigned long long upperbound){
		std::ofstream primeOut("PrimeNumbers.txt");
		std::vector<double> primeNumbers;
		std::vector<double>::iterator myit;
		primeNumbers.push_back(2);//to avoid confusion
		primeOut << 2.0<<'\t';
		int size = 1;//since it already has 2, used to avoid iterators when unnessary
		for (double i = 3; i <= upperbound + 1; i++){
			double upperbound = sqrt(i);//to short curcuit
			bool flag = true;//to avoid the iterator==pimenumber.end
			for (myit = primeNumbers.begin(); (*myit) <= upperbound; myit++){
				if (fmod(i, (*myit)) == 0.0){
					flag = false;// the current number is NOT a prime
					break;
				}
			}
			if (flag == true){// if it got through the entire loop
				primeNumbers.push_back(i);//the number is prime
				primeOut << std::to_string(i)<<'\t';
				size++;
			}
		}
	}
	
};
