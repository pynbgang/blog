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

# [[541] Reverse String II](https://leetcode.com/problems/reverse-string-ii/)

    || Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.
    ||                                                                                                                                                   
    || For example, with A = "abcd" and B = "cdabcdab".                                                                                                  
    ||                                                                                                                                                   
    || Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").
    || * Dislikes: 1094
    || * Total Accepted:    81.5K
    || * Total Submissions: 170.9K
    || * Testcase Example:  '"abcdefg"\n2'
    || * Source Code:       541.reverse-string-ii.py
    

## Owen.similary as lmv

```python
class Solution(object):
    def repeatedStringMatch(self, A, B):
        temp=1
        while (1):
            str1=A*temp
            if B in str1:return temp
            temp+=1
            if temp>len(B)/len(A)+2:return -1
            
        """
```

Runtime: 140 ms, faster than 41.43% of Python online submissions for Repeated String Match.
Memory Usage: 13.2 MB, less than 6.67% of Python online submissions for Repeated String Match.
