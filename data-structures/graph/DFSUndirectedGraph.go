// Implementaion of DFS Traversal in undirected Graph.
// Graph data is represented by using Adjancency matrix.

package main

import "fmt"

type undirectedGraph struct {
	AdjMatrix [][]int
	vertices int
}

func NewUndirectedGraph(vertices int) *undirectedGraph {
	matrix := make([][]int, vertices)
	for i := range matrix {
		matrix[i] = make([]int, 5)
	}

	return &undirectedGraph{
		AdjMatrix: matrix,
		vertices: vertices,
	}
}

func (g *undirectedGraph) addEdge(i, j int) {
	g.AdjMatrix[i][j] = 1
	g.AdjMatrix[j][i] = 1
}

func (g *undirectedGraph) removeEdge(i, j int) {
	g.AdjMatrix[i][j] = 0
	g.AdjMatrix[j][i] = 0
}

func (g *undirectedGraph) DFS(start int, visited []bool) {
	// Print out the visited node to the console
	fmt.Printf("%d ", start)

	// mark it as visited
	visited[start] = true

	// for every node of the graph
	for i := 0; i < g.vertices; i++ {
		// If some node is adjacent to the current node
		// and it has not been already visited
		if g.AdjMatrix[start][i] == 1 && !visited[i] {
			g.DFS(i, visited)
		}
	}
}


func main() {
	vertices := 4
	graph := NewUndirectedGraph(vertices)

	graph.addEdge(0,1)
	graph.addEdge(0,2)
	graph.addEdge(1,2)
	graph.addEdge(2,3)

	visited_arr := make([]bool, vertices)

	graph.DFS(0, visited_arr)
	fmt.Println()

	// remove an edge
	graph.removeEdge(2, 3)

	// reinitialize the visisted array
	visited_arr = make([]bool, vertices)

	graph.DFS(0, visited_arr)
}