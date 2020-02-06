#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start


if 0:  # ping: half way, run into "list length hell"
    from typing import List
    class Solution:
        def removeDuplicates(self, nums: List[int]) -> int:
            n = 0
            while n < len(nums):
                del nums[n]
                if nums and nums[n] in nums:
                    continue
                else:
                    nums.insert(n, nums[n])
                    n += 1
            return len(nums)

    nums = [1,1,2,2,3,3,4,4]
    S = Solution()
    S.removeDuplicates(nums)
    nums

if 1:  # lmv: avoid changing the list length
    from typing import List
    class Solution:
        def removeDuplicates(self, nums: List[int]) -> int:
            x = 1
            for i in range(len(nums)-1):
                if(nums[i]!=nums[i+1]):
                    nums[x] = nums[i+1]
                    x+=1
            return(x)

    S = Solution()
    nums = [1,1,2,2,3,3,4,4]
    nums = [1,1,1,1,1,1,1,1]
    nums = [1,1,1,1,1,1,1,2]
    nums = [1,2,3,3,4,4,5,6]
    S.removeDuplicates(nums)
    nums
# @lc code=end
