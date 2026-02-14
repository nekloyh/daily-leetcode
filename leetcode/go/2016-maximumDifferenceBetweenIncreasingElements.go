//go:build ignore

package main

import "fmt"

func maximumDifference(nums []int) int {
    res := -1
    m := nums[0]
    for i := 1 ; i < len(nums) ; i++ { 
        if nums[i] > m { 
            res = max(res, nums[i] - m)
        }
        m = min(m,nums[i])
    }   
    return res
}

func main() {
	nums := []int{7,1,5,4}
	fmt.Print(maximumDifference(nums))
}