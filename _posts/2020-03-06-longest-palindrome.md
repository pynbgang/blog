---
layout: post
title: "[409] Longest Palindrome"
published: true
created:  2020 Mar 06 10:08:19 PM
tags: [python, leetcode, list,easy]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[409]  Longest Palindrome](https://leetcode.com/problems/longest-palindrome/)

    ||Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
    ||                                                                                                                                                 
    ||This is case sensitive, for example "Aa" is not considered a palindrome here.                                                                    
    ||                                                                                                                                                 
    ||Note:                                                                                                                                            
    ||Assume the length of given string will not exceed 1,010.                                                                                         
    ||                                                                                                                                                 
    ||Example:                                                                                                                                         
    ||                                                                                                                                                 
    ||Input:                                                                                                                                           
      "abccccdd"                                                                                                                                       
                                                                                                                                                       
    ||Output:                                                                                                                                          
    ||7                                                                                                                                                
    ||                                                                                                                                                                                                                                                                                                                                                                                      
      Explanation:                                                                                                                                     
Owen: One longest palindrome that can be built is "dccaccd", whose length is 7.                                                                        

```python
class Solution(object):
    def longestPalindrome(self, s):
        if len(s)==1:return 1
        dict1={}
        for i in s:dict1[i]=dict1.get(i,0)+1
        even=0
        flag=False
        for i in dict1.keys():
            if dict1[i]%2==0:
                even+=dict1[i]
            else:
                flag=True
                even+=dict1[i]-1
        if flag:return even+1
        return even
            

        """
```
