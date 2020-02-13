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

# posted: remove-duplicates-from-sorted-list

https://www.lintcode.com/problem/remove-duplicates-from-sorted-list/description?_from=ladder&&fromId=99

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
    @param head: head is the head of the linked list
    @return: head of linked list
    """
    def deleteDuplicates(self, head):
        # write your code here

        ##either give condition:
        #if not head: return head
        #p=head

        ##or use dummy head
        p=ListNode(0, head)

        while p.next:
            if p.val==p.next.val:
                p.next=p.next.next
            else:
                p=p.next
        return head
```

keys:

- use dummy head to simplify conditions
- use while p.next to iterate a list

