package main

import "fmt"

//The prime factors of 13195 are 5, 7, 13 and 29.
//What is the largest prime factor of the number 600851475143 ?

func problem3() {

	var number int64 = 600851475143
	var i int64 = 2
	for i < number {
		if number%i == 0 {
			number = number / i
		}
		i++
	}
	fmt.Println("Largest Prime Factor:", i)
}
