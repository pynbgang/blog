---
layout: post
title: "[125] Valid Palindrome"
published: true
created:  2021 Feb 17 15:06:01
tags: [python, leetcode]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[125] Valid Palindrome](https://leetcode.com/problems/valid-palindrome/description/)

    || * algorithms
    || * Easy (37.67%)
    || * Likes:    1757
    || * Dislikes: 3583
    || * Total Accepted:    792.3K
    || * Total Submissions: 2.1M
    || * Testcase Example:  '"A man, a plan, a canal: Panama"'
    || * Source Code:       125.valid-palindrome.py
    || 
    || Given a string, determine if it is a palindrome, considering only
    alphanumeric characters and ignoring cases.
    || 
    || Note: For the purpose of this problem, we define empty string as valid palindrome.
    || 
    || Example 1:
    || 
    || 
    || Input: "A man, a plan, a canal: Panama"
    || Output: true
    || 
    || Example 2:
    || 
    || Input: "race a car"
    || Output: false
    ||  
    || Constraints:
    || 
    || 	s consists only of printable ASCII characters.

# solution

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = [c.lower() for c in s if c.isalnum()]
        return s1 == s1[::-1]

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            #print(s[l], s[r])
            while not s[l].isalnum() and l < r:
                l += 1
            while not s[r].isalnum() and l < r:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1; r -= 1  #<---same as with else: xxx
        return True
```
