---
layout: post
title: "[1836] remove duplicates from unsorted list"
published: true
created:  2019 Dec 30 01:08:48 AM
tags: [python, lintcode, linkedlist, easy]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [remove-duplicates-from-unsorted-list](https://www.lintcode.com/problem/remove-duplicates-from-unsorted-list/description?_from=ladder&&fromId=99)

```python
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The first node of linked list.
    @return: Head node.
    """
    def removeDuplicates(self, head):
        # write your code here
        d={}    # count each node values

        # if no node or just one node, nothing to do
        if not head or not head.next: return head

        # if there are at least 2 nodes, count first node
        p=head; d[head.val]=1
        # and keep checking next node
        while p.next:
            # count next node value
            d[p.next.val]=d.get(p.next.val,0)+1
            # if next node is seen, skip it
            if d[p.next.val]>=2:
                p.next=p.next.next
            else:
                p=p.next
        return head
```

