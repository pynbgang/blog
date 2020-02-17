---
layout: post
title: "Palindromic Substrings"
subtitle: "abc"
date: 2020-01-23
author: "Owen"
tags: 
    - lintcode
    - medium
    - python
    - google
    - interview
    - string
    - wangmazi
created:  20120 Jan 23 00:14:49 AM
categories: [tech]
published: true

---


TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [palindromic-substrings](https://www.lintcode.com/problem/palindromic-substrings/description)

## Owen(within helper function On2)

```python
class Solution:

    def countPalindromicSubstrings(self, str):
        if not str:
            return 0
        if len(str)==1:
            return 1
        lenth=len(str)
        count=0
        for i in range(lenth):
            for j in range(i+1,lenth+1):
                if self.checkPalindromic(str[i:j]):
                    count+=1
        return count
    ###helper function to check if it is Palindromic####
    def checkPalindromic(self,str123):
        if len(str123)==1:
            return True
        i=0
        j=len(str123)-1
        while(i<j):
            if str123[i]!=str123[j]:
                return False
            i+=1
            j-=1
        return True
```

## High voted answer (wangmazi)

考虑如果substring(i,j)如果是回文串，那么str[i]和str[j]一定相同，并且一定满足以
下两个条件之一

1. substring(i+1,j-1)也是回文串
2. `j-i<=2`，即substring(i,j)长度 `<=` 2

那么我们就只需要顺着这个思路dp就行了，复杂度On2

```python
class Solution:
   
    def countPalindromicSubstrings(self, str):
        dp = [[0 for j in range(len(str))] for i in range(len(str))]
        ans = 0
        for i in range(len(str)):
            for j in range(i + 1):
                if(str[j] == str[i] and (i - j <= 2 or dp[j + 1][i - 1] == 1)):
                    #need to understand how this dp logical comes from 
                    dp[j][i] = 1
                ans += dp[j][i]
        return ans
```

## ping


```python
class Solution:
    def countPalindromicSubstrings(self, str):
        count=0
        for i in range(len(str)):
            for j in range(i+1, len(str)+1):
                if str[i:j]==str[i:j][::-1]: count+=1
        return count
```

or, oneliner with generator:

use `int` to convert `True/False` to `1/0`

```python
class Solution:
    def countPalindromicSubstrings(self, str):
        return sum((int(str[i:j]==str[i:j][::-1]) for i in range(len(str)) for j in range(i+1, len(str)+1)))
```

lintcode: time limit exceeded

or:

```python
class Solution:
    def countPalindromicSubstrings(self, str):
        return sum( 
            ( 1 for i in 
                (str[i:j] for i in range(len(str)) for j in range(i+1, len(str)+1)) if i==i[::-1]
            )
        )
```

