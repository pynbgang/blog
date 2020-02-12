---
layout: post
title: "Longest Consecutive Sequence"
published: true
created:  2020 Feb 09 11:02:29 AM
tags: [list, python, brute force, hard, easy, set]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [Longest Consecutive Sequence](https://www.interviewbit.com/problems/longest-consecutive-sequence/)

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Example:
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.


## Owen

```python
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        if not A:
            return 0
        if len(A)==1:
            return 1
        B=list(set(list(A)))
        B.sort()
        dp=[1]*len(B)
        for i in range(1,len(B)):
            if B[i]-B[i-1]<=1:
                dp[i]=dp[i-1]+1
        return max(dp)
"""
||   ✔ Accepted
||   ✔ 68/68 cases passed (60 ms)
||   ✔ Your runtime beats 43.04 % of python3 submissions
||   ✔ Your memory usage beats 96.3 % of python3 submissions (13.8 MB)
"""
```

- within DP ,then return max value in this dp list

owen solution shortened (ping):

```python
class Solution:
    def longestConsecutive(self, A: List[int]) -> int:
        A=sorted(list(set(list(A))))
        dp=[1]*len(A)
        for i in range(1,len(A)):
            if A[i]-A[i-1]==1:
                dp[i]=dp[i-1]+1
        return max(dp or [0])
```

# ping

this is [leetcode 128](https://leetcode.com/problems/longest-consecutive-sequence/description/)

## brute force: initial: timeout

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxcount = 0

        for i in nums:

            count = 0
            i1 = i

            print("take i:", i)
            while i in nums:
                i += 1
                count += 1
            else:
                print("not in nums")

            print("take i-1:", i1-1)
            while i1-1 in nums:
                i1 -= 1
                count += 1
            else:
                print("not in nums")

            maxcount = max(count, maxcount)

        return maxcount
```


## brute force1: extra set to record checked

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxcount, checked = 0, set()

        for i in nums:

            count = 0
            i1 = i

            if i not in checked:
                print("take i:", i)
                while i in nums:
                    i += 1
                    count += 1
                    checked.add(i)

                print("take i-1:", i1-1)
                while i1-1 in nums:
                    i1 -= 1
                    count += 1
                    checked.add(i1)

            maxcount = max(count, maxcount)

        return maxcount
"""
||   ✔ Accepted
||   ✔ 68/68 cases passed (56 ms)
||   ✔ Your runtime beats 66.84 % of python3 submissions
||   ✔ Your memory usage beats 7.41 % of python3 submissions (14.8 MB)
"""
```

## brute force2: list to set to remove dup

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxcount, checked = 0, set()

        nums=set(nums)
        for i in nums:

            count = 0
            i1 = i

            if i not in checked:
                print("take i:", i)
                while i in nums:
                    i += 1
                    count += 1
                    checked.add(i)

                print("take i-1:", i1-1)
                while i1-1 in nums:
                    i1 -= 1
                    count += 1
                    checked.add(i1)

            maxcount = max(count, maxcount)

        return maxcount

"""
||   ✔ Accepted
||   ✔ 68/68 cases passed (56 ms)
||   ✔ Your runtime beats 66.84 % of python3 submissions
||   ✔ Your memory usage beats 7.41 % of python3 submissions (14.8 MB)
"""
```

## brute force3: use set.remove, no extra set

this is almost same as lmv

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxcount, nums = 0, set(nums)
        while nums:
            i1 = i = nums.pop()
            count = 1

            while i+1 in nums:
                count += 1
                nums.remove(i+1)
                i += 1

            while i1-1 in nums:
                count += 1
                nums.remove(i1-1)
                i1 -= 1

            maxcount = max(count, maxcount)

        return maxcount
"""
||   ✔ Accepted
||   ✔ 68/68 cases passed (64 ms)
||   ✔ Your runtime beats 31.28 % of python3 submissions
||   ✔ Your memory usage beats 100 % of python3 submissions (13.7 MB)
"""
```

## lmv

```python
class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        num=set(num)
        maxLen=0
        while num:
            n=num.pop()
            i=n+1
            l1=0
            l2=0
            while i in num:
                num.remove(i)
                i+=1
                l1+=1
            i=n-1
            while i in num:
                num.remove(i)
                i-=1
                l2+=1
            maxLen=max(maxLen,l1+l2+1)
        return maxLen
    """
    ||   ✔ Accepted
    ||   ✔ 68/68 cases passed (52 ms)
    ||   ✔ Your runtime beats 86.48 % of python3 submissions
    ||   ✔ Your memory usage beats 96.3 % of python3 submissions (13.8 MB)
    """
```

## tips:

* use set to remove dup from list
* use set to speed up `in`
* use set.pop and set.remove to update `in-place`
* the `for i in x` hell (comparing with `while i in x`):
  - `for i in x`, updating in x won't affect the iterated items.
  - `while i in x`, updating x will affact the progress
