'''
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: list1 = [], list2 = []
Output: []

Input: list1 = [], list2 = [0]
Output: [0]
'''

from __future__ import annotations
from typing import Optional

class SingleLinkedListNode:
    def __init__(self, data: int, node: SingleLinkedListNode = None) -> None:
        self.data = data
        self.next = node


class Solution:
    def mergeTwoListsUsingExtraSpace(self, list1: Optional[SingleLinkedListNode], list2: Optional[SingleLinkedListNode]) -> Optional[SingleLinkedListNode]:
        # Time complexity: O(list1 + list2)
        # Space complexity: O(list1 + list2)
        dummy = SingleLinkedListNode(data=0)
        tail = dummy

        while list1 and list2:
            if list1.data > list2.data:
                tail.next = list1
                list2 = list2.next
            else:
                tail.next = list1
                list1 = list1.next
            
            tail = tail.next

        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        return dummy.next
    
    def mergeTwoListsInPlace(self, list1: Optional[SingleLinkedListNode], list2: Optional[SingleLinkedListNode]) -> Optional[SingleLinkedListNode]:
        # Time complexity: O(list1 + list2)
        # Space complexity: O(1)

        # Base cases
        if not list1: return list2
        if not list2: return list1

        if list1.data > list2.data:
            list1, list2 = list2, list1

        res = list1

        while list1 and list2:
            tmp = None
            while list1 and list1.data <= list2.data:
                tmp = list1
                list1 = list1.next
            tmp.next = list2

            # Swap
            list1, list2 = list2, list1
        return res


if __name__ == "__main__":
    node1 = SingleLinkedListNode(data=1)
    node1.next = SingleLinkedListNode(data=2)
    node1.next.next = SingleLinkedListNode(data=3)

    node2 = SingleLinkedListNode(data=3)
    node2.next = SingleLinkedListNode(data=4)

    # Print list1 data
    tmp1 = node1
    while tmp1:
        print(tmp1.data, end='->')
        tmp1 = tmp1.next
    print()

    # Print list2 data
    tmp2 = node2
    while tmp2:
        print(tmp2.data, end='->')
        tmp2 = tmp2.next
    print()

    # Merge node1 and node2
    sol = Solution()
    result = sol.mergeTwoListsUsingExtraSpace(node1, node2)
    while result:
        print(result.data, end='->')
        result = result.next
    print()

    node1 = SingleLinkedListNode(data=1)
    node1.next = SingleLinkedListNode(data=2)
    node1.next.next = SingleLinkedListNode(data=3)

    node2 = SingleLinkedListNode(data=3)
    node2.next = SingleLinkedListNode(data=4)

    sol1 = Solution()
    result = sol1.mergeTwoListsInPlace(node1, node2)
    while result:
        print(result.data, end='->')
        result = result.next
    print()