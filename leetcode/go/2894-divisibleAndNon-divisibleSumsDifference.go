//go:build ignore

package main

import "fmt"

func differenceOfSums(n int, m int) int {
	res := 0
	for num := 0; num <= n; num ++ {
		if num % m == 0 {
			res -= num
		} else {
			res += num
		}
	}

	return res
}

func main() {
	n, m := 10, 3
	fmt.Print(differenceOfSums(n, m))
}