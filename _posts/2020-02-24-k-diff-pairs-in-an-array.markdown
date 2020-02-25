---
layout: post
title: "k-diff-pairs-in-an-array"
published: true
created:  2020 Feb 24 02:13:44 PM
tags: [python, leetcode, list, easy]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[532] K-diff Pairs in an Array](https://leetcode.com/problems/k-diff-pairs-in-an-array/description/)

|| * algorithms
|| * Easy (30.85%)
|| * Likes:    471
|| * Dislikes: 1096
|| * Total Accepted:    87.1K
|| * Total Submissions: 281.7K
|| * Testcase Example:  '[3,1,4,1,5]\n2'
|| 
|| Given an array of integers and an integer k, you need to find the number of
unique k-diff pairs in the array. Here a k-diff pair is defined as an integer
pair (i, j), where i and j are both numbers in the array and their absolute
difference is k.

|| Example 1:
|| 
|| Input: [3, 1, 4, 1, 5], k = 2
|| Output: 2
|| Explanation: There are two 2-diff pairs in the array, (1, 3) and (3,
5).Although we have two 1s in the input, we should only return the number of
unique pairs.

|| Example 2:
|| 
|| Input:[1, 2, 3, 4, 5], k = 1
|| Output: 4
|| Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
|| 
|| Example 3:
|| 
|| Input: [1, 3, 1, 5, 4], k = 0
|| Output: 1
|| Explanation: There is one 0-diff pair in the array, (1, 1).
|| 
|| Note:
|| 
|| The pairs (i, j) and (j, i) count as the same pair.
|| The length of the array won't exceed 10,000.
|| All the integers in the given input belong to the range: [-1e7, 1e7].

## ping: fail

```python
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = 0
        while len(nums):
            num = nums.pop()
            if num-k in nums:
                count += 1
                nums.remove(nums-k)
            if num+k in nums:
                count += 1
                nums.remove(nums+k)
        return count
```

## ping: time limit exceeded

```python
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        count, set1 = 0, set()
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[j]-nums[i]==k and nums[j] not in set1:
                    set1.add(nums[j])
                    count += 1
                    break
        return count
```

## ping: very slow

```python
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count, newdup = 0, True
        nums.sort()
        if k > 0:
            for num in set(nums):
                if num+k in set(nums):
                    count += 1
        if k == 0:
            for i in range(len(nums)-1):
                if nums[i] is nums[i+1] and newdup:
                    count += 1
                    newdup = False
                if nums[i] is not nums[i+1]:
                    newdup = True
        return count

"""
||   ✔ Accepted
||   ✔ 72/72 cases passed (7788 ms)
||   ✔ Your runtime beats 5 % of python3 submissions
||   ✔ Your memory usage beats 96.77 % of python3 submissions (14.2 MB)
"""
```

## ping: use Counter: same, slow

```python
from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = 0
        if k > 0:
            for num in set(nums):
                if num+k in set(nums):
                    count += 1
        if k == 0:
            d = Counter(nums)
            count = sum(1 for num in d if d[num] > 1)
        return count
```

## lmv

```python
from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
		#If k is less than 0, then the result is 0 since we are looking fpr pairs with an ABSOLUTE difference of k.
        if k < 0:
            return 0

        count = Counter(nums)
        pairs = set([])

        for num in count.keys():
			#Special case: If k == 0, then there needs to be at least two occurences of a particular num in nums
			#in order for there to be a pair (num, num).
            if k == 0:
                if count[num] > 1:
                    pairs.add((num, num))

			#Regular case: k != 0. Simply check if num + k is a member of the array nums.
			#Insert the pair into the set of pairs (smallerNum, largerNum) so that there are no duplicate pairs.
            else:
                otherNum = num + k
                if otherNum in count:
                    pairs.add((num, otherNum) if num <= otherNum else (otherNum, num))

        return len(pairs)
```

## internet https://blog.csdn.net/fuxuemingzhu/article/details/79255633

```python
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        if k < 0: return 0
        elif k == 0:
            count = collections.Counter(nums)
            for n, v in count.items():
                if v >= 2:
                    res += 1
            return res
        else:
            nums = set(nums)
            for num in nums:
                if num + k in nums:
                    res += 1
            return res
```
