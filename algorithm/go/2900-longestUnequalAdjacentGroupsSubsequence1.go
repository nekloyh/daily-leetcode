//go:build ignore

package main

import (
	"fmt"
)

func getLongestSubsequence(words []string, groups []int) []string {
	len := len(words)
	res := []string{words[0]}  
	prev := groups[0]

	for i := 1; i < len; i++ {
		if prev != groups[i] {
			res = append(res, words[i])
			prev = groups[i]
		} 
	}

	return res
}


func main() {
	words := []string{"a", "b", "c", "d"}
	groups := []int{1, 0, 1, 1}

	result := getLongestSubsequence(words, groups)

	for i := 0; i < len(result); i++ {
		fmt.Printf("%s\t", result[i])
	}
}
