---
layout: post
title: "swap-two-nodes-in-linked-list"
subtitle: "abc"
date: 2019-12-30
author: "ping"
tags: 
    - LinkedList
    - dict
    - lintcode
    - medium
    - python
    - dayoushi
created:  2019 Dec 29 11:53:49 PM
categories: [tech]
published: true

---


TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [swap-two-nodes-in-linked-list](https://www.lintcode.com/problem/swap-two-nodes-in-linked-list/description?_from=ladder&&fromId=99)

## 古人云

![image](https://user-images.githubusercontent.com/2038044/71569321-4048d080-2a9c-11ea-8832-55b0c9b02958.png)
![image](https://user-images.githubusercontent.com/2038044/71569303-18596d00-2a9c-11ea-9121-683edd653e8c.png)

古人云： 重提kb九月末，空叹流年不禁过

## mine (swap value only)


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
    @param head: a ListNode
    @param v1: An integer
    @param v2: An integer
    @return: a new head of singly-linked list
    """
    def swapNodes(self, head, v1, v2):
        # write your code here
        p, q, r=None,None,head
        while r:
            if r.val==v1: p=r
            if r.val==v2: q=r
            r=r.next
        if p and q:
            p.val, q.val=v2, v1
        return head
```

## mine

```python
class Solution:
    """
    @param head: a ListNode
    @param v1: An integer
    @param v2: An integer
    @return: a new head of singly-linked list
    """
    def swapNodes(self, head, v1, v2):
        # write your code here
        if not head: return None

        dummy=r=ListNode(-1000,head)
        p=q=None

        #iterate to find pre-nodes (p, q) of the 2 nodes(v1, v2)
        while r.next:
            if r.next.val==v1: p=r
            if r.next.val==v2: q=r
            r=r.next

        # if both found, check 3 conditions:
        # nodes are adjacent: 
        #    -x-v1-v2-y; 
        #    -x-v2-v1-y;  
        # nodes are not adjacent:
        #    -x-v1-y-v2-z-
        #    -x-v1-y1-y2-v2-z- (no diff)

        def swapAdjNodes(p, q):
            # name the 3 positions:
            # -p-pnode-qnode-qnext-
            pnode=q
            qnode=q.next
            qnext=qnode.next

            #swap
            p.next=qnode
            qnode.next=pnode
            pnode.next=qnext

        if p and q:
            if p.next is q:   swapAdjNodes(p,q)
            elif q.next is p: swapAdjNodes(q,p)
            else:
                # name the 4 positions: 
                # -p-pnode-pnext-//-q-qnode-qnext-
                pnode=p.next
                pnext=pnode.next
                qnode=q.next
                qnext=qnode.next

                #swap
                p.next=qnode
                qnode.next=pnext
                q.next=pnode
                pnode.next=qnext
        return dummy.next
```

## zhangba

```python
class Solution:
    # @param {ListNode} head, a ListNode
    # @oaram {int} v1 an integer
    # @param {int} v2 an integer
    # @return {ListNode} a new head of singly-linked list
    def swapNodes(self, head, v1, v2):
        if head is None:
            return None
        dummy = ListNode(0)
        dummy.next = head
        prev1, prev2 = self.findPrevs(dummy, v1, v2)
        if prev1 is None or prev2 is None:
            return head
        if prev1 == prev2:
            return head
        if prev1.next == prev2:
            self.swapAdjcent(prev1)
        elif prev2.next == prev1:
            self.swapAdjcent(prev2)
        else:
            self.swapRemote(prev1, prev2)
        return dummy.next
    # head->...->prev1->v1->...->prev2->v2...
    # return prev1 & prev2
    def findPrevs(self, dummy, v1, v2):
        prev1, prev2 = None, None
        node = dummy
        while node.next is not None:
            if node.next.val == v1:
                prev1 = node
            if node.next.val == v2:
                prev2 = node
            node = node.next
        return prev1, prev2
    # dummy->head->..->prev->node1->node2->post...
    # swap node1 & node2
    def swapAdjcent(self, prev):
        node1 = prev.next
        node2 = node1.next
        post = node2.next
        prev.next = node2
        node2.next = node1
        node1.next = post
    # dummy->head->..->prev1->node1->post1->...->prev2->node2->post2...
    # swap node1 & node2
    def swapRemote(self, prev1, prev2):
        node1 = prev1.next
        post1 = node1.next

        node2 = prev2.next
        post2 = node2.next

        prev1.next = node2
        node2.next = post1

        prev2.next = node1
        node1.next = post2
```


## jj1

```python
class Solution:
    """
    @param head: a ListNode
    @param v1: An integer
    @param v2: An integer
    @return: a new head of singly-linked list
    """
    def swapNodes(self, head, v1, v2):
        # write your code here
        if v1 == v2: return head

        dummy = p = ListNode(0, head)

        d = {v1: None, v2: None}
        while p.next:
            if p.next.val == v1 or p.next.val == v2:
                d[p.next.val] = p 
            p = p.next
        if not all(d.values()):
            return dummy.next

        v1n, v2n = d[v1].next, d[v2].next

        if v1n == d[v2] or v2n == d[v1]:
            p = d[v1] if d[v2] == v1n else d[v2]
            temp = p.next
            p.next = p.next.next
            temp.next = temp.next.next
            p.next.next = temp
        else:
            d[v1].next = d[v1].next.next
            d[v2].next = d[v2].next.next
            v1n.next = d[v2].next
            d[v2].next = v1n
            v2n.next = d[v1].next
            d[v1].next = v2n
        return dummy.next
```

keys:

- all
- d.values 
- temp is must, otherwise loop (next to self)

## jj2 (best)

```python
class Solution:
    """
    @param head: a ListNode
    @param v1: An integer
    @param v2: An integer
    @return: a new head of singly-linked list
    """
    def swapNodes(self, head, v1, v2):
        # write your code here
        dummy = p = ListNode(0, head)
        d = {v1: None, v2: None}
        while p.next:
            if p.next.val == v1 or p.next.val == v2:
                d[p.next.val] = p 
            p = p.next
        if not d[v1] or not d[v2] or d[v1] is d[v2]:
            return dummy.next
        d[v1].next, d[v2].next = d[v2].next, d[v1].next
        d[v1].next.next, d[v2].next.next = d[v2].next.next, d[v1].next.next
        return dummy.next
```

## jj2 illustration

![image](https://user-images.githubusercontent.com/2038044/71566077-6cefee80-2a82-11ea-8aee-80b2a98aa669.png)
![image](https://user-images.githubusercontent.com/2038044/71566084-7aa57400-2a82-11ea-8181-96bdd477f637.png)
![image](https://user-images.githubusercontent.com/2038044/71566088-85600900-2a82-11ea-8295-77856fee6d06.png)
![image](https://user-images.githubusercontent.com/2038044/71566487-1d132680-2a86-11ea-83ff-040e637169a8.png)

