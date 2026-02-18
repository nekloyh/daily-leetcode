//go:build ignore

package main

import "fmt"

func hasAlternatingBits(n int) bool {
    flag := n & 1
	n >>= 1

	for ; n > 0; n >>= 1 {
		if n & 1 == flag {
			return false
		}
		flag = n & 1
	}

	return true
}

func main() {
	n := 5
	fmt.Print(hasAlternatingBits(n))
}