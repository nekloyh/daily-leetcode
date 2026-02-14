//go:build ignore

package main

import "fmt"

func lengthAfterTransformations(s string, t int) int {
    const MOD = 1e9 + 7
	var res int
	freq := make([]int, 26)
	
	for _, ch := range s {
		freq[ch - 'a']++
	}

	
	for i := 0; i < t; i++ {
		temp := make([]int, 26)

		for j := 0; j < 25; j++ {
			temp[j + 1] = freq[j]
		}

		temp[0] = freq[25]
		temp[1] = (temp[1] + freq[25]) % MOD

		freq = temp
	}
	
	for i := 0; i <= 25; i++ {
		res = (res + freq[i]) % MOD
	}

	return res
}

func main() {
	s := "abcyy"
	t := 2
	fmt.Println(lengthAfterTransformations(s, t))
}