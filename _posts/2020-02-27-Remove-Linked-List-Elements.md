---
layout: post
title: "Remove Linked List Elements"
published: true
created:  2020 Feb 27 02:45:47 PM
tags: [python, linked list, leetcode, easy]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/)

||Remove all elements from a linked list of integers that have value val.em.                                                                         
||Example:                                                                                                                                          
||Input:  1->2->6->3->4->5->6, val = 6                                      
||Output: 1->2->3->4->5                                                                                                                                                                                                                                                                                                                                                                                     
||Example 1:                                                                                                                                                        
||                                                                                                                                                                  
||Input: [8,1,5,2,6]                                                                                                                                                
||Output: 11                                                                                                                                                        
||                                                                                                                                                                                                                                                                                                                                                                                                                                          

## Owen - fast/slow pointers 

```python
class Solution(object):
    def removeElements(self, head, val):
        if not head:
            return None
        if head.val==val:
            return self.removeElements(head.next, val)
        i,j=head,head.next
        while(j):
            if j.val==val and not j.next:
                i.next=None
                break
            elif j.val==val and j.next:
                j=j.next
                i.next=j
            else:
                i=i.next
                j=j.next
        return headp
```




