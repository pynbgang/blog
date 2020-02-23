#
# @lc app=leetcode id=1313 lang=python3
#
# [1313] Decompress Run-Length Encoded List
#

# @lc code=start
#ping
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res=[]
        i=0
        while i<len(nums):
            res.extend( nums[i] * [nums[i+1]] )
            i+=2
        return res

#lmv
class Solution:
    def decompressRLElist(self, N: List[int]) -> List[int]:
        return sum([N[i]*[N[i+1]] for i in range(0,len(N),2)],[])

# @lc code=end
