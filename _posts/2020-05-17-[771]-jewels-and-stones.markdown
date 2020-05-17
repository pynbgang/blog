---
layout: post
title: "[771] Jewels and Stones"
published: true
created:  2020 May 17 06:17:07 PM
tags: [python, leetcode, easy, set, sum]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -


# [[771] Jewels and Stones](https://leetcode.com/problems/jewels-and-stones/description/)

    || * algorithms
    || * Easy (84.42%)
    || * Likes:    1982
    || * Dislikes: 351
    || * Total Accepted:    485.1K
    || * Total Submissions: 564.4K
    || * Testcase Example:  '"aA"\n"aAAbbbb"'
    || * Source Code:       771.jewels-and-stones.py
    || 
    || You're given strings J representing the types of stones that are jewels,
    and S representing the stones you have.  Each character in S is a type of
    stone you have.  You want to know how many of the stones you have are also
    jewels.
    || 
    || The letters in J are guaranteed distinct, and all characters in J and S
    are letters. Letters are case sensitive, so "a" is considered a different
    type of stone from "A".
    || 
    || Example 1:
    || 
    || Input: J = "aA", S = "aAAbbbb"
    || Output: 3
    || 
    || Example 2:
    || 
    || Input: J = "z", S = "ZZ"
    || Output: 0
    || 
    || Note:
    || 
    || 	S and J will consist of letters and have length at most 50.
    || 	The characters in J are distinct.

# ping

```python
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(S.count(j) for j in set(J))
```


