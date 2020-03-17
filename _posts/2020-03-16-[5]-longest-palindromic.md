---
layout: post
title: "[5] Longest Palindromic Substring"
published: true
created:  2020 Mar 16 03:32:50 PM
tags: [python, leetcode, two pointer, medium]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[5] Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)

    ||Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
    ||                                                                                                                   
    ||Example 1:                                                                                                         
    ||                                                                                                                   
    ||Input: "babad"                                                                                                     
    ||Output: "bab"                                                                                                      
    ||Note: "aba" is also a valid answer.                                                                                
    ||Example 2:                                                                                                         
    ||                                                                                                                   
    ||Input: "cbbd"                                                                                                      
      Output: "bb"                                                                                                       




## owen
recuresive time out...-_-#

```python
class Solution(object):
    def longestPalindrome(self, s):
        if not s:return s
        if s==s[::-1]:return s
        t1=self.longestPalindrome(s[1:])
        t2=self.longestPalindrome(s[0:-1])
        if len(t1)>len(t2):return t1
        return t2

two pointer 
class Solution(object):
    def longestPalindrome(self, s):
        if not s:return ""
        l=[]
        for i in xrange(len(s)):
            tmp = self.helper(s, i, i)
            l.append(tmp)
            tmp = self.helper(s, i, i+1)
            l.append(tmp)
        l.sort(key=lambda x:len(x))
        return l[-1]

    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]
        
the last one did not pass,since it is from edge to middle 

class Solution(object):
    def longestPalindrome(self, s):
        if not s: return ""
        if s == s[::-1]: return s
        l1 = [s[0]]
        len1 = len(s)
        for i in range(1,len1-1):
            mingap = min(i, len1 - 1 - i)
            temp1 = self.helper(s[i - mingap:i + mingap + 1])
            temp2 = self.helper(s[i - mingap :i + mingap])
            temp3=self.helper(s[i - mingap+1 :i + mingap+1])
            l1.extend([temp1, temp2,temp3])
        print l1
        l1.sort(key=lambda x: len(x))
        return l1[-1]

    def helper(self, s):
        if s == s[::-1]: return s
        return self.helper(s[1:-1])
```
