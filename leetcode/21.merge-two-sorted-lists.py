#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

if 1:  #ping(per wangmazi class)
    class Solution:
        def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
            res = dummy = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    res.next = l1
                    l1 = l1.next
                else:
                    res.next = l2
                    l2 = l2.next
                res = res.next
            res.next = l1 if l1 else l2
            return dummy.next

    """
    ||   ✔ Accepted
    ||   ✔ 208/208 cases passed (36 ms)
    ||   ✔ Your runtime beats 62.47 % of python3 submissions
    ||   ✔ Your memory usage beats 100 % of python3 submissions (12.7 MB)
    """

if 0:  #lmv

    """
    https://leetcode.com/problems/merge-two-sorted-lists/discuss/9735

    * Lang:    python3
    * Author:  caikehe
    * Votes:   383
    """

    class Solution:
        # iteratively
        def mergeTwoLists1(self, l1, l2):
            dummy = cur = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            cur.next = l1 or l2
            return dummy.next

        # recursively
        def mergeTwoLists2(self, l1, l2):
            if not l1 or not l2:
                return l1 or l2
            if l1.val < l2.val:
                l1.next = self.mergeTwoLists(l1.next, l2)
                return l1
            else:
                l2.next = self.mergeTwoLists(l1, l2.next)
                return l2

        # in-place, iteratively
        def mergeTwoLists(self, l1, l2):
            if None in (l1, l2):
                return l1 or l2
            dummy = cur = ListNode(0)
            dummy.next = l1
            while l1 and l2:
                if l1.val < l2.val:
                    l1 = l1.next
                else:
                    nxt = cur.next
                    cur.next = l2
                    tmp = l2.next
                    l2.next = nxt
                    l2 = tmp
                cur = cur.next
            cur.next = l1 or l2
            return dummy.next

# @lc code=end
