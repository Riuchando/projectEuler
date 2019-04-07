//Author: Stephen Kinser
//Problem 114
/*
A row measuring seven units in length has red blocks with a minimum length of three units placed on it, such that any two red blocks (which are allowed to be different lengths) are separated by at least one black square. There are exactly seventeen ways of doing this.

How many ways can a row measuring fifty units in length be filled?
*/

#include <iostream>

int main()
{
  /*
		with 7, the 17 possibilities are:
		length of red : combinations
		0: 1
		3: 5
		4: 4
		5: 3
		6: 2 
		7: 1 +1 
		the +1 being a red of length 3 + 1 black + red of length 3= 7

		conjecture: 
		0: 1
		(n>3)n: (size-n) +1 ; eg for size 50, 3: 48 or for size 7, 3: 5
		(L>=7) l: if l is even then it is (size-L)(size-L-1) if it is odd, (l)(l-1)/2:
		why?
		let r be red, b be black
		this is the first iteration: 3r+1b+3r+43b;
		both: 3r+2b+3r+42b; and 1b+3r+1b+3r+42b; are valid
		if 3r (+1b) leads, there are 50-7 combinations 
		if 1b+3r (+1b) leads, there are 50-8 combinations, 
		so (43)(42)/2
		with even numbers:
		both 4r+1b+3r+ 42b; and 3r+1b+4r+ 42b; are valid as first iterations
		so take what is known from the first:
		(size - L)(size - L-1)/2
		(46-3)(45-3)/2	and (47-4)(46-4)/2
		which are the same so:
		(43)(42)
		for k > 8: 3r+ 1b+ 5r: and 4r+1b + 4r: and 5r+1b+ 3r
		*****************************************************************
		New conjecture:
		for k>6 : ((Size- k+2)(size-k+1)/2)*(k-6)
		****************************************************************
		The problem didn't specify HOW many reds there would be, so assume infinite or 4/size amounts
		new conjecture:
		ring = 2*blockSize;
		for  k> ring :  ((Size- k+2)(size-k+1)/2)*(k-ring)

		for k > ring+4  :((Size- k-1)(size-k-2)/2)*(k-ring)
		for k > ring+4+4 :((Size- k-5)(size-k-6)/2)*(k-ring)
		*****************************************************************
		
		****************************************************************
	*/
  double answer = 1; //hyp
  int size = 29;
  int blocksize = 3;
  int ring = 0;
  for (int i = blocksize; i <= size; i++)
  {
    answer += (size - i + 1);
    if (i > 6)
    {
      ring = 0;
      for (int j = 2 * blocksize; j < i; j += 4)
      {
        int value = (ring * (blocksize + 1));
        answer += (size - i + 2) * (size - i + 1) / 2 * (i - j);
        ring++;
      }
    }
  }

  std::cout << answer << '\n';
  return 0;
}