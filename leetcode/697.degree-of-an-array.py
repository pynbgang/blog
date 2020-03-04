#
# @lc app=leetcode id=697 lang=python3
#
# [697] Degree of an Array
#

# @lc code=start
class Solution:     #lmv
    def findShortestSubArray(self, nums: List[int]) -> int:
        C = {}
        for i, n in enumerate(nums):
            if n in C: C[n].append(i)
            else: C[n] = [i]
        M = max([len(i) for i in C.values()])
        return min([i[-1]-i[0] for i in C.values() if len(i) == M]) + 1

        """
        ||   ✔ Accepted
        ||   ✔ 89/89 cases passed (228 ms)
        ||   ✔ Your runtime beats 95.61 % of python3 submissions
        ||   ✔ Your memory usage beats 9.09 % of python3 submissions (15.1 MB)
        """

class Solution:     #ping: brute force, Counter
    def findShortestSubArray(self, nums: List[int]) -> int:
        from collections import Counter
        nums_rev, len1, min1, d = nums[::-1], len(nums), len(nums), Counter(nums)
        freq = d.most_common(1)[0][1]
        for n in (k for k in d.keys() if d[k]==freq):
            min1 = min(min1, len1-nums_rev.index(n)-nums.index(n))
        return min1
        """
        ||   ✔ Accepted
        ||   ✔ 89/89 cases passed (796 ms)
        ||   ✔ Your runtime beats 12.91 % of python3 submissions
        ||   ✔ Your memory usage beats 100 % of python3 submissions (13.6 MB)
        """
# @lc code=end
