'''
Reverse a doubly linked list and return the head pointer that points to the reversed list

I/P: NULL<-1->2->3->4->NULL
O/P: NULL<-4->3->2->1->NULL
'''

from __future__ import annotations


class DoublyLinkedListNode:
    def __init__(self, data: int, next: DoublyLinkedListNode=None, prev: DoublyLinkedListNode=None) -> None:
        self.data = data
        self.prev = prev
        self.next = next


def reverse(head: DoublyLinkedListNode) -> DoublyLinkedListNode:
    while head:
        head.prev, head.next = head.next, head.prev
        if head.prev is None:
            break
        head = head.prev
    return head


if __name__ == "__main__":
    head = DoublyLinkedListNode(data=1)
    node2 = DoublyLinkedListNode(data=2)
    node3 = DoublyLinkedListNode(data=3) 
    node4 = DoublyLinkedListNode(data=4)

    head.next =  node2
    node2.next = node3
    node3.next = node4

    node2.prev = head
    node3.prev = node2
    node4.prev = node3

    print("Initial order")
    h = head
    while h:
        print(h.data)
        h = h.next

    print("After reversing")
    r = reverse(head)
    while r:
        print(r.data)
        r = r.next