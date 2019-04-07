package main

import "os"

func main() {
	if len(os.Args) != 2 {
		panic("must provide a problem number")
	}
	problemNumber := os.Args[1]

	switch problemNumber {
	case "1":
		problem1()
	case "2":
		problem2()
	case "3":
		problem3()
	case "6":
		problem6()
	case "29":
		problem29()
	default:
		println("not done yet!")
	}
}
