---
layout: post
title: "[541] Reverse String II"
published: true
created:  2020 Apr 13 12:16:56 PM
tags: [python, leetcode, easy, recursion]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[541] Reverse String II](https://leetcode.com/problems/reverse-string-ii/)

    || https://leetcode.com/problems/reverse-string-ii/description/
    || 
    || * algorithms
    || * Easy (47.13%)
    || * Likes:    377
    || * Dislikes: 1094
    || * Total Accepted:    81.5K
    || * Total Submissions: 170.9K
    || * Testcase Example:  '"abcdefg"\n2'
    || * Source Code:       541.reverse-string-ii.py
    || 
    || Given a string and an integer k, you need to reverse the first k
    characters for every 2k characters counting from the start of the string.
    If there are less than k characters left, reverse all of them. If there are
    less than 2k but greater than or equal to k characters, then reverse the
    first k characters and left the other as original.
    || 
    || Example:
    || 
    || Input: s = "abcdefg", k = 2
    || Output: "bacdfeg"
    || 
    || Restrictions: 
    || 
    || ⁠The string consists of lower English letters only.
    || ⁠Length of the given string and k will in the range [1, 10000]

## Owen: follow basic rules

```python
class Solution(object):
    def reverseStr(self, s, k):
        if len(s)==1:return s
        if k==0:return s
        if k==len(s):return s[::-1]
        m=len(s)/k
        l=[]
        for i in range(m):
            l.append(s[i*k:(i+1)*k])
        l.append(s[m*k:])
        str1=""
        for i in range(len(l)):
            if i%2==0:str1+=l[i][::-1]
            else:str1+=l[i]
        return str1
        """
```

## owen: recursion

```python
class Solution(object):
    def reverseStr(self, s, k):
        if s=="" ：return ""
        return s[0:k][::-1] + s[k:2*k] + self.reverseStr(s[2*k:], k) 
```

## ping: brute force

```python
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        return "".join(s[i:i+k][::-1] + s[i+k:i+2*k] for i in range(0, len(s), 2*k))

	"""
        ||   ✔ Accepted
        ||   ✔ 60/60 cases passed (48 ms)
        ||   ✔ Your runtime beats 12.2 % of python3 submissions
        ||   ✔ Your memory usage beats 14.29 % of python3 submissions (13.6 MB)
	"""
```

    #a b c d e f g
    #0 1|2 3|4 5 6
    #    k   2k
    #i       i
