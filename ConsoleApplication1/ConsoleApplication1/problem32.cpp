//Stephen Kinser
//Problem 32
#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
bool pandigital(unsigned long, unsigned long, unsigned long);
int main(){
	std::vector<unsigned long> mylist;
	std::vector<unsigned long>::iterator myiter;
	unsigned long answer = 0;
	for (unsigned long i = 0; i < 10000; i++){
		for (unsigned long j = i+1; j < 10000; j++){
			unsigned long product = i*j;
			if (log10(product)+log10(j)+log10(i) > 9){
				break;
			}
			if (pandigital(i, j, product)){
				myiter = find(mylist.begin(), mylist.end(), product);
				if (myiter == mylist.end()){
					mylist.push_back(product);
					answer += product;
				}
			}
		}
	}

	std::cout << answer << '\n';

	return 0;
}
bool pandigital(unsigned long one, unsigned long two, unsigned long three){
	std::string panD = "123456789";
	std::string comparison = std::to_string(one) + std::to_string(two) + std::to_string(three);
	if (panD.length() != comparison.length()){
		return false;
	}
	
		for (int j = 0; j < comparison.length(); j++){
			bool found = false;
			for (int i = 0; i < panD.length(); i++){
				if (comparison[j] == panD[i]){
					panD.erase(panD.begin() + i);
					found = true;
					break;
				}
				
			}
			if (found == false){
				return false;
			}
		}
		
	
	return true;
}