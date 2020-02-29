#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = p = ListNode(0); dummy.next=head
        while p.next:
            if p.next.val is val:
                p.next=p.next.next
            else:
                p=p.next
        return dummy.next
# @lc code=end
