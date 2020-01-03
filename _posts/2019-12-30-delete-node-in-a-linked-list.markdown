---
layout: post
title: "delete-node-in-a-linked-list"
published: true
created:  2019 Dec 30 12:47:06 AM
tags: [python, lintcode, LinkedList, easy]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [delete-node-in-a-linked-list](https://www.lintcode.com/problem/delete-node-in-a-linked-list/description?_from=ladder&&fromId=99)

## zhangba

```python
class Solution:
    """
    @param: node: the node in the list should be deleted
    @return: nothing
    """
    def deleteNode(self, node):
        # write your code here
        if not node or not node.next:
            node = None
            return

        node.val = node.next.val
        node.next = node.next.next
```
