package main

import (
	"fmt"
	"math"
)

/*
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
*/
func problem6() {
	var number float64 = 0
	var i float64 = 1
	//there's probably a single line formula like the (n*n+1)/2
	for i < 100 {
		number += math.Pow(i, 2)
		i++
	}
	var number2 float64 = math.Pow(100*101/2, 2)
	//fmt.Println("difference:",number2-number)
	fmt.Sprintf("%f", number2-number) // print with infinite precision plz
}
