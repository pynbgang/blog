---
layout: post
title: "[686] Repeated String Match"
published: true
created:  2020 May 12 12:16:56 PM
tags: [python, leetcode, easy, math]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[686] Repeated String Match](https://leetcode.com/problems/repeated-string-match/description/)

    || * algorithms
    || * Easy (32.02%)
    || * Likes:    726
    || * Dislikes: 697
    || * Total Accepted:    88.3K
    || * Total Submissions: 274.5K
    || * Testcase Example:  '"abcd"\n"cdabcdab"'
    || * Source Code:       686.repeated-string-match.py
    || 
    || Given two strings A and B, find the minimum number of times A has to be
    repeated such that B is a substring of it. If no such solution, return -1.
    || 
    || For example, with A = "abcd" and B = "cdabcdab".
    || 
    || Return 3, because by repeating A three times (“abcdabcdabcd”), B is a
    substring of it; and B is not a substring of A repeated two times
    ("abcdabcd").
    || 
    || Note:
    || The length of A and B will be between 1 and 10000.

## Owen: similar with lmv

```python
class Solution(object):
    def repeatedStringMatch(self, A, B):
        temp = 1
        while (1):
            str1 = A * temp
            if B in str1: return temp
            temp += 1
            if temp > len(B) / len(A) + 2: return -1
        """
        Runtime: 140 ms, faster than 41.43% of Python online submissions for Repeated String Match.
        Memory Usage: 13.2 MB, less than 6.67% of Python online submissions for Repeated String Match.
        """
```

## ping: brute force

```python
class Solution:     #ping: brute force, passed
    def repeatedStringMatch(self, A: str, B: str) -> int:
        for i in range(1, len(B) // len(A) + 5):
            if B in A * i: return i
        return -1
        """
        ✔ Accepted
        ✔ 55/55 cases passed (696 ms)
        ✔ Your runtime beats 5.07 % of python3 submissions
        ✔ Your memory usage beats 5.55 % of python3 submissions (14.1 MB)
        """
```

## lmv: len(B)//len(A) + 2

```python
class Solution:     #lmv
    def repeatedStringMatch(self, A: str, B: str) -> int:
        """
        https://leetcode.com/problems/repeated-string-match/discuss/330741

        * Lang:    python3
        * Author:  junaidmansuri
        * Votes:   3
        """
        if not set(B).issubset(set(A)): return -1
        for i in range(1, len(B) // len(A) + 3):
            if B in A * i: return i
        return -1
        """
        ✔ Accepted
        ✔ 55/55 cases passed (32 ms)
        ✔ Your runtime beats 96.17 % of python3 submissions
        ✔ Your memory usage beats 5.55 % of python3 submissions (13.9 MB)
        """
```

## takeaways/tips

* "abc" * 2
* setA.issubset
