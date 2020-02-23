#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for num2 in nums2:                  #for each num in nums2
            i = 0
            while i<m:                 #iterate nums1 to find insert pos
                if num2 <= nums1[i]:        #  if found ever
                    nums1.insert(i, num2)   #  insert
                    nums1.pop()             #  and pop the ending 0
                    break                   #  and that's it for this num2
                i += 1
            else:                           #otherwise, use this num2 to
                nums1[m] = num2        #  update the first 0 in the end
            m = m+1               #update nums1 len after insertion

"""
https://leetcode.com/problems/merge-sorted-array/discuss/29699

* Lang:    python3
* Author:  lime66
* Votes:   31
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        nums1[:n] = nums2[:n]


# @lc code=end
