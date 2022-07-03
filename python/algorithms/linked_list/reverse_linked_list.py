# Reversing a linked list using different approaches

from __future__ import annotations


class Node:
    def __init__(self, data: int = None):
        self.data: int | None = data
        self.next: Node | None = None


def print_values(head: Node) -> None:
    current_node = head
    while current_node is not None:
        print(f"{current_node.data}", end=" ")
        current_node = current_node.next
    print()


def reverse_linked_list_using_stack(head: Node | None = None) -> Node:
    # store the elements in the stack one by one
    # pop the elements from the stack and link it one by one
    # finally make the next of the last item/node None
    # Time complexity: O(n)
    # Space complexity: O(n)
    stack, temp = [], head

    while temp:
        stack.append(temp)
        temp = temp.next

    head = temp = stack.pop()

    while len(stack) > 0:
        temp.next = stack.pop()
        temp = temp.next

    temp.next = None

    return head


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    print_values(head)

    # Reverse linked list(iterative method)
    # Time complexity: O(n)
    # Auxilary space: O(1)
    prev_node: Node = None
    current_node: Node | None = head
    next_node: Node = None

    while current_node is not None:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node

    head = prev_node  # finally change the head node

    print_values(head)

    head = reverse_linked_list_using_stack(head)
    print_values(head)
