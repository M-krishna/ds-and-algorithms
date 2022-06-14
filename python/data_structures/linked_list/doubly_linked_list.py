# Doubly linked list

from __future__ import annotations


class Node:
    def __init__(
        self,
        data: str | None = None,
        prev_node: Node | None = None,
        next_node: Node | None = None,
    ):
        self.data: str | None = data
        self.prev_node: Node | None = prev_node
        self.next_node: Node | None = next_node


class DoublyLinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None

    def create_node(self, data: str) -> Node:
        return Node(data=data)

    def push(self, data: str) -> None:
        print(f"Pushing {data} into DLL")
        new_node = self.create_node(data)
        if self.is_empty:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
            self.tail = new_node

    def insert_node_at_first(self, data: str) -> None:
        print(f"Inserting {data} at first")
        new_node = self.create_node(data)
        if self.is_empty:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head.prev_node = new_node
            self.head = new_node

    def insert_node_at_last(self, data: str) -> None:
        print(f"Inserting {data} at last")
        new_node = self.create_node(data)
        if self.is_empty:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
            self.tail = new_node

    def remove_head_node(self) -> None:
        if self.is_empty:
            print("DLL is empty")
            return
        print(f"Removing {self.head.data} from head node")
        current_head_node = self.head
        self.head = current_head_node.next_node
        self.head.prev_node = current_head_node.prev_node

    def remove_tail_node(self) -> None:
        if self.is_empty:
            print("DLL is empty")
            return
        print(f"Removing {self.tail.data} from tail")
        current_tail_node = self.tail
        self.tail = current_tail_node.prev_node
        self.tail.next_node = current_tail_node.next_node

    def remove_node(self, data: str) -> None:
        if self.is_empty:
            print("DLL is empty")
            return
        found = False
        if self.head.data == data:
            found = True
            current_head_node = self.head
            self.head = current_head_node.next_node
            self.head.prev_node = current_head_node.prev_node
            print(f"Removed {data} from head node")
        elif self.tail.data == data:
            found = True
            current_tail_node = self.tail
            self.tail = current_tail_node.prev_node
            self.tail.next_node = current_tail_node.next_node
            print(f"Removed {data} from tail node")
        else:
            currentNode = self.head.next_node
            while currentNode is not None:
                if currentNode.data == data:
                    found = True
                    prev_node = currentNode.prev_node
                    next_node = currentNode.next_node
                    prev_node.next_node = next_node
                    next_node.prev_node = prev_node
                    print(f"{data} is removed from DLL")
                    return
        if not found:
            print(f"{data} is not present in DLL")

    @property
    def is_empty(self) -> bool:
        return self.head == None

    def print_values(self) -> None:
        if self.is_empty:
            print("DLL is empty")
            return

        print("Printing values: ", end=" ")
        currentNode = self.head
        while currentNode is not None:
            print(f"{currentNode.data}", end=" ")
            currentNode = currentNode.next_node
        print()

    def print_reverse(self) -> None:
        if self.is_empty:
            print("DLL is empty")
            return
        print("Printing reverse: ", end=" ")
        currentNode = self.tail
        while currentNode is not None:
            print(f"{currentNode.data}", end=" ")
            currentNode = currentNode.prev_node
        print()


if __name__ == "__main__":
    dll = DoublyLinkedList()

    START = 0
    END = 6

    dll.remove_node(str(19))  # should print DLL is empty

    dll.insert_node_at_last(str(10))

    dll.print_values()

    dll.print_reverse()

    for i in range(START, END):
        dll.push(str(i))

    dll.print_values()

    dll.remove_node(str(10))

    dll.print_values()

    dll.print_reverse()

    dll.remove_node(str(5))

    dll.print_values()

    dll.print_reverse()

    dll.insert_node_at_first(str(9))

    dll.print_values()

    dll.print_reverse()

    dll.remove_head_node()

    dll.print_values()

    dll.print_reverse()

    dll.remove_tail_node()

    dll.print_values()

    dll.print_reverse()
