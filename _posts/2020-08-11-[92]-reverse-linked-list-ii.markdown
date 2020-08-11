---
layout: post
title: "[92] Reverse Linked List II"
published: true
created:  2020 Aug 11 01:22:32 PM
tags: [python, leetcode, medium]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[92] Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/description/)

    || * algorithms
    || * Medium (37.10%)
    || * Likes:    2513
    || * Dislikes: 147
    || * Total Accepted:    279.6K
    || * Total Submissions: 719.8K
    || * Testcase Example:  '[1,2,3,4,5]\n2\n4'
    || * Source Code:       92.reverse-linked-list-ii.py
    || 
    || Reverse a linked list from position m to n. Do it in one-pass.
    || 
    || Note: 1 ≤ m ≤ n ≤ length of list.
    || 
    || Example:
    || 
    || 
    || Input: 1->2->3->4->5->NULL, m = 2, n = 4
    || Output: 1->4->3->2->5->NULL

# owen

```python
class Solution(object):
    def reverseBetween(self, head, m, n):
        if not head:return None
        l=[]
        while head:
            l.append(head)
            head=head.next
        l1=[l[i] for i in range(m-1,n)]
        l1.reverse()
        temp=l[0:m-1]+l1+l[n:]
        for i in range(len(temp)-1):
            temp[i].next=temp[i+1]
        temp[-1].next=None
        return temp[0]
```

# jj

```python
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        res = p = ListNode(0, head)
        for _ in range(m - 1):
            p = p.next
        h, t, r = p, p.next, p.next
        for _ in range(n - m + 1):
            temp, r = r, r.next
            temp.next = h
            h = temp
        p.next, t.next = h, r
        return res.next
```

