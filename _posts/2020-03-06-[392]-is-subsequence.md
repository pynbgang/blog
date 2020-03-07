---
layout: post
title: "[392] Is Subsequence"
published: true
created:  2020 Mar 05 10:08:19 PM
tags: [python, leetcode, easy, iter, all, find, exception]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[989] Is Subsequence](https://leetcode.com/problems/is-subsequence/)

    || Given a string s and a string t, check if s is subsequence of t.                                                                                                                                                                                                      
    || You may assume that there is only lower case English letters in both s
    and t. t is potentially a very long (length ~= 500,000) string, and s is a
    short string (<=100).                                                                                               
    ||                                                                                                                                                                                                                                                                       
    || A subsequence of a string is a new string which is formed from the
    original string by deleting some (can be none) of the characters without
    disturbing the relative positions of the remaining characters. (ie, "ace"
    is a subsequence of "abcde" while "aec" is not).
    ||                                                                                                                                                                                                                                                                       
    || Example 1:                                                                                                                                                                                                                                                            
    || s = "abc", t = "ahbgdc"                                                                                                                                                                                                                                               
    ||                                                                                                                                                                                                                                                                       
    || Return true.                                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                          
       Example 2:                                                                                                                                                                                                                                                            
    || s = "axc", t = "ahbgdc"                                                                                                                                                                                                                                               
    ||                                                                                                                                                                                                                                                                       
    || Return false.                                                                                                                                                                                                                                                         

## Owen: str, int

```python
class Solution(object):
    def isSubsequence(self, s, t):
        if not s and t:return True
        i,j=0,0
        while (i<len(s) and j<len(t)):
            if s[i]!=t[j]:
                j+=1
            else:
                i+=1
                j+=1
        if i<len(s):return False
        return True

        """
```

## ping: in: time exceeded

```python
class Solution:     #ping: time exceeded
    def isSubsequence(self, s: str, t: str) -> bool:
        pos = 0
        for c in s:                         #for each char of s
            if c in t[pos:]:                #if in t, find its pos and
                pos = t.find(c, pos) + 1    #update the next search base
            else:                           #if not found, False
                return False
        return True
```

## ping: find: passed

```python
class Solution:     #ping: passed, remove 'in' which wasted time
    def isSubsequence(self, s: str, t: str) -> bool:
        pos = 0
        for c in s:                     #for each char of s, just find the index
            pos = t.find(c, pos) + 1    #and update the next search base
            if not pos:                 #when not found, find return '-1'
                return False            #then pos is 0, return False
        return True
        """
        ||   ✔ Accepted
        ||   ✔ 14/14 cases passed (32 ms)
        ||   ✔ Your runtime beats 92.51 % of python3 submissions
        ||   ✔ Your memory usage beats 26.67 % of python3 submissions (17.3 MB)
        """
```

## lmv

```python
class Solution:  #lmv: use exception
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in range(len(s)):
            try:
                index = t.index(s[i])
            except ValueError:
                return False
            t = t[index+1:]
        return True

        """
        ||   ✔ Accepted
        ||   ✔ 14/14 cases passed (28 ms)
        ||   ✔ Your runtime beats 96.58 % of python3 submissions
        ||   ✔ Your memory usage beats 26.67 % of python3 submissions (17.3 MB)
        """
```

## lmv

```python
class Solution(object):           
    def isSubsequence(self, s, t):
        t = iter(t)               
        return all(c in t for c in s)
```

## tips

* find return -1 when no found, better than index (no need exception)
* `in` take extra time, use `find` directly, or use char comparison
* use exception
