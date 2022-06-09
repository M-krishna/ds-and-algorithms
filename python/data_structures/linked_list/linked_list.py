# Basic Linked list implementation
# Singly linked list

from __future__ import annotations


class Node:
    def __init__(self, data: str, next_node: Node | None = None):
        self.data: str = data
        self.next: Node | None = next_node


class LinkedList:
    def __init__(self):
        self.head: Node | None = None

    def create_node(self, data: str) -> Node:
        print(f"Creating Node with {data}:")
        return Node(data)

    def insert_node(self, data: str):
        if not self.head:
            print(f"Inserting {data} as head")
            self.head = self.create_node(data)
            return

        currentNode = self.head
        while currentNode.next is not None:
            currentNode = currentNode.next
        print(f"Inserting {data}")
        currentNode.next = self.create_node(data)

    def print_values(self):
        if self.is_empty:
            print("Linked list is empty")
            return
        print("Items in Linked list:")
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data, end=" ")
            currentNode = currentNode.next
        print()  # new line

    def delete_node(self, data: str):
        if self.is_empty:
            print("Linked list is empty")
            return
        # check if the data is present in head node
        print(f"Deleting {data}")
        if self.head.data == data:
            self.head = self.head.next
        else:
            previous_node = None
            currentNode = self.head.next
            while currentNode is not None:
                if currentNode.data == data:
                    previous_node.next = currentNode.next
                previous_node = currentNode
                currentNode = currentNode.next
        print("Delete operation done")

    @property
    def is_empty(self):
        return self.head is None


if __name__ == "__main__":
    linkedList = LinkedList()

    # insert values
    for i in range(1, 6):
        linkedList.insert_node(str(i))

    # print values
    linkedList.print_values()

    # delete 3
    linkedList.delete_node("3")

    # print values
    linkedList.print_values()

    # delete 5
    linkedList.delete_node("5")

    # print values
    linkedList.print_values()

    # delete remaining items
    linkedList.delete_node("1")
    linkedList.delete_node("2")
    linkedList.delete_node("4")

    # print values
    linkedList.print_values()
