---
layout: post
title: "[137] Single Number II"
published: true
created:  2020 Sep 08 11:15:04 PM
tags: [python, leetcode, bit]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[137] Single Number II](https://leetcode.com/problems/single-number-ii/description/)

    || * algorithms
    || * Medium (48.29%)
    || * Likes:    1963
    || * Dislikes: 368
    || * Total Accepted:    255.9K
    || * Total Submissions: 486.1K
    || * Testcase Example:  '[2,2,3,2]'
    || * Source Code:       137.single-number-ii.py
    || 
    || Given a non-empty array of integers, every element appears three times
    except for one, which appears exactly once. Find that single one.
    || 
    || Note:
    || 
    || Your algorithm should have a linear runtime complexity. Could you
    implement it without using extra memory?
    || 
    || Example 1:
    || Input: [2,2,3,2]
    || Output: 3
    || 
    || Example 2:
    || Input: [0,1,0,1,0,1,99]
    || Output: 99

## owen

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (sum(set(nums))*3 - sum(nums))//2
```

## lmv


Python Bit Manipulation  (with more general case)

https://leetcode.com/problems/single-number-ii/discuss/43412

* Lang:    python3
* Author:  briankwong
* Votes:   14

```python
class Solution(object):
    def singleNumber(self, nums):
        one, two = 0, 0
        for x in nums:
            one, two, three = one ^ x, two | (one & x), two & x
            one, two = one & ~three, two & ~three
        return one
```

Actually, this approach can be generalized for the case that each number
appears 5 times except one:

```python
class Solution(object):
    def singleNumber(self, nums):
        one = two = three = four = 0
        for x in nums:
            one, two, three, four, five = one ^ x, two | (one & x), three | (two & x), four | (three & x), four & x
            one, two, three, four = one & ~three & ~five, two & ~three, three & ~four, four & ~five
        return one
```

If each number appears 5 times except that one number appears only 3 times,
`return three` will be the result
