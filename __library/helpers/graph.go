package main

import (
	"container/heap"
	"fmt"
)

func matrixToGraph(matrix [][]int) map[int]map[int]int {
	/**
	Generate a graph from a matrix if you can go
	UP, DOWN, LEFT, RIGHT, RIGHT-UP, RIGHT-DOWN, LEFT-UP, LEFT-DOWN

	having an Y x X matrix, this generates a graph, where vertices are positions
	in the matrix. For example (i, j) is the vertex i * X + j. And edges are matrix's
	elements. For example having matrix

	1 2
	3 4

	This means that going from (0, 0) you can go to
	- (0, 1) with cost 2,
	- (1, 0) with cost 3
	- (1, 1) with cost 4

	for the matrix X * Y the graph will have approximately 8 * X * Y edges
	*/
	x, y := len(matrix[0]), len(matrix)
	graph := map[int]map[int]int{}
	for i, row := range matrix {
		for j, _ := range row {
			value := i*x + j
			graph[value] = map[int]int{}
			if i > 0 {
				// up
				graph[value][value-x] = matrix[i-1][j]
			}
			if i < y-1 {
				// down
				graph[value][value+x] = matrix[i+1][j]
			}
			if j > 0 {
				// left
				graph[value][value-1] = matrix[i][j-1]
			}
			if j < x-1 {
				// right
				graph[value][value+1] = matrix[i][j+1]
			}

			if i < y-1 && j < x-1 {
				// right down
				graph[value][value+x+1] = matrix[i+1][j+1]
			}
			if i > 0 && j < x-1 {
				// right up
				graph[value][value-x+1] = matrix[i-1][j+1]
			}
			if i < y-1 && j > 0 {
				// left down
				graph[value][value+x-1] = matrix[i+1][j-1]
			}
			if i > 0 && j > 0 {
				// left up
				graph[value][value-x-1] = matrix[i-1][j-1]
			}
		}
	}
	return graph
}

func dijkstraCost(graph map[int]map[int]int, start, end int) int {
	/**
	take priority queue from http://stackoverflow.com/q/30827729/1090562 change
	func (pq PriorityQueue) Less(i, j int) bool {
		  return pq[i].priority < pq[j].priority
	}
	*/

	if start == end {
		return 0
	}
	frontier := make(PriorityQueue, 1)
	frontier[0] = &Item{value: start, priority: 0, index: 0}
	visited := map[int]bool{}
	heap.Init(&frontier)

	for frontier.Len() > 0 {
		element := heap.Pop(&frontier).(*Item)
		vertex, cost := element.value, element.priority
		visited[vertex] = true
		neighbors := graph[vertex]
		for vertex_new, cost_new := range neighbors {
			if !visited[vertex_new] {
				if vertex_new == end {
					return cost + cost_new
				}
				heap.Push(&frontier, &Item{
					value:    vertex_new,
					priority: cost + cost_new,
				})
			}
		}
	}
	return -1
}

func bfsCost(G map[int]map[int]bool, start int, total int) []int {
	/**
	finds the distance from starting position in a graph to any other vertex in the graph
	the distance to a starting vertex is 0, the distance to any node that is unaccessible is also 0
	*/
	cost, seen := make([]int, total+1), make([]bool, total+1)
	frontier := []int{start}
	seen[start] = true
	for len(frontier) > 0 {
		el := frontier[0]
		frontier = frontier[1:]
		for k, _ := range G[el] {
			if !seen[k] {
				seen[k] = true
				frontier = append(frontier, k)
				cost[k] = cost[el] + 1
			}
		}
	}
	return cost
}

func connectedComponents(G map[int]map[int]bool, N int) [][]int {
	/**
	for a graph G, and a number of vertices N (from 1 to N), finds all the connected components.
	If we gave some other vertices, we need to pass them in the function and use it as unseen map
	*/
	components, unseen := [][]int{}, map[int]bool{}
	for i := 0; i < N; i++ {
		unseen[i] = true
	}

	for len(unseen) > 0 {
		frontier, component := []int{}, []int{}
		for k, _ := range unseen {
			frontier = append(frontier, k)
			break
		}

		for len(frontier) > 0 {
			element := frontier[len(frontier)-1]
			frontier = frontier[:len(frontier)-1]
			component = append(component, element)
			delete(unseen, element)
			for k, _ := range G[element] {
				if unseen[k] {
					frontier = append(frontier, k)
					delete(unseen, k)
				}
			}
		}
		components = append(components, component)
	}
	return components
}

func dfs(G map[int]map[int]bool, start int) map[int]bool {
	frontier, seen := []int{start}, map[int]bool{start: true}

	for len(frontier) > 0 {
		el := frontier[len(frontier)-1]
		frontier = frontier[:len(frontier)-1]
		for node := range G[el] {
			if !seen[node] {
				seen[node] = true
				frontier = append(frontier, node)
			}
		}
	}

	return seen
}

func dijkstraDistanceToAll(G map[int]map[int]int, N int, start int) []int {
	/**
	take priority queue from http://stackoverflow.com/q/30827729/1090562 change
	func (pq PriorityQueue) Less(i, j int) bool {
		  return pq[i].priority < pq[j].priority
	}
	*/
	MAX := 99999999

	checked, distance := make([]bool, N+1), make([]int, N+1)
	for i := 0; i <= N; i++ {
		distance[i] = MAX
	}
	distance[start], checked[start] = 0, true

	frontier := make(PriorityQueue, 1)
	frontier[0] = &Item{value: start, priority: 0, index: 0}
	heap.Init(&frontier)

	for v, w := range G[start] {
		heap.Push(&frontier, &Item{value: v, priority: w})
	}

	for frontier.Len() > 0 {
		element := heap.Pop(&frontier).(*Item)
		vertex, cost := element.value, element.priority

		checked[vertex] = true
		if distance[vertex] > cost {
			distance[vertex] = cost
		}

		for vertexNew, costNew := range G[vertex] {
			if !checked[vertexNew] {
				heap.Push(&frontier, &Item{value: vertexNew, priority: cost + costNew})
			}
		}
	}
	return distance
}

func prim(G map[int]map[int]int, N int, start int) int {
	connected := make([]bool, N+1)
	num, total := 0, 0

	frontier := make(PriorityQueue, 1)
	frontier[0] = &Item{value: start, priority: 0, index: 0}
	heap.Init(&frontier)

	for frontier.Len() > 0 && num <= N {
		element := heap.Pop(&frontier).(*Item)
		vertex := element.value
		if !connected[vertex] {
			total += element.priority
			num++
			connected[vertex] = true

			for v, w := range G[vertex] {
				if !connected[v] {
					heap.Push(&frontier, &Item{value: v, priority: w})
				}
			}
		}
	}

	return total
}

func floyd(G map[int]map[int]int, N int) [][]int {
	inf := 99999999
	matrix := [][]int{}
	for i := 0; i < N; i++ {
		line := make([]int, N)
		for j := 0; j < N; j++ {
			line[j] = inf
		}
		matrix = append(matrix, line)
	}

	for i := 0; i < N; i++ {
		matrix[i][i] = 0
	}

	for v1, arr := range G {
		for v2, w := range arr {
			matrix[v1-1][v2-1] = w
		}
	}

	for k := 0; k < N; k++ {
		for i := 0; i < N; i++ {
			for j := 0; j < N; j++ {
				if matrix[i][j] > matrix[i][k]+matrix[k][j] {
					matrix[i][j] = matrix[i][k] + matrix[k][j]
				}
			}
		}
	}

	return matrix
}

func createRootedTree(G map[int][]int, root int) map[int][]int {
	rooted, frontier, seen := map[int][]int{}, []int{root}, map[int]bool{root: true}
	for {
		if len(frontier) == 0 {
			return rooted
		}

		next_frontier := []int{}
		for _, v := range frontier {
			children, _ := G[v]
			for _, child := range children {
				if !seen[child] {
					seen[child] = true
					rooted[v] = append(rooted[v], child)
					next_frontier = append(next_frontier, child)
				}
			}
		}
		frontier = next_frontier
	}
	return rooted
}

func reverseDirectedGraph(G map[int]map[int]bool) map[int]map[int]bool {
	Gr := map[int]map[int]bool{}
	for k, _ := range G {
		Gr[k] = map[int]bool{}
	}

	for s, set := range G {
		for e, _ := range set {
			Gr[e][s] = true
		}
	}

	return Gr
}

func main() {

}
