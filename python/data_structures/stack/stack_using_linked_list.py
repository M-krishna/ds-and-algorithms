from __future__ import annotations


class StackNode:
    def __init__(self, data: str | None = None, node: StackNode | None = None):
        self.data = data
        self.next = node


class Stack:
    def __init__(self):
        self.head = None

    def create_stack_node(self, data) -> StackNode:
        return StackNode(data)

    @property
    def is_empty(self) -> bool:
        return self.head == None

    def push(self, data: str) -> None:
        new_node = self.create_stack_node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Inserted {data} to Stack")

    def pop(self) -> None:
        if self.is_empty:
            print("Stack is empty")
            return
        head = self.head
        self.head = head.next
        print(f"{head.data} popped successfully")

    def peak(self) -> None:
        print(f"Peak: {self.head.data}")

    def print_values(self) -> None:
        if self.is_empty:
            print("Stack is empty")
            return

        head = self.head
        while head is not None:
            print(f"{head.data}", end=" ")
            head = head.next
        print()


if __name__ == "__main__":
    stack = Stack()

    # push to stack
    for i in range(0, 6):
        stack.push(str(i))

    # peak
    stack.peak()  # should print 5

    # pop
    stack.pop()  # should return 5

    # print values
    stack.print_values()

    # pop
    stack.pop()  # should return 4

    # peak
    stack.peak()  # should print 3

    stack.print_values()
