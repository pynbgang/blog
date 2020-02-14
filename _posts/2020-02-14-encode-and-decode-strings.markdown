---
layout: post
title: "encode-and-decode-strings"
published: true
created:  2020 Feb 14 11:04:01 AM
tags: [lintcode, leetcode, python, string, medium]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

Place holder, todo

## posted: encode-and-decode-strings

https://www.lintcode.com/problem/encode-and-decode-strings/description

|| Description
|| Design an algorithm to encode a list of strings to a string. The encoded string
|| is then sent over the network and is decoded back to the original list of
|| strings.
|| 
|| Please implement encode and decode
|| 
|| Have you met this question in a real interview?  
|| Example
|| Example1
|| 
|| Input: ["lint","code","love","you"]
|| Output: ["lint","code","love","you"]
|| Explanation:
|| One possible encode method is: "lint:;code:;love:;you"
|| Example2
|| 
|| Input: ["we", "say", ":", "yes"]
|| Output: ["we", "say", ":", "yes"]
|| Explanation:
|| One possible encode method is: "we:;say:;:::;yes"

### wangmazi

```python
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    # " " -> ": " to separate different words
    # ":" -> "::" to identify ":"
    def encode(self, strs):
        # write your code here
        encoded = []
        for string in strs:
            for char in string:
                if char == ":":
                    encoded.append("::")
                else:
                    encoded.append(char)
            
            encoded.append(": ")
        
        # the res will always be ended with ": "
        # such as "lint: code: love: you: "
        return "".join(encoded)

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        res = []
        
        idx = 0
        length = len(str)
        tmp_str = []
        
        # length - 1 because it always ends with ": "
        while idx < length - 1:
            if str[idx] == ":":
                if str[idx + 1] == ":":
                    tmp_str.append(":")
                    idx += 2
                elif str[idx + 1] == " ":
                    res.append("".join(tmp_str))
                    tmp_str = []
                    idx += 2
            else:
                tmp_str.append(str[idx])
                idx += 1
        
        return res
```

