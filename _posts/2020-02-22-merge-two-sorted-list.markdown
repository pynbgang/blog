---
layout: post
title: "merge two sorted list"
published: true
created:  2020 Feb 22 11:32:45 AM
tags: [python, linkedlist, leetcode, easy]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[21] Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/description/)

|| * algorithms
|| * Easy (51.03%)
|| * Likes:    3356
|| * Dislikes: 494
|| * Total Accepted:    846.4K
|| * Total Submissions: 1.7M
|| * Testcase Example:  '[1,2,4]\n[1,3,4]'
|| * Source Code:       21.merge-two-sorted-lists.py
|| 
|| Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
|| 
|| Example:
|| 
|| Input: 1->2->4, 1->3->4
|| Output: 1->1->2->3->4->4

## Owen very dummy way

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2 :
            return l1
        l11=[]
        l22=[]
        while(l1):
            l11.append(l1)
            l1=l1.next
        while(l2):
            l22.append(l2)
            l2=l2.next
        l3=l11+l22
        l3.sort(key=lambda x:x.val)
        for i in range(len(l3)-1):
            l3[i].next=l3[i+1]
        l3[-1].next=None
        return l3[0]
```

## ping

```python
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
```

    ||   ✔ Accepted
    ||   ✔ 208/208 cases passed (36 ms)
    ||   ✔ Your runtime beats 62.47 % of python3 submissions
    ||   ✔ Your memory usage beats 100 % of python3 submissions (12.7 MB)


## lmv

    https://leetcode.com/problems/merge-two-sorted-lists/discuss/9735
    * Lang:    python3
    * Author:  caikehe
    * Votes:   383

```python
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
```

# @lc code=end
