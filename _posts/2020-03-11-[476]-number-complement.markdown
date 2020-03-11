---
layout: post
title: "[476] Number Complement"
published: true
created:  2020 Mar 11 03:32:50 PM
tags: [python, leetcode, bit, easy, number, math]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[476] Number Complement](https://leetcode.com/problems/number-complement/description/)

    || * algorithms
    || * Easy (63.13%)
    || * Likes:    663
    || * Dislikes: 76
    || * Total Accepted:    124.7K
    || * Total Submissions: 197.2K
    || * Testcase Example:  '5'
    || * Source Code:       476.number-complement.py
    || 
    || Given a positive integer, output its complement number. The complement
    strategy is to flip the bits of its binary representation.
    || 
    || Example 1:
    || Input: 5
    || Output: 2
    || Explanation: The binary representation of 5 is 101 (no leading zero
    bits), and its complement is 010. So you need to output 2.
    || 
    || Example 2:
    || Input: 1
    || Output: 0
    || Explanation: The binary representation of 1 is 1 (no leading zero bits),
    and its complement is 0. So you need to output 0.
    || 
    || Note:
    || 
    || 	The given integer is guaranteed to fit within the range of a 32-bit
    ||  signed integer.
    || 	You could assume no leading zero bit in the integer’s binary
    ||  representation.
    || 	This question is the same as
    ||  1009: https://leetcode.com/problems/complement-of-base-10-integer/

```python
class Solution:     #ping: brute force: bit flip
    def findComplement(self, num: int) -> int:
        return int(''.join(str(1-int(i)) for i in bin(num)[2:]), 2)
        """
        ||   ✔ Accepted
        ||   ✔ 149/149 cases passed (24 ms)
        ||   ✔ Your runtime beats 85.4 % of python3 submissions
        ||   ✔ Your memory usage beats 100 % of python3 submissions (12.8 MB)
        """
class Solution(object):     #owen: (2**n-1)-num
    def findComplement(self, num):
        return 2 ** (len(bin(num))-2) - 1 - num

class Solution:     #lmv: num ^ (2**n-1)
    def findComplement(self, num: int) -> int:
        return num ^ (2 ** num.bit_length() - 1)
        """
        Python XOR one line - no loops
        https://leetcode.com/problems/number-complement/discuss/324332

        * Lang:    python3
        * Author:  w2schmitt
        * Votes:   3
        """
"""

