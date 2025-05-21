//go:build ignore

package main

import "fmt"

func setZeroes(matrix [][]int)  {
	row, col := make([]bool, len(matrix)), make([]bool, len(matrix[0]))


    for i, v := range matrix {
		for j := range len(v) {
			if matrix[i][j] == 0 {
				row[i] = true
				col[j] = true
			}
		}
	}

	for i, v := range matrix {
		for j := range len(v) {
			if row[i] == true || col[j] == true {
				matrix[i][j] = 0
			}
		}
	}
}

func main() {
	matrix := [][]int{{1, 1, 1} , {1, 0, 1}, {1, 1, 1}}
	setZeroes(matrix)

	fmt.Println(matrix)
}