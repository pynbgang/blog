#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# @lc code=start


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        sum0 = sorted([nums[i], nums[j], nums[k]])
                        if sum0 not in res:
                            res.append(sum0)

        return res
# @lc code=end
