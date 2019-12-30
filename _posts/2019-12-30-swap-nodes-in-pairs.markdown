---
layout: post
title: "swap-nodes-in-pairs"
published: true
created:  2019 Dec 30 12:54:53 AM
tags: [python, lintcode, LinkedList, easy]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [swap-nodes-in-pairs](https://www.lintcode.com/problem/swap-nodes-in-pairs/description?_from=ladder&&fromId=99)

## mine

```python
class Solution:
    """
    @param head: a ListNode
    @return: a ListNode
    """
    def swapPairs(self, head):
        # write your code here

        # dummy head and pointer p: node before the pair nodes to be swapped

        dummy=p=ListNode(-1000, head)

        #adjacent node pair to be swapped
        a=dummy.next
        b=a.next if a else None

        # swap only when both nodes in pair exist:
        while a and b:
            # swap
            a.next=b.next
            b.next=a
            p.next=b

            # move the 3 pointers ahead
            p=a
            a=a.next
            b=a.next if a else None
        return dummy.next    
```

## jiuzhang

```python
class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        # Write your code here
        if head == None or head.next == None:
            return head
        p = dummy = ListNode(0); dummy.next = head
        while p.next and p.next.next:
            tmp = p.next.next
            p.next.next = tmp.next
            tmp.next = p.next
            p.next = tmp
            p = p.next.next
        return dummy.next
```

## jj (best)

```python
class Solution:
    """
    @param head: a ListNode
    @return: a ListNode
    """
    def swapPairs(self, head):
        # write your code here
        dummy = p = ListNode(0, head)
        while head and head.next:
            p.next = head.next
            head.next = head.next.next
            p.next.next = head
            p = head
            head = head.next
        return dummy.next
```

