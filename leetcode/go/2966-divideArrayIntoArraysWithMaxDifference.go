//go:build ignore

package main

import (
	"fmt"
	"sort"
)

func divideArray(nums []int, k int) [][]int {
	sort.Ints(nums)
	res := [][]int{}
	for i := 0; i < len(nums); i+=3 {
		if nums[i + 2] - nums[i] > k {
			return [][]int{}
		}
		res = append(res, []int{nums[i], nums[i+1], nums[i+2]})
	}
	return res
}

func main() {
	nums := []int{1,3,4,8,7,9,3,5,1} 
	k := 2
	fmt.Printf("%v\n", divideArray(nums, k))
}