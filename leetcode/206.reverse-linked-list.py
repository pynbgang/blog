#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        next1 = root.next
        next1.next = root

class Solution:     #lmv: 3 pointers
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

"""

1. init:

    prev
    v
    None

        node1(head) -> node2 -> node3 -> None
        ^
        curr

2. first move

    prev
    v
    None
       ^
        \2.curr.next
         \
        node1(head) -x> node2 -> node3 -> None
        ^               ^
        curr            1.next
        ^
        3.prev=curr     4.curr=next

3. 2nd move

    prev
    v
    None
       ^
        \
         \     2.curr.next=prev
          \
        node1(head) <- node2 -> node3 -> None
        ^               ^
        prev            curr
                                1.next
                        3.prev  4.curr

4. last (no move)

    None
       ^
        \
         \
          \
        node1(head) <- node2 <- node3    None
                                ^        ^
                                prev     curr



"""
# @lc code=end
