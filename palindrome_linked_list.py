from __future__ import annotations


class ListNode:
    def __init__(self, val: int, next: ListNode | None = None) -> None:
        self.val = val
        self.next = next

class Solution1: # Reverse second half of the list and use two pointers
    def isPalindrome(self, head: ListNode | None) -> bool:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next

        left = head
        right = prev
        while right and left != right:
            if left.val != right.val: return False
            left = left.next
            right = right.next
        return True

class Solution2: # Store values of list in arr and then use two pointers left and right
    def isPalindrome(self, head: ListNode | None) -> bool:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        left = 0
        right = len(arr) - 1
        while left < right:
            if arr[left] != arr[right]:
                return False
            left += 1
            right -= 1

        return True

# Solution 3: Use stack


# EXAMPLE HEAD: 1->2->2->1->None
node3 = ListNode(1)
node2 = ListNode(2, node3)
node1 = ListNode(2, node2)
head = ListNode(1, node1)

solution = Solution1()
print(solution.isPalindrome(head=head))
