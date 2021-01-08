#
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
#

# @lc code=start
class Solution:     #ON2
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        return count

class Solution:     #ON
    def numIdenticalPairs(self, nums: List[int]) -> int:
        repeat, res = {}, 0
        for v in nums:
            if v not in repeat:
                repeat[v] = 1
            else:
                res += repeat[v]
                repeat[v] += 1
        return res

class Solution:     #ON
    from collections import Counter
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res, c = 0, Counter(nums)
        return sum(c[n]*(c[n]-1)//2 for n in c if c[n] >= 2)


#nums = [1,2,3,1,1,3]

# @lc code=end
