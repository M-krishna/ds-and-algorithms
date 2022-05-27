# Basic Stack(LIFO) implementation using List(array)

from __future__ import annotations


class Stack:
    def __init__(self):
        self.items = []  # currently infinite

    def push(self, val: str):
        print(f"Pushing item {val} to the Stack")
        self.items.append(val)

    def pop(self):
        if self.is_empty:
            print("The Stack is empty")
            return
        print("Popped item:", self.items.pop())

    @property
    def is_empty(self) -> bool:
        return len(self.items) == 0

    def peak(self):
        if self.is_empty:
            print("Stack is empty")
            return
        print("Top Element of the Stack:", self.items[len(self.items) - 1])

    def print_values(self):
        if self.is_empty:
            print("Stack is empty")
            return

        print("Items in stack:")
        for item in self.items[::-1]:
            print(item, end=" ")
        print()  # new line


if __name__ == "__main__":
    stack = Stack()

    # Push 5 elements into the Stack
    for i in range(1, 6):
        stack.push(str(i))

    # Print values
    stack.print_values()

    # Peak
    stack.peak()  # Should print 5

    # Pop
    stack.pop()  # should print 5

    # Push
    stack.push("6")

    # Peak
    stack.peak()  # should print 6
