//go:build ignore

package main

import (
	"fmt"
	"math/bits"
)

func makeTheIntegerZero(num1 int, num2 int) int {
	if num2 >= num1 {
		return -1
	}
	
	k := 1
	for {
		temp := int64(num1) - int64(k)*int64(num2)
		if temp <= 0 {
			return -1
		}

		count := bits.OnesCount64(uint64(temp))
		if k >= count && k <= int(temp) {
			return k
		}
		k++
	}
}

func main() {
	num1, num2 := 3, -2
	fmt.Print(makeTheIntegerZero(num1, num2))
}