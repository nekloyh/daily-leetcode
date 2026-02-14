//go:build ignore

package main

import "fmt"

func triangleType(nums []int) string {
	if nums[0] == nums[1] && nums[1] == nums[2] {
		return "equilateral" 
	}

	if nums[0] > nums[1] {
		nums[0], nums[1] = nums[1], nums[0]
	}

	if nums[1] > nums[2] {
		nums[1], nums[2] = nums[2], nums[1]
	}

	if nums[0] > nums[1] {
		nums[0], nums[1] = nums[1], nums[0]
	}

	if nums[0] + nums[1] <= nums[2] {
		return "none"
	}

	if nums[0] == nums[1] || nums[1] == nums[2] {
		return "isosceles" 
	}

	return "scalene"
}

func main() {
	nums := []int{3, 3, 3}
	fmt.Printf(triangleType(nums))
}