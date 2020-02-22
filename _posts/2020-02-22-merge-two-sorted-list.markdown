---
layout: post
title: "merge two sorted list"
published: true
created:  2020 Feb 22 11:32:45 AM
tags: [python, list, leetcode, easy]
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

Python
```
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
