'''
Find cycle in a linked list.

I/P: 1->2->3->1->NULL
O/P: True
Explanation: Here the values represents nodes, not the actual value inside the node.
We can see that the node 3 points to node 1 meaning it has a cycle

I/P: 1->2->3->4->NULL
O/P: False
'''

from __future__ import annotations


class SinglyLinkedListNode:
    def __init__(self, data: int, node: SinglyLinkedListNode=None) -> None:
        self.data = data
        self.next = node


class Solution:
    def hasCycle(self, head: SinglyLinkedListNode) -> bool:
        slowPointer = head
        fastPointer = head

        while slowPointer and fastPointer and fastPointer.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
            
            if slowPointer == fastPointer:
                return True
        return False


if __name__ == "__main__":
    head = SinglyLinkedListNode(1)
    head.next = SinglyLinkedListNode(2)
    head.next.next = SinglyLinkedListNode(3)
    head.next.next.next = SinglyLinkedListNode(4)

    s1 = Solution()
    print(s1.hasCycle(head))

    head1 = SinglyLinkedListNode(1)
    head1.next = SinglyLinkedListNode(2)
    head1.next.next = SinglyLinkedListNode(3)
    head1.next.next.next = head1.next.next

    s2 = Solution()
    print(s2.hasCycle(head1))