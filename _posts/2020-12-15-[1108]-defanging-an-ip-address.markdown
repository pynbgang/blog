---
layout: post
title: "[1108] Defanging an IP Address"
published: true
created:  2020 Dec 15 15:04:09
tags: [python, leetcode]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[1108] Defanging an IP Address](https://leetcode.com/problems/defanging-an-ip-address/description/)

    || * algorithms
    || * Easy (88.34%)
    || * Likes:    529
    || * Dislikes: 996
    || * Total Accepted:    249.8K
    || * Total Submissions: 282.8K
    || * Testcase Example:  '"1.1.1.1"'
    || 
    || Given a valid (IPv4) IP address, return a defanged version of that IP address.
    || 
    || A defanged IP address replaces every period "." with "[.]".
    ||  
    || Example 1:
    || Input: address = "1.1.1.1"
    || Output: "1[.]1[.]1[.]1"
    || Example 2:
    || Input: address = "255.100.50.0"
    || Output: "255[.]100[.]50[.]0"
    || 
    ||  
    || Constraints:
    || 
    || 
    || 	The given address is a valid IPv4 address.


# ping

```python
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]", -1)
```
