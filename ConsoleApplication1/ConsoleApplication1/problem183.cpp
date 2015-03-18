//Author: Stephen Kinser
//Problem 183

#include<iostream>
#include<vector>
#include<algorithm>
struct pair{
	int div;
	int rem;
	bool operator==(pair rhs){
		return (div == rhs.div) && (rem == rhs.rem);
	}
};
bool repeating(long long one, long long two);
long long gcd(long long a, long long b);
int main(){
	long long sum = 0;
	for (double i = 11; i < 100; i++){
		bool flag = false;
		double upperbound = 1 * log10(i);
		double j;
		for ( j = 2; flag == false; j++){
			if (j*log10(i/j) > upperbound){
				upperbound = j*log10(i/j);
			}
			else{
				flag = true;
			}

		}
		double fractionpart = 1;
		for (int k = 0; k < j - 2; k++){
			fractionpart *= i / (j-2);
		}
		//fractionpart = fmod(fractionpart*pow((j - 2), (j - 2)), pow((j - 2), (j - 2)));
		double square = pow((j - 2), (j - 2));
		//fractionpart = fractionpart*square;
		int count = 1;
		double copy = fractionpart;
		while (fractionpart > square){
			if (count < square){
				fractionpart += copy;
				count++;
			}
			fractionpart = fractionpart - square;
		}
		double GCD = gcd(fractionpart, square);
			sum = repeating(fractionpart/GCD, square/GCD)? sum+(j-2): sum-(j-2);
	}
	std::cout << sum << '\n';

	return 0;
}
bool repeating(long long one, long long two){
	if (one == 0){
		return false;
	}
	std::vector<pair> velociraptor;
	std::vector<pair>::iterator trex;
	pair temp;
	temp.div = one/two;
	temp.rem = one;
	while (temp.rem != 0 && velociraptor.size()<1000){
		temp.div = temp.rem / two;
		while (temp.rem < two*temp.div || temp.div==0 ){
			temp.rem *= 10;
			temp.div = temp.rem / two;
		}
		
		temp.rem =  temp.rem - temp.div*two;

		trex = std::find(velociraptor.begin(), velociraptor.end(), temp);
		if (trex == velociraptor.end()){
			velociraptor.push_back(temp);
		}
		else{
			
			return true;
		}

	}

	return false;
}

long long gcd(long long a, long long b)
{
	int c;
	while (a != 0) {
		c = a; a = b%a;  b = c;
	}
	return b;
}