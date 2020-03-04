#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#

# @lc code=start
class Solution:     #ping
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return [i for i in A if not i % 2] + [i for i in A if i % 2]

class Solution:     #lmv
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return sorted(A, key = lambda x : x % 2)

# @lc code=end
