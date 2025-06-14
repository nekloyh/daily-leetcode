//go:build ignore

package main

import (
	"fmt"
	"math"
)

func minMaxDifference(num int) int {
	digits := []int{}
	for num > 0 {
		digits = append([]int{num % 10}, digits...)
		num /= 10
	}

	var mappingMax int
	found := false
	for _, d := range digits {
		if d != 9 {
			mappingMax = d
			found = true
			break
		}
	}
	if !found {
		mappingMax = -1 
	}

	mappingMin := digits[0]

	maxNum, minNum := 0, 0
	for i, d := range digits {
		pos := len(digits) - i - 1
		if d == mappingMax {
			maxNum += 9 * int(math.Pow(10, float64(pos)))
		} else {
			maxNum += d * int(math.Pow(10, float64(pos)))
		}

		if d == mappingMin {
			minNum += 0 * int(math.Pow(10, float64(pos)))
		} else {
			minNum += d * int(math.Pow(10, float64(pos)))
		}
	}

	return maxNum - minNum
}

func main() {
	num := 11891
	fmt.Print(minMaxDifference(num))
}