//go:build ignore

package main

import (
	"fmt"
)

func countBits(n int) int {
	cnt := 0
	for ; n > 0; n >>= 1 {
		cnt += n & 1
	}
	return cnt
}

func readBinaryWatch(turnedOn int) []string {
	res := []string{}

	for h := 0; h < 12; h++ {
		for m := 0; m < 60; m++ {
			if countBits(h)+countBits(m) == turnedOn {
				timeStr := fmt.Sprintf("%d:%02d", h, m)
				res = append(res, timeStr)
			}
		}
	}

	return res
}

func main() {
	turnedOn := 1
	fmt.Println(readBinaryWatch(turnedOn))
}
