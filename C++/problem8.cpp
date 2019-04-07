//Author:Stephen Kinser
//problem 8:project euler
/*
The four adjacent digits in the 1000-digit number that have the greatest product are 9 � 9 � 8 � 9 = 5832.
Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
*/
#include <iostream>
#include <string>
#include <queue>
#include <iomanip>
int size = 13;
std::string bigNum = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450";
bool reset(long long &bal, std::queue<int> &myQueue, int &start);
int main()
{

  std::queue<int> myQueue;
  unsigned long long answer = 1.0;
  unsigned long long currentBalance = 1.0;

  answer = currentBalance;
  for (int k = 0; k < bigNum.length() - size; k++)
  {
    currentBalance = ((int)bigNum[k] - '0');
    currentBalance *= ((int)bigNum[k + 1] - '0');
    currentBalance *= ((int)bigNum[k + 2] - '0');
    currentBalance *= ((int)bigNum[k + 3] - '0');
    currentBalance *= ((int)bigNum[k + 4] - '0');
    currentBalance *= ((int)bigNum[k + 5] - '0');
    currentBalance *= ((int)bigNum[k + 6] - '0');
    currentBalance *= ((int)bigNum[k + 7] - '0');
    currentBalance *= ((int)bigNum[k + 8] - '0');
    currentBalance *= ((int)bigNum[k + 9] - '0');
    currentBalance *= ((int)bigNum[k + 10] - '0');
    currentBalance *= ((int)bigNum[k + 11] - '0');
    currentBalance *= ((int)bigNum[k + 12] - '0');
    if (currentBalance > answer)
    {
      answer = currentBalance;
    }
  }
  /*
	ELEGANT SOLUTION?
	for (int i = 0; i < size; i++){
		myQueue.push(int(bigNum[i] - '0'));
		currentBalance *= int(bigNum[i] - '0');
	}
	for (int j = size; j < bigNum.length() - 1; j++){
		
		int lastNum = int(bigNum[j] - '0');
		if (lastNum == 0){
			bool flag = false;
			while (flag==false&& j<bigNum.length()-size){
				flag = reset(currentBalance, myQueue, j);
			}
		}
		else{
			int firstNum = myQueue.front();
			myQueue.pop();
			myQueue.push(lastNum);
			currentBalance =  long long( currentBalance / firstNum)*lastNum;
		}
		if (currentBalance > answer){
			answer = currentBalance;
		}

	}*/
  std::cout << answer << '\n';
  return 0;
}
bool reset(long long &bal, std::queue<int> &myQueue, int &start)
{

  while (!myQueue.empty())
  {
    myQueue.pop();
  }
  bal = 1;
  int k;
  for (k = start + 1; k <= start + size; k++)
  {
    if (bigNum[k] == '0')
    {
      start = k;
      bal = 1;
      return false;
    }
    myQueue.push(int(bigNum[k] - '0'));
    bal *= int(bigNum[k] - '0');
    if (bal > 8821658160)
    {
      std::cout << std::setprecision(16) << bal << '\n';
    }
  }
  start = k;
  return true;
}