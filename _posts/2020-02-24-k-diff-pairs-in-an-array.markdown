---
layout: post
title: "k-diff-pairs-in-an-array"
published: true
created:  2020 Feb 24 02:13:44 PM
tags: [python, leetcode, list, easy, Counter, collections, module, wangmazi, brute force]
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

## ping

### tips

requirements are kind of tricky, it indicates:

* when k is negative, return 0
* 1,3,5 k2: compose 1,3; 3,5. so 3 is (allowed to be) used twice
* 3,3,5 k2: composes 3,5; instead of 3,5; 3,5; 5 can be used only once as "right border"
* 3,3,5,5 k2: composes 3,5; 3,5; each 3 and 5 can be used twice.
* 1,1,1,2,2 k0: composes 1,1; 2,2; instead of 1,1;1,1;2,2; a duplicated number count as 1 only

### 2 conditions: passed

```python
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count, newdup = 0, True
        nums.sort()
        if k > 0:
            nums = set(nums)
            for num in nums:
                if num+k in nums:
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

### use Counter

not faster

```python
from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = 0
        if k > 0:
            nums = set(nums)
            for num in nums:
                if num+k in nums:
                    count += 1
        if k == 0:
            d = Counter(nums)
            count = sum(1 for num in d if d[num] > 1)
        return count
```

### failed

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

### time limit exceeded

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

## wangmazi

```python
class Solution:
    """
    @param nums: an array of integers
    @param k: an integer
    @return: the number of unique k-diff pairs
    """

    def findPairs(self, nums, k):
        # Write your code here
        nums.sort()
        n, j, ans = len(nums), 0, 0
        for i in range(n):
            if i == j:
                j += 1
            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1
            while j + 1 < n and nums[j] == nums[j + 1]:
                j += 1
            while j < n and abs(nums[i] - nums[j]) < k:
                j += 1
            if j >= n:
                break
            if abs(nums[i] - nums[j]) == k:
                ans, j = ans + 1, j + 1
        return ans
```
