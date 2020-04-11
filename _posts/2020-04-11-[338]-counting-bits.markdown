---
layout: post
title: "[338] Counting Bits"
published: true
created:  2020 Apr 11 12:16:56 PM
tags: [python, leetcode, medium, dp]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[338] Counting Bits](https://leetcode.com/problems/counting-bits/description/)

    || * algorithms
    || * Medium (66.60%)
    || * Likes:    2128
    || * Dislikes: 139
    || * Total Accepted:    230.7K
    || * Total Submissions: 343.4K
    || * Testcase Example:  '2'
    || * Source Code:       338.counting-bits.py
    || 
    || Given a non negative integer number num. For every numbers i in the
    range 0 ≤ i ≤ num calculate the number of 1's in their binary
    representation and return them as an array.
    || 
    || Example 1:
    || 
    || Input: 2
    || Output: [0,1,1]
    || 
    || Example 2:
    || 
    || Input: 5
    || Output: [0,1,1,2,1,2]
    || 
    || Follow up:
    || 
    || It is very easy to come up with a solution with run time
    || O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a
    || single pass?
    || Space complexity should be O(n).
    || Can you do it like a boss? Do it without using any builtin function like
    || __builtin_popcount in c++ or in any other language.


## ping: brute force + bin

```python
class Solution:     #ping
    def countBits(self, num: int) -> List[int]:
        res = []
        for i in range(num+1):
            res.append(bin(i).count('1'))
        return res

        """
        ||   ✔ Accepted
        ||   ✔ 15/15 cases passed (96 ms)
        ||   ✔ Your runtime beats 34.85 % of python3 submissions
        ||   ✔ Your memory usage beats 5 % of python3 submissions (20.7 MB)
        """
```

## owen: dp

```python
class Solution(object): #owen
    def countBits(self, num):
        res = [0]
        for i in range(1, num+1):
            res.append(res[i//2] + 1) if i % 2 else res.append(res[i//2])
        return res

        """
        ||   ✔ Accepted
        ||   ✔ 15/15 cases passed (84 ms)
        ||   ✔ Your runtime beats 68.83 % of python3 submissions
        ||   ✔ Your memory usage beats 5 % of python3 submissions (20.6 MB)
        """
```

## lmv
```python
class Solution(object): #lmv
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        iniArr = [0]
        if num > 0:
            amountToAdd = 1
            while len(iniArr) < num + 1:
                iniArr.extend([x+1 for x in iniArr])
        return iniArr[0:num+1]

        """
        https://leetcode.com/problems/counting-bits/discuss/79538
        * Lang:    python3
        * Author:  startingwars
        * Votes:   29
        Code works by constantly extending a list with itself but with the values
        incremented by 1.
        Simple python solution that runs in O(n) time. Let me know if there are any
        ways to improve it.
        ||   ✔ Accepted
        ||   ✔ 15/15 cases passed (84 ms)
        ||   ✔ Your runtime beats 68.83 % of python3 submissions
        ||   ✔ Your memory usage beats 5 % of python3 submissions (20.7 MB)
        """
```

