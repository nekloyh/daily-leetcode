//go:build ignore

package main

import "fmt"

func candy(ratings []int) int {
	n := len(ratings)
	candies := make([]int, n)

	for i := 0; i < n; i++ {
		candies[i] = 1
	}

	for i := 1; i < n; i++ {
		if ratings[i] > ratings[i - 1] {
			candies[i] = candies[i - 1] + 1
		}
	}

	res := candies[n - 1]
	for i := n - 2; i >= 0; i-- {
		if ratings[i] > ratings[i + 1] {
			candies[i] = max(candies[i], candies[i + 1] + 1)
		}
		res += candies[i]
	}

	return res
}

func main() {
	ratings := []int{1, 2, 2}
	fmt.Println(candy(ratings))
}
