//go:build ignore

package main

import "fmt"

func findWordsContaining(words []string, x byte) []int {
    res := []int{}
	for idx, word := range words {
		for i := range word {
			if word[i] == x {
				res = append(res, idx)
				break
			}
		}
	}
	return res
}

func main() {
	words := []string{"leet", "code"}
	var x byte = 'e'
	fmt.Print(findWordsContaining(words, x))
}