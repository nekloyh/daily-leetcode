//go:build ignore

package main

import "fmt"

func longestPalindrome(words []string) int {
    word_cnt := make(map[string]int)

	for _, word := range words {
		word_cnt[word]++
	}

	res := 0
	var center int

	for word, cnt := range word_cnt {
		if word[0] == word[1] {
			if center == 0 {
				center = cnt % 2
			}
			res += (cnt - cnt % 2) * 2
		} else {
			rev := string([]byte{word[1], word[0]})
			if rev > word {
				res += min(cnt, word_cnt[rev]) * 4
			}
		}
	}

	return res + center * 2
}

func main() {
	words := []string{"ab","ty","yt","lc","cl","ab"}
	fmt.Print(longestPalindrome(words))
}