//go:build ignore

package main

import (
	"fmt"
	"sort"
)

func partitionArray(nums []int, k int) int {
	if len(nums) == 1 {
		return 1
	}

	sort.Ints(nums)
	n := len(nums)
	res, pnt := 1, n - 1

	for i := n - 2; i >= 0; i-- {
		if nums[pnt] - nums[i] > k {
			res += 1
			pnt = i
		}
	} 
	return res
}

func main() {
	nums := []int{3,6,1,2,5}
	k := 2
	fmt.Print(partitionArray(nums, k))
}