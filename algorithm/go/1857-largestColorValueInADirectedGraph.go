// go: build ignore
package main

import "fmt"

func boolToInt(b bool) int {
	if !b {
		return 0
	}
	return 1
}

func largestPathValue(colors string, edges [][]int) int {
    n := len(colors)
	adj := make([][]int, n)
	rank := make([]int, n)

	for _, e := range edges {
		adj[e[0]] = append(adj[e[0]], e[1])
		rank[e[1]]++
	}

	dp := make([][]int, n)
	for i := 0; i < n; i++ {
		dp[i] = make([]int, 26)
	}

	q := []int{}
	for u := range n {
		if rank[u] == 0 {
			q = append(q, u)
			dp[u][int(colors[u] - 'a')]++
		}
	}

	visited := 0
	res := 0

	for len(q) > 0 {
		u := q[0]
		q = q[1:]
		visited++

		for _, v := range adj[u] {
			for c := range 26 {
				tmp := boolToInt(int(colors[v] - 'a') - c == 0)
				dp[v][c] = max(dp[v][c], dp[u][c] + tmp)
			}
			
			rank[v]--
			if rank[v] == 0 {
				q = append(q, v)
			}
		}

		for _, val := range dp[u] {
			res = max(res, val)
		}
	}

	if visited != n {
		return -1
	}
	return res
}

func main() {
	colors := "abaca"
	edges := [][]int{{0, 1}, {0, 2}, {2, 3}, {3, 4}}
	fmt.Println(largestPathValue(colors, edges))
}