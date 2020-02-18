---
layout: post
title: "Max Distance"
published: true
created:  2020 Feb 17 11:04:01 AM
tags: [leetcode,python,list,two pointers,easy,amazon,interviewbit,brute force]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [Max Distance](https://www.interviewbit.com/problems/max-distance/)

Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] `<=` A[j].
If there is no solution possible, return -1.


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

S = Solution()
A=[1,2,3]
S.maximumGap(A)


## tips

- it is not the best way,can not pass all the test cases.

## ping: brute force

time exceeded

```python
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        max1 = -1
        for i in range(len(A)-1, -1, -1):
            for j in range(i+1):
                if A[i] >= A[j]:
                    max1 = max(max1, (i-j))
                    break
        return max1
```

