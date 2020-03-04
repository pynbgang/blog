---
layout: post
title: "[922] Sort Array By Parity II"
published: true
created:  2020 Mar 04 01:54:43 AM
tags: [python, leetcode, easy, list]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[922] Sort Array By Parity II](https://leetcode.com/problems/sort-array-by-parity-ii/description/)

    || * algorithms
    || * Easy (67.89%)
    || * Likes:    484
    || * Dislikes: 42
    || * Total Accepted:    76.3K
    || * Total Submissions: 112.1K
    || * Testcase Example:  '[4,2,5,7]'
    || * Source Code:       922.sort-array-by-parity-ii.py
    || 
    || Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.
    || Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.
    || 
    || You may return any answer array that satisfies this condition.
    || 
    || Example 1:
    || Input: [4,2,5,7]
    || Output: [4,5,2,7]
    || Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
    || 
    || Note:
    || 
    || 
    || 	2 <= A.length <= 20000
    || 	A.length % 2 == 0
    || 	0 <= A[i] <= 1000

## ping: use extra lists to store even, old

```python
class Solution:     #ping, use 3 extra lists
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        len1, waiteven, even, odd, res, = len(A), 1, [], [], []
        for i in range(len(A)):
            if not A[i] % 2:
                even.append(A[i])
            else:
                odd.append(A[i])
            if even and waiteven:
                res.append(even.pop())
                waiteven = 0
            if odd and not waiteven:
                res.append(odd.pop())
                waiteven = 1
        return res
        """
        ||   ✔ Accepted
        ||   ✔ 61/61 cases passed (236 ms)
        ||   ✔ Your runtime beats 37.76 % of python3 submissions
        ||   ✔ Your memory usage beats 100 % of python3 submissions (14.9 MB)
        """
```

## lmv

```python
class Solution(object):     #lmv: in-place
    def sortArrayByParityII(self, A):
        i, j, len1 = 0, 1, len(A)        # i - even index, j - odd index, len1 - length of A
        while j < len1:                  # (len1 - 1) is odd, j can reach the last element, so this condition is enough
            if A[j] % 2 == 0:            # judge if the value on odd indices is odd
                A[j], A[i] = A[i], A[j]  # if it is even, exchange the values between index j and i
                i += 2                   # even indices get a right value, then i pointer jump to next even index
            else:
                j += 2                   # if it is odd, odd indices get a right value, then j pointer jump to next odd index
        return A
        """
        ||   ✔ Accepted
        ||   ✔ 61/61 cases passed (224 ms)
        ||   ✔ Your runtime beats 68.47 % of python3 submissions
        ||   ✔ Your memory usage beats 86.96 % of python3 submissions (15.2 MB)
        """

        """
        0  1  2  3  4  5
        3  2  3  2  3  2
        i  j
        2<>3
        j  i.
            i  j.
            2<>3
                j  i
        0  1  2  3  4  5
        2  2  3  2  3  3
        i  j
        2<>2
        j  i
        3<>2
        j     i
        2 < > 2
        j           i
        3   <  >    2
                j <>  i
                3     2
        """
```

## ping: in place

```python
class Solution:     #ping, in-place
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        i, j, len1 = 0, 1, len(A)
        while i<len1:
            if A[i] % 2:                #if even pos is odd
                while A[j] % 2:         #check if odd pos is even
                    j += 2              #if no found, keep checking by sliding
                A[i], A[j] = A[j], A[i] #eventually will find one, and swap
            i += 2                      #keep checking next even pos
        return A
```
