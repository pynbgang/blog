---
layout: post
title: "decompress run length encoded list"
published: true
created:  2020 Feb 22 10:16:23 PM
tags: [leetcode, easy, python, list]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[1313] Decompress Run-Length Encoded List](https://leetcode.com/problems/decompress-run-length-encoded-list/description/)

|| * algorithms
|| * Easy (85.57%)
|| * Likes:    76
|| * Dislikes: 297
|| * Total Accepted:    25K
|| * Total Submissions: 29.4K
|| * Testcase Example:  '[1,2,3,4]'
|| * Source Code:       1313.decompress-run-length-encoded-list.py
|| 
|| We are given a list nums of integers representing a list compressed with run-length encoding.
|| 
|| Consider each adjacent pair of elements [a, b] = [nums[2*i],
|| nums[2*i+1]] (with i >= 0).  For each such pair, there are a elements with
|| value b in the decompressed list.
|| 
|| Return the decompressed list.
|| 
|| Example 1:
|| 
|| Input: nums = [1,2,3,4]
|| Output: [2,4,4,4]
|| Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
|| The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
|| At the end the concatenation [2] + [4,4,4] is [2,4,4,4].
||  
|| Constraints:

    2 <= nums.length <= 100
    nums.length % 2 == 0
    1 <= nums[i] <= 100

# ping

```python
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res=[]
        i=0
        while i<len(nums):
            res.extend( nums[i] * [nums[i+1]] )
            i+=2
        return res
```

tips:
* list multiplication!

#lmv

```python
class Solution:
    def decompressRLElist(self, N: List[int]) -> List[int]:
        return sum([N[i]*[N[i+1]] for i in range(0,len(N),2)],[])
```
