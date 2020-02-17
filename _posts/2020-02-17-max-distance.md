---
layout: post
title: "Max Distance"
published: true
created:  2020 Feb 17 11:04:01 AM
tags: [leetcode, python,list,tow pointer,easy,Amazon]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -
## Max Distance

### https://www.interviewbit.com/problems/max-distance/

```python
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        if not A :return -1
        if len(set(A))==1 and len(A)!=1:
            return len(A)-1
        if len(A)==1:return 0
        lenth=len(A)
        l,r=0,lenth-1
        temp=0
        while (l<r):
            if A[l]>max(A[l+1:r+1]) :
                l+=1
            elif A[l]<=A[r]:
                temp=max(temp,r-l)
                l+=1
                r=lenth-1
            else:
                r-=1
        return temp
```
