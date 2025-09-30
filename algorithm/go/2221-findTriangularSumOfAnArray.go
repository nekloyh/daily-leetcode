//go:build ignore

package main

import "fmt"

func triangularSum(nums []int) int {
	if len(nums) == 0 {
		return 0
	}

	for m := len(nums); m > 1; m-- {
		for i := 0; i < m - 1; i++ {
			nums[i] = (nums[i] + nums[i + 1]) % 10
		}
	}
	return nums[0]
}

func main() {
	nums := []int{1, 2, 3, 4, 5}
	fmt.Println(triangularSum(nums))
}