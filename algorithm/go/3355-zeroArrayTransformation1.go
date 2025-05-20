//go:build ignore

package main

import "fmt"

func isZeroArray(nums []int, queries [][]int) bool {
    dec := make([]int, len(nums) + 1)
	for _, q := range queries {
		dec[q[0]] += 1
		dec[q[1] + 1] -= 1;
	}

	minus := 0
	for i := range nums {
		minus += dec[i]
		if nums[i] - minus > 0 {
			return false
		}
	}

	return true
}

func main() {
	nums := []int{1,0,1}
	queries := [][]int{{0,2}}
	fmt.Print(isZeroArray(nums, queries))
}