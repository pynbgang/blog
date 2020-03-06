---
layout: post
title: "[941] Valid Mountain Array"
published: true
created:  2020 Mar 03 12:17:00 PM
tags: [python, leetcode, easy, list, comment]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[941] Valid Mountain Array](https://leetcode.com/problems/valid-mountain-array/description/)

    || * algorithms
    || * Easy (35.53%)
    || * Likes:    275
    || * Dislikes: 59
    || * Total Accepted:    36.9K
    || * Total Submissions: 103.8K
    || * Testcase Example:  '[2,1]'
    || 
    || Given an array A of integers, return true if and only if it is a valid mountain array.
    || 
    || Recall that A is a mountain array if and only if:
    || 
    || 	A.length >= 3
    || 	There exists some i with 0 < i < A.length - 1 such that:
    || 	
    || 		A[0] < A[1] < ... A[i-1] < A[i] 
    || 		A[i] > A[i+1] > ... > A[A.length - 1]
    || 
    || Example 1:
    || Input: [2,1]
    || Output: false
    || 
    || Example 2:
    || Input: [3,5,5]
    || Output: false
    || 
    || Example 3:
    || Input: [0,3,2,1]
    || Output: true
    || 
    || Note:
    || 
    || 	0 <= A.length <= 10000
    || 	0 <= A[i] <= 10000 

## ping: w/o loop

```python
class Solution:     #ping: without loop
    def validMountainArray(self, A: List[int]) -> bool:
        if not A: return False                  #empty list are false
        maxpos = A.index(max(A))                #get peak value
        half1, half2 = A[0:maxpos], A[maxpos:]  #split list in 2 halves with it
        return (
            True if                             #in order to be True Mountain
            len(A) >= 3 and                     #the length has to be 3 or more
            maxpos is not len(A)-1 and          #peak has to be not at end
            maxpos is not 0 and                 # or beginning
            half1 == sorted(half1) and          #first half has to be same as
            len(half1) == len(set(half1)) and   #sorted and no dup, 2nd half
            half2 == sorted(half2, reverse=True) and #same as reversely sorted
            len(half2) == len(set(half2))       # and also no dup
            else False                          # otherwise can't be Mountain
        )
        """
        ||   ✔ Accepted
        ||   ✔ 51/51 cases passed (200 ms)
        ||   ✔ Your runtime beats 99.59 % of python3 submissions
        ||   ✔ Your memory usage beats 5.26 % of python3 submissions (14.6 MB)
        """

## ping: w/ loop

class Solution:     #ping: with loop
    def validMountainArray(self, A: List[int]) -> bool:
        #for (i, j) in zip(range(1, len(A)), range(len(A)-1, 0, -1)):
        i, len1, half1, half2 = 1, len(A), False, False
        while i < len1 and A[i] > A[i-1]:  #set 1st half true if increasing
            half1 = True
            i += 1
        while i < len1 and A[i] < A[i-1]:  #set 2nd half true if decreasing
            half2 = True
            i += 1 #if reach end and both halves are true, then true.
        return True if i == len1 and half1 and half2 else False

        """
        ||   ✔ Accepted
        ||   ✔ 51/51 cases passed (208 ms)
        ||   ✔ Your runtime beats 96.12 % of python3 submissions
        ||   ✔ Your memory usage beats 47.37 % of python3 submissions (14.1 MB)
        """
```

## tip

comment for long lines
