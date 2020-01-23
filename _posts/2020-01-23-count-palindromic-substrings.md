---
layout: post
title: "Palindromic Substrings"
subtitle: "abc"
date: 2020-01-23
author: "Owen"
tags: 
    - Palindromic
    - lintcode
    - medium
    - python
    - Google Phone interview
created:  20120 Jan 23 00:14:49 AM
categories: [tech]
published: true

---


TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# Owen's Solution(within helper function),however it is O(N**2)
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
# High voted answer

class Solution:

   
    def countPalindromicSubstrings(self, str):
        dp = [[0 for j in range(len(str))] for i in range(len(str))]
        ans = 0
        for i in range(len(str)):
            for j in range(i + 1):
                if(str[j] == str[i] and (i - j <= 2 or dp[j + 1][i - 1] == 1)):
                <<<---need to understand how this dp logical comes from 
                    dp[j][i] = 1
                ans += dp[j][i]
        return ans
