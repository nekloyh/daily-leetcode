//go:build ignore

package main

import "fmt"

func maxDifference(s string) int {
    freq := make([]int, 26)
	for _, ch := range(s) {
		freq[int(ch - 'a')] += 1
	}

	maxOdd := -1
	minEven := 100
	for i := 0; i <= 25; i++ {
		if freq[i] % 2 == 0 {
			if freq[i] == 0 {
				continue
			}
			minEven = min(minEven, freq[i])
		} else {
			maxOdd = max(maxOdd, freq[i])
		}
	}

	return maxOdd - minEven
}

func main() {
	s := "aaaaabbc"
	fmt.Print(maxDifference(s))
}