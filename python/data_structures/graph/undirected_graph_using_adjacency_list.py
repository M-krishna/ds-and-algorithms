# Undirected Graph using adjancency list, undirected graph means we can travel both ways. If there is a edge between (a, b) then we can go from a -> b and b -> a.
# vertices/node
# edges(connection)

# we'll use linked list to represent the graph
# we'll maintain an array of length is equal to total number of vertices
# the array holds the head node for each vertices

from __future__ import annotations
from collections import deque


class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: Node | None = None


class Graph:
    def __init__(self, vertices: int):
        self.array: list[Node] = [None] * vertices

    def add_edge(self, source: int, destination: int) -> None:
        destination_node = Node(destination)
        destination_node.next = self.array[source]
        self.array[source] = destination_node

        source_node = Node(source)
        source_node.next = self.array[destination]
        self.array[destination] = source_node

    def print_values(self) -> None:
        for i, v in enumerate(self.array):
            print(f"{i}: ", end=" ")
            current_node = v
            while current_node:
                print(f"{current_node.data}", end="->")
                current_node = current_node.next
            print()

    def bfs(self, index: int) -> None:
        print(f"BFS for node {index}")
        visited_array = [False] * len(self.array)
        queue = deque()

        queue.append(index)
        visited_array[index] = True

        while len(queue) != 0:
            index = queue.popleft()
            print(f"BFS: {index}")
            child_node = self.array[index]

            while child_node is not None:
                if not visited_array[child_node.data]:
                    queue.append(child_node.data)
                    visited_array[child_node.data] = True
                child_node = child_node.next

    def dfs(self, index: int) -> None:
        print(f"DFS for {index}")
        visited_array = [False] * len(self.array)
        stack = deque()

        stack.append(index)
        visited_array[index] = True

        while len(stack) != 0:
            index = stack.pop()
            print(f"index: {index}")
            child_node = self.array[index]

            while child_node is not None:
                if not visited_array[child_node.data]:
                    stack.append(child_node.data)
                    visited_array[child_node.data] = True
                child_node = child_node.next

    def __repr__(self) -> str:
        return f"{self.array}"


if __name__ == "__main__":
    graph = Graph(7)
    print(graph)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(4, 5)
    graph.add_edge(4, 6)
    graph.print_values()
    graph.bfs(4)
    graph.bfs(0)
    graph.bfs(3)
    graph.bfs(2)
    graph.dfs(0)
