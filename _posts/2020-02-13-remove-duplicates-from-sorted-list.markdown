---
layout: post
title: "remove-duplicates-from-sorted-list"
published: true
date: 2020-02-12
created:  2020 Feb 13 02:55:44 PM
tags: [python, linkedlist, easy, lintcode]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [remove-duplicates-from-sorted-list](https://www.lintcode.com/problem/remove-duplicates-from-sorted-list/description?_from=ladder&&fromId=99)

also see [leetcode](https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/)

|| Given a sorted linked list, delete all duplicates such that each element appear only once.
|| 
|| Example 1:
|| 
|| 
|| Input: 1->1->2
|| Output: 1->2
|| 
|| 
|| Example 2:
|| 
|| 
|| Input: 1->1->2->3->3
|| Output: 1->2->3
|| 
|| 
|| [Finished in 3 seconds]


## code

```python
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

if 0:  # ping
    class Solution:
        def deleteDuplicates(self, head: ListNode) -> ListNode:
            """
            @param head: head is the head of the linked list
            @return: head of linked list
            """

            ##either give condition:
            #if not head: return head
            #p=head

            ##or use dummy head
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

```

## tips:

- use dummy head to simplify conditions
- use while p.next to iterate a list

