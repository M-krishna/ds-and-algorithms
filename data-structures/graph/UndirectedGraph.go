// creating an undirected graph using 
// adjacency matrix

package main

import "fmt"

type UndirectedGraph struct {
	AdjMatrix [][]int
	vertices int
}

func NewUndirectedGraph(vertices int) *UndirectedGraph {
	matrix := make([][]int, vertices)
	for i := range matrix {
		matrix[i] = make([]int, vertices)
	}
	return &UndirectedGraph{
		AdjMatrix: matrix,
		vertices: vertices,
	}
}

func (g *UndirectedGraph) addEdge(i, j int) {
	g.AdjMatrix[i][j] = 1
	g.AdjMatrix[j][i] = 1
}

func (g *UndirectedGraph) removeEdge(i, j int) {
	g.AdjMatrix[i][j] = 0
	g.AdjMatrix[j][i] = 0
}

func (g *UndirectedGraph) displayGraph() {
	for _, row := range g.AdjMatrix {
		for _, val := range row {
			fmt.Printf("%d ", val)
		}
		fmt.Println()
	}
}

func main() {
	vertices := 4
	graph := NewUndirectedGraph(vertices)
	graph.addEdge(0,1)
	graph.addEdge(0,2)
	graph.addEdge(1,2)
	graph.addEdge(2,0)
	graph.addEdge(2,3)

	graph.displayGraph()
}