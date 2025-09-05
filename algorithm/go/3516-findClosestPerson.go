//go:build ignore

package main

import "fmt"

func abs(n int) int {
	if n > 0 {
		return n
	}
	return -n
}

func findClosest(x int, y int, z int) int {
	if abs(x - z) == abs(y - z) {
		return 0
	}
	if abs(x - z) > abs(y - z) {
		return 2
	}
	return 1
}

func main() {
	x, y, z := 2, 7, 4
	fmt.Print(findClosest(x, y, z))
}