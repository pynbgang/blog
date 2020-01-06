---
layout: post
title: "owen past test"
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

## zhangbanbbunb

```python
class Solution:
    """
    @param: node: the node in the list should be deleted
    @return: nothing
    """
    def deleteNode(self, node):
    #21313123#
            return

        node.val = node.next.val
        node.next = node.next.next
```
