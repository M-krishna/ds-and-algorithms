# Doubly linked list

from __future__ import annotations


class Node:
    def __init__(
        self,
        data: str | None = None,
        prev_node: Node | None = None,
        next_node: Node | None = None,
    ):
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def create_node(self, data: str) -> Node:
        return Node(data=data)

    def insert_node(self, data: str) -> None:
        if self.head is None:
            print(f"Inserting {data} as head")
            self.head = self.create_node(data)
            return

        currentNode = self.head
        while currentNode.next_node is not None:
            currentNode = currentNode.next_node

        new_node = self.create_node(data)
        print(f"Inserting {new_node.data}")
        currentNode.next_node = new_node
        new_node.prev_node = currentNode

    def remove_node(self, data: str) -> None:
        if self.is_empty:
            print("DLL is empty")
            return

        if self.head.data == data:
            print(f"Removing head: {data}")
            if self.head.next_node is None:
                self.head = None
                return
            self.head = self.head.next_node
            if self.head:
                self.head.prev_node = None
            return

        found = False
        currentNode = self.head
        while currentNode is not None:
            if currentNode.data == data:
                found = True
                print(f"Removing {data} from DLL")
                prev_node = currentNode.prev_node
                next_node = currentNode.next_node
                if prev_node:
                    prev_node.next_node = next_node
                if next_node:
                    next_node.prev_node = prev_node
                break
            currentNode = currentNode.next_node
        if not found:
            print(f"{data} is not present in DLL")

    @property
    def is_empty(self) -> bool:
        return self.head == None

    def print_values(self) -> None:
        if self.is_empty:
            print("DoublyLinkedList is empty")
            return
        print("Values: ", end=" ")
        currentNode = self.head
        while currentNode is not None:
            print(f"{currentNode.data}", end=" ")
            currentNode = currentNode.next_node
        print()

    def print_reverse(self) -> None:
        if self.is_empty:
            print("DoublyLinkedList is empty")
            return
        currentNode = self.head
        while currentNode is not None:
            last_node = currentNode
            currentNode = currentNode.next_node

        print("Reverse order: ", end=" ")
        while last_node is not None:
            print(last_node.data, end=" ")
            last_node = last_node.prev_node
        print()  # new line


if __name__ == "__main__":
    dll = DoublyLinkedList()

    START = 0
    END = 6

    for i in range(START, END):
        dll.insert_node(str(i))

    dll.print_values()

    dll.print_reverse()

    dll.remove_node(str(3))

    dll.print_values()

    dll.print_reverse()

    dll.remove_node(str(5))

    dll.print_values()

    dll.print_reverse()

    dll.remove_node(str(4))

    dll.print_values()

    dll.print_reverse()

    dll.remove_node(str(0))

    dll.print_values()

    dll.print_reverse()

    dll.remove_node(str(1))

    dll.print_values()

    dll.print_reverse()

    dll.remove_node(str(2))

    dll.print_values()

    dll.print_reverse()
