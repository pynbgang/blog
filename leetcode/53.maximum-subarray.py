#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        #pres记录前i个数的和，
        #mins记录前i个数中总和和最小的一段（0-k）,
        #maxs记录全局最大值，
        mins, pres, maxs = 0,0, -sys.maxsize

        for num in nums:
            pres += num
            maxs = max(maxs, pres - mins)
            mins = min(mins, pres)

        return maxs

    def maxSubArray(self, nums): #ping (Thu 27 Aug 2020 01:07:30 PM DST) brute force timeout
            return max(max(sum(nums[i:j+1]) for j in range(i, len(nums))) for i in range(len(nums)))

class Solution:
    def maxSubArray(self, nums):
        sum, maxs=0, -sys.maxsize
        for num in nums:
            sum=num + (sum if sum > 0 else 0)
            maxs=max(maxs, sum)
        return maxs


# @lc code=end
