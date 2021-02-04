---
layout: post
title: "[680] Valid Palindrome II"
published: true
created:  2021 Feb 04 16:55:03
tags: [python, leetcode]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [680. Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/)

    Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
    Example 1:
    Input: "aba"
    Output: True
    Example 2:
    Input: "abca"
    Output: True
    Explanation: You could delete the character 'c'.
    Note:
    The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

# solution:

```python
class Solution:     # brute force: timeout
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        else:
            for i in range(len(s)):
                s1 = s[:i] + s[i+1:]
                if s1 == s1[::-1]:
                    return True
        return False

class Solution:     #double pointer from LMV, ON, ON
    def validPalindrome(self, s: str) -> bool:
        p, q = 0, len(s)-1
        while p < q:
            if s[p] != s[q]:
                cut_l, cut_r = s[p+1:q+1], s[p:q]
                return cut_l == cut_l[::-1] or cut_r == cut_r[::-1]
            p += 1; q -= 1
        return True
```

# tips

    a b c d c b d
    ^           ^

* start from 2 end point
* if same, move inward
* if not, check if removing either end will result in a palindrome
* use `if s[p] != s[q]` instead of `if s[p] == s[q]: xx else: yy` to save one branch



