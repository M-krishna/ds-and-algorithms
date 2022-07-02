# WIP
# Basic circular linked list implementation

from __future__ import annotations

class Node:
	def __init__(self, data: str | None = None, next_node: Node | None = None):
		self.data = data
		self.next_node = next_node

class CircularLinkedList:
	def __init__(self):
		self.head = None

	def create_node(self, data: str) -> Node:
		return Node(data)

	def is_empty(self) -> bool:
		return self.head is None

	def insert(self, data: str) -> None:
		if self.head is None:
			self.head = self.create_node(data)
			self.head.next_node = self.head
		else:
			new_node = self.create_node(data)
			currentNode = self.head
			while currentNode.next_node is not self.head:
				currentNode = currentNode.next_node
			new_node.next_node = currentNode.next_node
			currentNode.next_node = new_node

	def insert_before(self, data: str, new_data: str) -> None:
		if self.is_empty:
			print("CLL is empty")
			return
		new_node = self.create_node(new_data)
		if self.head.data == data:
			temp = self.head
			self.head = new_node
			self.head.next_node = temp
			temp.next_node = self.head
		else:
			currentNode = self.head.next_node
			while currentNode is not self.head:
				if currentNode.data == data:
					


	def insert_after(self, data: str, new_data: str) -> None:
		pass


	def print_values(self) -> None:
		print(f"Items in CLL:")
		currentNode = self.head
		while currentNode.next_node is not self.head:
			print(f"{currentNode.data}", end=" ")
			currentNode = currentNode.next_node
		print() # new line


if __name__ == "__main__":
	cll = CircularLinkedList()

	for i in range(6):
		cll.insert(str(i))

	cll.print_values()