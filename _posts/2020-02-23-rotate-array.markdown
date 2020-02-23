---
layout: post
title: "rotate array"
published: true
created:  2020 Feb 23 03:36:30 PM
tags: [leetcode, python, list, easy]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[189] Rotate Array](https://leetcode.com/problems/rotate-array/description/)

|| * algorithms
|| * Easy (32.78%)
|| * Likes:    2156
|| * Dislikes: 743
|| * Total Accepted:    410.6K
|| * Total Submissions: 1.2M
|| * Testcase Example:  '[1,2,3,4,5,6,7]\n3'
|| * Source Code:       189.rotate-array.py
|| 
|| Given an array, rotate the array to the right by k steps, where k is non-negative.
|| 
|| Example 1:
|| 
|| 
|| Input: [1,2,3,4,5,6,7] and k = 3
|| Output: [5,6,7,1,2,3,4]
|| Explanation:
|| rotate 1 steps to the right: [7,1,2,3,4,5,6]
|| rotate 2 steps to the right: [6,7,1,2,3,4,5]
|| rotate 3 steps to the right: [5,6,7,1,2,3,4]
|| 
|| 
|| Example 2:
|| 
|| 
|| Input: [-1,-100,3,99] and k = 2
|| Output: [3,99,-1,-100]
|| Explanation: 
|| rotate 1 steps to the right: [99,-1,-100,3]
|| rotate 2 steps to the right: [3,99,-1,-100]
|| 
|| 
|| Note:
|| 
|| 
|| 	Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
|| 	Could you do it in-place with O(1) extra space?

# ping

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            nums.insert(0, nums.pop())
        return nums
```

# lmv

4 solutions in python (From easy to hard)

https://leetcode.com/problems/rotate-array/discuss/269948

* Lang:    python3
* Author:  user3284
* Votes:   28

A good start ito think a wayt out is brute force 

1. Approach #1 

   varaible `previous` to store the number being replaced.

   ```python
   class Solution1:
       def rotate(self, nums, k):
           """
           :type nums: List[int]
           :type k: int
           :rtype: None Do not return anything, modify nums in-place instead.
           """
           for _ in range(k):
               previous = nums[-1] #initiate a first previous 
               for i in range(len(nums)):
                   temp = nums[i] #hodl nums[i]
                   nums[i] = previous #overwrite the current index 
                   previous = temp #swap the value 
           logging.debug(f"nums: {nums}")
   ```

   **Complexity Analysis**

   - Time complexity : O( *n*\u2217*k*). All the numbers are shifted by one step(O (n)*O*(*n*)) k times(O (k)*O* ( *k* ) ).
   - Space complexity : O(1). No extra space is used.

2. Approch #2 Using Extra Array

   We use an extra array in which we place every element of the array at its correct position i.e. the number at index i*i* in the original array is placed at the index (i+k)%(length of array)(*i*+*k*). Then, we copy the new array to the original one.

   ```python
   class Solution2:
       def rotate(self, nums, k):
           """
           :type nums: List[int]
           :type k: int
           :rtype: None Do not return anything, modify nums in-place instead.
           """
           a = [0] * len(nums)
           for i in range(len(nums)):
               a[(i+k)%len(nums)] = nums[i] #recycle
   
           for i in range(len(nums)):
               nums[i] = a[i]
   ```

   **Complexity Analysis**

   - Time complexity : O(n). One pass is used to put the numbers in the new array. And another pass to copy the new array to the original one.
   - Space complexity :O*(*n). Another array of the same size is used.



3. Approach #3 Using Cyclic Replacements

   ![solution 3](https://leetcode.com/media/original_images/189_Rotate_Array.png)

   ```python
   class Solution3:
       def rotate(self, nums, k):
           """
           :type nums: List[int]
           :type k: int
           :rtype: None Do not return anything, modify nums in-place instead.
           """
           k = k % len(nums)
           count = 0
           start = 0
           while count < len(nums):
               current = start 
               prev = nums[start] #store the value in the position
               
               while True:
                   next = (current + k) % len(nums) #
                   temp = nums[next] #store it temporaly 
                   nums[next] = prev #overide the next 
                   prev = temp #reset prev
                   current = next #reset current
                   count += 1
   
                   if start == current:
                       break 
               
               start += 1
   ```

   **Complexity Analysis**

   - Time complexity : O(n). Only one pass is used.
   - Space complexity : O(1). Constant extra space is used.





4. #### Approach #4 Using Reverse 

   **Algorithm**

   This approach is based on the fact that when we rotate the array k times, k%n*k* elements from the back end of the array come to the front and the rest of the elements from the front shift backwards.

   In this approach, we firstly reverse all the elements of the array. Then, reversing the first k elements followed by reversing the rest n-k*n*\u2212*k*elements gives us the required result.

   Let n=7*n*=7 and k=3*k*=3.

   ```python
   Original List                   : 1 2 3 4 5 6 7
   After reversing all numbers     : 7 6 5 4 3 2 1
   After reversing first k numbers : 5 6 7 4 3 2 1
   After revering last n-k numbers : 5 6 7 1 2 3 4 --> Result
   ```

   ```python
   class Solution4:
       def rotate(self, nums, k) -> None:
           """
           :type nums: List[int]
           :type k: int
           :rtype: None Do not return anything, modify nums in-place instead.
           """
           k %= len(nums)
           self.reverse(nums,0,len(nums)-1)
           self.reverse(nums,0, k-1)
           self.reverse(nums,k, len(nums)-1)
   
       def reverse(self, nums, start, end) -> None:
           """
           :type nums: List[int]
           :type start: int
           :type end: int
           :rtype: None
           """
           while start < end: #
               temp = nums[start]
               nums[start] = nums[end]
               nums[end] = temp 
               start += 1
               end -= 1
   ```

   **Complexity Analysis**

   - Time complexity : O(n) .n*n*elements are reversed a total of three times.
   - Space complexity : O(1). No extra space is used.

# @lc code=end

