//go:build ignore

package main

import "fmt"

func sumZero(n int) []int {
	res := []int{}
	if n % 2 == 1 {
		res = append(res, 0)
		n -= 1
	}
	n /= 2
	
	for i := 0; i < n; i+=1 {
		res = append(res, i + 1)
		res = append(res, -i - 1)
	}
	
	return res
}

func main() {
	n := 5
	fmt.Print(sumZero(n))
}