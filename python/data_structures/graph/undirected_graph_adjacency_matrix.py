# Undirected Graph using Adjacency matrix
# vertices/node
# Edges(connection)

from __future__ import annotations


class Graph:
    def __init__(self, vertices: int):
        self.vertices = vertices
        self.adjacency_matrix = self.create_adjacency_matrix(vertices)

    def create_adjacency_matrix(self, vertices: int):
        matrix = [[0 for _ in range(0, vertices)] for _ in range(vertices)]
        return matrix

    def add_edge(self, i, j: int):
        if self.is_empty:
            print("Graph is empty")
            return
        try:
            self.adjacency_matrix[i][j] = 1
            self.adjacency_matrix[j][i] = 1
            print(f"Added edge between {i} and {j}")
        except:
            print("Error adding edge")

    def remove_edge(self, i, j: int):
        if self.is_empty:
            print("Graph is empty")
            return
        try:
            self.adjacency_matrix[i][j] = 0
            self.adjacency_matrix[j][i] = 0
            print(f"Removing edge between {i} and {j}")
        except:
            print("Error removing edge")

    @property
    def is_empty(self) -> bool:
        return len(self.adjacency_matrix) == 0

    def print_adjacency_matrix(self):
        if self.is_empty:
            print("Graph is empty")
            return
        print("Printing Adjacency matrix")
        for i in range(self.vertices):
            for j in range(self.vertices):
                print(self.adjacency_matrix[i][j], end=" ")
            print()  # new line


if __name__ == "__main__":
    graph = Graph(vertices=4)  # 0 1 2 3
    graph.print_adjacency_matrix()

    # Add Egdes
    graph.add_edge(0, 1)  # edge between 0 and 1 vertices
    graph.add_edge(0, 2)  # edge between 0 and 2 vertices
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)

    graph.print_adjacency_matrix()

    # remove edge
    graph.remove_edge(0, 1)  # removes edge between 0 and 1 vertices

    graph.print_adjacency_matrix()
