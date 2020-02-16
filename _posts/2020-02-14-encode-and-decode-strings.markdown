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

## encode-and-decode-strings

### [lintcode](https://www.lintcode.com/problem/encode-and-decode-strings/description)

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

### [leetcode](https://leetcode.com/problems/encode-and-decode-strings/description/)

    || [leetcode show 271]
    || [271] Encode and Decode Strings  
    || 
    || 
    || * algorithms
    || * Medium (29.81%)
    || * Likes:    360
    || * Dislikes: 133
    || * Total Accepted:    52.3K
    || * Total Submissions: 174.8K
    || * Testcase Example:  '["Hello","World"]'
    || 
    || Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
    || 
    || Machine 1 (sender) has the function:
    || 
    || 
    || string encode(vector<string> strs) {
    || ⁠ // ... your code
    || ⁠ return encoded_string;
    || }
    || Machine 2 (receiver) has the function:
    || 
    || 
    || vector<string> decode(string s) {
    || ⁠ //... your code
    || ⁠ return strs;
    || }
    || 
    || 
    || So Machine 1 does:
    || 
    || 
    || string encoded_string = encode(strs);
    || 
    || 
    || and Machine 2 does:
    || 
    || 
    || vector<string> strs2 = decode(encoded_string);
    || 
    || 
    || strs2 in Machine 2 should be the same as strs in Machine 1.
    || 
    || Implement the encode and decode methods.
    || 
    || Note:
    || 
    || 	The string may contain any possible characters out of 256 valid ascii characters. Your algorithm should be generalized enough to work on any possible characters.
    || 	Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.
    || 	Do not rely on any library method such as eval or serialize methods. You should implement your own encode/decode algorithm.
    || 
    || 

### ideas

the key is to design a special delimitor to "glue" all list items(strings)
into a bigger string

1. use a special non-ascii char (which can't appear in any string - but how
   can it be possible?)
2. use normal string, with a "escaping method" (when it happens to also
   appear in the item string) (wangmazi)
3. use a number to indicate length of each item string in the list
4. combine 2&3 (lmv)

### use non-ascii delimitor

* chr(258) Ă
* chr(301) ą

```python
class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return chr(258)
        # encode here is a workaround to fix BE CodecDriver error
        return chr(258).join(x for x in strs)

    def decode(self, s):
        """Decodes a single string to a list of strings.
        :type s: str
        :rtype: List[str]
        """
        if s == chr(258):
            return []
        return s.split(chr(258))
```

### wangmazi: use ascii delimitor

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

### lmv

```python
class Codec:
    def encode(self, strs):
        return ''.join('%d:' % len(s) + s for s in strs)

    def decode(self, s):
        strs = []
        i = 0
        while i < len(s):
            j = s.find(':', i)
            i = j + 1 + int(s[i:j])
            strs.append(s[j+1:i])
        return strs
```


```python
[ins] In [50]: strs=["they", "don't", "care"]
[ins] In [51]: S.encode(strs)
Out[51]: "4:they5:don't4:care"
#         0123456789012345678
#         i|    |
#         -j(previous :)
#         ------i(start of next num), so between j and i is the string

#         i=0
#           j=1
#           i=j+1+int(s[0:1])=6
#           strs.append(s[j+1:i]) s[2:3]

#         i=6
#           j=7
#           ...
```

## test

```python
S=Solution()
S=Codec()
strs=["they", "don't", "care"]
S.encode(strs)
```

