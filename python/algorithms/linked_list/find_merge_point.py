'''
Given pointer to the head nodes of 2 nodes of linked list that merge together at some point,
find the node where the two lists merge. The merge point is where both lists point to the same node,
i.e. they reference the same memory location.

Eg:
[List #1] a--->b--->c
                     \
                      x--->y--->z--->NULL
                     /
     [List #2] p--->q
'''

from __future__ import annotations


class SinglyLinkedListNode:
    def __init__(self, data: int, node: SinglyLinkedListNode=None) -> None:
        self.data = data
        self.next = node


class Solution:
    
    def bruteForceApproach(self, list1: SinglyLinkedListNode, list2: SinglyLinkedListNode) -> int:
        # Compare all the nodes of list1 with all the nodes of list2
        # returns the data of the merge point
        l1 = list1

        while l1:
            l2 = list2
            while l2:
                if l1 == l2:
                    return l1.data
                l2 = l2.next
            l1 = l1.next
        return -1  # if the merge point doesn't exist

        # Time complexity: O(n*m), where n is length of list1 and m is length of list2
        # Space complexity: O(1)


    def optimalSolution(self, list1: SinglyLinkedListNode, list2: SinglyLinkedListNode) -> int:
        # Explanation video: https://www.youtube.com/watch?v=u4FWXfgS8jw

        l1 = list1
        l2 = list2

        while l1 != l2:
            l1 = list2 if l1 is None else l1.next
            l2 = list1 if l2 is None else l2.next
        
        if l1:
            return l1.data
        return -1

        # Time complexity: O(2m) where m is the length of list2. Why 2? Because we are iterating both of them
        # Space complexity: O(1)


if __name__ == "__main__":
    head1 = SinglyLinkedListNode(1)
    head1.next = SinglyLinkedListNode(2)
    head1.next.next = SinglyLinkedListNode(3)
    
    head2 = SinglyLinkedListNode(1)
    head2.next = head1.next.next

    solution = Solution()

    print(solution.bruteForceApproach(head1, head2))
    print(solution.optimalSolution(head1, head2))