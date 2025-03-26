# Problem: You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
#
# Return the head of the merged linked list.

# Leetcode 21: https://leetcode.com/problems/merge-two-sorted-lists/

from __future__ import annotations

class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None) -> None:
        self.val = val
        self.next = next

# Approach: Similar to merge part of merge sort. Initialize one pointer at the start of each list, and keep adding
# the smaller node in new list.
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        new_list = ListNode()
        curr = new_list

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        if list1:
            curr.next = list1
        if list2:
            curr.next = list2

        return new_list.next
