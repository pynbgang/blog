---
layout: post
title: "Remove Element"
published: true
created:  2020 Feb 19 11:04:01 PM
tags: [python, string, two pointer,lintcode,east]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [Remove Element](https://www.lintcode.com/problem/remove-element/leaderboard)

Given an array and a value, remove all occurrences of that value in place and return the new length.

The order of elements can be changed, and the elements after the new length don't matter.

Example
Example 1:
	Input: [], value = 0
	Output: 0


Example 2:
	Input:  [0,4,4,0,0,2,4,4], value = 4
	Output: 4
	
	Explanation: 
	the array after remove is [0,0,0,2]


## ideas

1. pop
2. pointers

## two pointers

```python
class Solution:
    """
    @param: A: A list of integers
    @param: elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        if len(A)==1 and A[0]==elem:
            A.pop()
        i,j = 0,len(A)-1
        while (i <=j):
            if A[i] == elem:
                A.pop(i)
                j-=1
            elif A[j]==elem:
                A.pop(j)
                j-=1
            else:
                i += 1
                j-=1
        return len(A)
```


## one pinter

```python
class Solution:

    def removeElement(self, A, elem):
        i = 0
        L = len(A)
        while i < L:
            if A[i] == elem:
                A.pop(i)
                L = len(A)
            else:
                i += 1
        return len(A)

```



