from __future__ import annotations


class QueueNode:
    def __init__(self, data: str | None = None, nextNode: QueueNode | None = None):
        self.data = data
        self.next = nextNode


class Queue:
    def __init__(self):
        self.head = None

    def create_node(self, data: str) -> QueueNode:
        return QueueNode(data=data)

    @property
    def is_empty(self) -> bool:
        return self.head == None

    def enqueue(self, data: str) -> None:
        print(f"Enqueue: {data}")
        if not self.head:
            self.head = self.create_node(data)
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = self.create_node(data)

    def dequeue(self) -> None:
        head = self.head
        self.head = self.head.next
        print(f"Dequeued: {head.data}")

    def peak(self) -> None:
        if self.is_empty:
            print("Queue is empty")
            return
        print(f"Peak: {self.head.data}")

    def print_values(self) -> None:
        if self.is_empty:
            print("Queue is empty")
            return
        print("Items in Queue: ", end=" ")
        head = self.head
        while head is not None:
            print(f"{head.data}", end=" ")
            head = head.next
        print()


if __name__ == "__main__":
    queue = Queue()

    START = 0
    END = 6

    for i in range(START, END):
        queue.enqueue(str(i))

    for _ in range(START, END):
        queue.print_values()
        queue.dequeue()
