//go:build ignore

package main

import (
	"fmt"
	"sort"
)

func maximumValueSum(nums []int, k int, edges [][]int) int64 {
	var res int64
	for i := range len(nums) {
		res += int64(nums[i])
	}

	dif := []int{}
	for i := range len(nums) {
		dif = append(dif, nums[i] ^ k - nums[i])
	}
	sort.Slice(dif, func(i, j int) bool {
		return dif[i] > dif[j]
	})

	for i := 1; i < len(dif); i+=2 {
		if (dif[i] + dif[i - 1]) >= 0 {
			res += int64(dif[i] + dif[i - 1])
		}
	}

	return res
}

func main() {
	nums := []int{7,7,7,7,7,7}
	k := 3
	edges := [][]int{{0,1},{0,2},{0,3},{0,4},{0,5}}

	fmt.Print(maximumValueSum(nums, k, edges))
}