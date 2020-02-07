#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
if 0:
    class Solution:
        def removeElement(self, nums: List[int], val: int) -> int:
            j = 0
            for i in range(len(nums)):
                if nums[i] != val:
                    nums[j] = nums[i]
                    j += 1
            return j

    """
    ||   ✔ Accepted
    ||   ✔ 113/113 cases passed (32 ms)
    ||   ✔ Your runtime beats 58.83 % of python3 submissions
    ||   ✔ Your memory usage beats 100 % of python3 submissions (12.7 MB)
    ||   ✔ Accepted
    ||   ✔ 113/113 cases passed (40 ms)
    ||   ✔ Your runtime beats 14.42 % of python3 submissions
    ||   ✔ Your memory usage beats 100 % of python3 submissions (12.5 MB)
    """

if 1:
    class Solution:
        def removeElement(self, nums, val):
            start, end = 0, len(nums) - 1
            while start <= end:
                if nums[start] == val:
                    nums[start], nums[end], end = nums[end], nums[start], end - 1
                else:
                    start +=1
            return start

    """
    ||   ✔ Accepted
    ||   ✔ 113/113 cases passed (24 ms)
    ||   ✔ Your runtime beats 95.88 % of python3 submissions
    ||   ✔ Your memory usage beats 100 % of python3 submissions (12.9 MB)
    """

# @lc code=end
