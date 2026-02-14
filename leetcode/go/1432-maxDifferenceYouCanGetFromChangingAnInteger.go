package main

import (
	"fmt"
	"strconv"
	"strings"
)

func maxDiff(num int) int {
	numStr := strconv.Itoa(num)
	uniqueDigits := make(map[byte]bool)
	for i := 0; i < len(numStr); i++ {
		uniqueDigits[numStr[i]] = true
	}

	maxVal := num
	minVal := num

	for digit := range uniqueDigits {
		for d := byte('0'); d <= '9'; d++ {
			if numStr[0] == digit && d == '0' {
				continue
			}

			newStr := strings.ReplaceAll(numStr, string(digit), string(d))
			newNum, err := strconv.Atoi(newStr)
			if err != nil {
				continue
			}
			if newNum > maxVal {
				maxVal = newNum
			}
			if newNum < minVal {
				minVal = newNum
			}
		}
	}

	return maxVal - minVal
}

func main() {
	num := 555
	fmt.Println(maxDiff(num)) 
}
