#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:  # http://laker.me/blog/2019/02/23/19_0223_leetcode_39/
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        print(res)
        return res

    def dfs(self, nums, target, index, path, res):
        print(nums, target, index, path, res)
        for i in range(index, len(nums)):
            remain = target - nums[i]
            if remain < 0:
                break
            if remain == 0:
                res.append(path + [nums[i]])
                break
            self.dfs(nums, remain, i, path + [nums[i]], res)
            print('i=%d' %i)
            print('===')


a =Solution()
a.combinationSum([2,3,6,7], 7)
# @lc code=end
