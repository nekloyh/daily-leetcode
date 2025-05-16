//go:build ignore

package main

import (
	"fmt"
)

func isHamming(a, b string) bool {
	if len(a) != len(b) {
		return false
	}

	var is_hamming bool
	for i := range a {
		if (a[i] != b[i]) {
			if is_hamming {
				return false
			}

			is_hamming = true
		}
	}

	return is_hamming
}

func reverse(arr []string) {
	for i, j := 0, len(arr) - 1; i < j; i, j = i + 1, j - 1 {
		arr[i], arr[j] = arr[j], arr[i]
	}
}

func getWordsInLongestSubsequence(words []string, groups []int) []string {
    n := len(words)
	dp := make([]int, n)
	prev := make([]int, n)
	for i := range(n){
		prev[i] = -1
		dp[i] = 1
	}
	
	idx := 0

	for i := range n {
		for j := range i {
			if (groups[i] != groups[j] && isHamming(words[i], words[j]) && dp[i] < dp[j] + 1) {
				dp[i] = dp[j] + 1
				prev[i] = j
			}
		}
		
		if (dp[i] > dp[idx]) {
			idx = i
		}
	}

	res := []string{}
	for i := idx; i >= 0; i = prev[i] {
		res = append(res, words[i])
	}
	reverse(res)

	return res
}

func main() {
	words := []string{"adbe","acace"}
	groups := []int{2, 2}

	fmt.Println(getWordsInLongestSubsequence(words, groups))
}