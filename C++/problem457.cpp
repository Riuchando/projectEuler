#include <iostream>
#include <fstream>
#include <math.h> /* sqrt */
long long f(long long n) { return (n * n) - (3 * n) - 1; }
long long R(long long p)
{
  for (long long i = p; i < p * p; i++)
  {
    long long temp = f(i) % (p * p);
    if (temp == 0)
    {
      return i;
    }
  }
  return 0;
}
int main()
{
  std::fstream primeIn("PrimeNumbers.txt");
  long long answer = 0;
  long long prime;
  primeIn >> prime;
  while (prime < pow(10, 7))
  {
    answer += R(prime);
    primeIn >> prime;
  }
  std::cout << answer << '\n';
  return 0;
}
