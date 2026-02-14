//go:build ignore

package main

import "fmt"

func minNumberOperations(target []int) int {
    res := 0
	prev := 0
	for i := 0; i < len(target); i++ {
		if target[i] > prev {
			res += target[i] - prev
		}
		prev = target[i]
	} 

	return res
}

func main() {
	target := []int{3,1,5,4,2}
	fmt.Println(minNumberOperations(target))
}
