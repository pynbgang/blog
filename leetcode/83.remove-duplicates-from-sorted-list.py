#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

if 0:  # ping
    class Solution:
        def deleteDuplicates(self, head: ListNode) -> ListNode:
            p = ListNode(-1000); p.next = head
            while p.next:
                while p.next and p.val == p.next.val:
                    p.next = p.next.next
                if p.next:
                    p = p.next
            return head


if 0:  # ping
    class Solution:
        def deleteDuplicates(self, head: ListNode) -> ListNode:
            p = ListNode(-1000); p.next = head
            while p.next:
                if p.val==p.next.val:
                    p.next=p.next.next
                else:
                    p=p.next
            return head

if 0:  # lmv
    class Solution:
        def deleteDuplicates(self, head: ListNode) -> ListNode:
            cur = head
            while cur:
                while cur.next and cur.next.val == cur.val:
                    cur.next = cur.next.next     # skip duplicated node
                cur = cur.next     # not duplicate of current node, move to next node
            return head
# @lc code=end
