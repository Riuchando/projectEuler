//Author Stephen Kinser
//Problem 124

#include<iostream>
#include<vector>
#include<algorithm>
struct radn{
	unsigned long par1;
	unsigned long par2;
 
};
bool myfunc(const radn& lhs, const radn& rhs){ return lhs.par2 < rhs.par2; };
int radN(int input);
int main(){
	std::vector<radn> myList;
	for (int i = 1; i < 100000; i++){
		radn temp;
		temp.par1 = i;
		temp.par2 = radN(i);
		myList.push_back(temp);
	}
	std::sort(myList.begin(), myList.end(), myfunc);
	int answer = myList[10000 - 1].par1;
	int other = myList[10000 - 1].par2;
	std::cout << answer << '\n';
	return 0;
}
int radN(int input){
	for (int j = 2; j <= sqrt(input); j++){
		bool flag = false;
		while (input % j==0){
			input /= j;
			flag = true;
		}
		if (flag == true){
			input *= j;
		}
	}
	return input;


}