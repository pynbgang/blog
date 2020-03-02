#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#

# @lc code=start
class Solution:  #ping: wrong, can't sort
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        return sum(sorted(nums)[-1:-k-1:-1])/k

class Solution:  #ping: time limit exceeded
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        return max(sum(nums[i:i+k]) for i in range(len(nums)-k+1))/k

class Solution:  #ping: passed
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max1 = sum1 = sum(nums[0:k])
        for i in range(len(nums)-k):
            sum1+=nums[i+k]-nums[i]
            max1=max(max1, sum1)
        return max1/k
        #res=max(sum1, max([sum1+nums[i+k]-nums[i] for i in range(len(nums)-k)] or [-sys.maxsize]))/k

        """
        ||   ✔ Accepted
        ||   ✔ 123/123 cases passed (896 ms)
        ||   ✔ Your runtime beats 81.22 % of python3 submissions
        ||   ✔ Your memory usage beats 12.5 % of python3 submissions (16.1 MB)
        """

class Solution:     #lmv
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        M = d = 0
        for i in range(len(nums)-k):
            d += nums[i+k] - nums[i]
            if d > M: M = d
        return (sum(nums[:k])+M)/k

        """
        ||   ✔ Accepted
        ||   ✔ 123/123 cases passed (872 ms)
        ||   ✔ Your runtime beats 94.21 % of python3 submissions
        ||   ✔ Your memory usage beats 12.5 % of python3 submissions (16.1 MB)
        """
# @lc code=end
