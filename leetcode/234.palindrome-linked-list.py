#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:     # convert to a list, ON, ON
    def isPalindrome(self, head: ListNode) -> bool:
        allvalue = []
        while head:
            allvalue.append(head.val)
            head = head.next
        return allvalue == allvalue[::-1]

def isPalindrome(self, head):
    rev, slow, fast = None, head, head
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next
    while rev and rev.val == slow.val:
        slow = slow.next
        rev = rev.next
    return not rev

"""
   None     head    ->  node1  ->  node2   ->   node3   ->  node4   ->  None

phaseI: create a reverse linke list for 1st half

   rev      fast/slow
                                   fast
     <----- rev         slow

                                                             fast

              <-------- rev        slow

                                                 slow
phaseII: compare 1st half(reversed linked list) and 2nd half(original linked l)

                          ^------------------------^
              rev                                            slow

   rev                                                                  rev

"""

# @lc code=end
