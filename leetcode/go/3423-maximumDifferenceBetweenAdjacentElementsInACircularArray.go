//go:build ignore

package main

import (
	"fmt"
)

func absInt(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func maxInt(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func maxAdjacentDistance(nums []int) int {
	res := absInt(nums[len(nums) - 1] - nums[0]) 
	for i := 1; i < len(nums); i++ {
		res = maxInt(res, absInt(nums[i - 1] - nums[i]))
	}
	return res
}

func main() {
	nums := []int{1, 2, 4}
	fmt.Println(maxAdjacentDistance(nums))
}