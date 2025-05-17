//go:build ignore

package main

import (
	"fmt"
)

func _sortColors(nums []int) {
	zeros, ptr, twos := 0, 0, len(nums) - 1
	for ptr <= twos {
		if nums[ptr] == 0 {
			nums[ptr], nums[zeros] = nums[zeros], nums[ptr]
			zeros += 1
			ptr += 1
		} else if nums[ptr] == 2 {
			nums[ptr], nums[twos] = nums[twos], nums[ptr]
			twos -= 1
		} else {
			ptr += 1
		}
	}
}

func sortColors(nums []int) {
	freq := []int{0, 0, 0}
	for i := range(len(nums)) {
		freq[nums[i]]++
	}

	idx := 0
	for i := range(3) {
		for freq[i] > 0 {
			nums[idx] = i
			freq[i]--
			idx++
		}
	}
}

func main() {
	_nums := []int{2, 0, 2, 1, 1, 0}
	_sortColors(_nums)
	fmt.Println(_nums)

	nums := []int{2, 0, 2, 1, 1, 0}
	sortColors(nums)
	fmt.Println(nums)
}