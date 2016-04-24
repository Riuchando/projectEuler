package main
import (
	"fmt"
	 "math"
	)
func main() {
	fmt.Println("Hello, playground")
	//var m map[string]int
	var logMemo map[float64]bool
	logMemo = make(map[float64]bool)
	for i := 2; i <= 100; i++ {
		for j:=2 ; j<= 100 ; j++ {
		//precision problems, maybe make it arbitrary precision
		var tmp float64 =float64(i)*math.Log(float64(j))
		//if item does not exist, add here
		if logMemo[tmp]!=true {
		//fmt.Println(tmp)
		logMemo[tmp]=true
		}
		
		//fmt.Println(float64(i)*math.Log(float64(j)))
		}
	}
	//print length of list
	fmt.Println(len(logMemo))
}