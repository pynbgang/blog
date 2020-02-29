---
layout: post
title: "Best Sightseeing Pair"
published: true
created:  2020 Feb 26 02:45:47 PM
tags: [python, list, leetcode, medium]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [Best Sightseeing Pair](https://leetcode.com/problems/best-sightseeing-pair/)

    || Given an array A of positive integers, A[i] represents the value of the i-th
    || sightseeing spot, and two sightseeing spots i and j have distance j - i between
    || them.
    ||
    || The score of a pair `(i < j)` of sightseeing spots is `(A[i] + A[j] + i - j)`:
    || the sum of the values of the sightseeing spots, minus the distance between
    || them.
    ||
    || Return the maximum score of a pair of sightseeing spots.
    ||
    ||Example 1:
    ||
    ||Input: [8,1,5,2,6]
    ||Output: 11
    ||

## Owen - find the max from end

```python
class Solution(object):
    def maxScoreSightseeingPair(self, A):
        len1,l2,temp=len(A),[0]*(len(A)-1)+[A[-1]+1-len(A)],0
        for i in range(len1-2,0,-1):
            l2[i]=max(A[i]-i,l2[i+1])
        for i in range(len1-1):
            temp=max(temp,A[i]+i+l2[i+1])
        return temp
```

## ping: brute force

```python
class Solution:  # ping: brute force: timeout
    import sys
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        max1 = -sys.maxsize-1
        for i in range(len(A)-1):
            for j in range(i+1, len(A)):
                max1 = max(A[i]+A[j]+i-j, max1)
        return max1
```

## lmv

```python
class Solution:
    """
    https://leetcode.com/problems/best-sightseeing-pair/discuss/400283

    * Lang:    python3
    * Author:  junaidmansuri
    * Votes:   0
    """

    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        maxi = max1 = 0
        for j in range(1, len(A)):
            maxi = max(maxi, A[i]+i)
            max1 = max(max1, maxi+A[j]-j)
        return max1
```

## idea

    A[i]+A[j]+i-j = 
    A[i]+i + A[j]-j
    ------   ------

for any j, maintain a maxi (A[i]+i), and max res **for current j** is maxi+A[j]-j
final res is max of all these max


