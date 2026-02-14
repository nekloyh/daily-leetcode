//go:build ignore

package main

import "fmt"

func comb(n, k int) int64 {
	if k < 0 || k > n {
		return 0
	}

	res := int64(1)
	for i := 1; i <= k; i++ {
		res = res * int64(n-i+1) / int64(i)
	}

	return res
}

func distributeCandies(n int, limit int) int64 {
	if n > limit*3 {
		return 0
	}

	res := comb(n+2, 2)

	if n > limit {
		res -= 3 * comb(n-limit+1, 2)
	}

	if n-2 >= 2*limit {
		res += 3 * comb(n-2*limit, 2)
	}

	return res
}

func main() {
	n := 5
	limit := 2
	fmt.Println(distributeCandies(n, limit))
}
