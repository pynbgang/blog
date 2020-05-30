#
# @lc app=leetcode id=1341 lang=python3
#
# [1341] The K Weakest Rows in a Matrix
#

# @lc code=start

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        t=[(i, sum(mat[i])) for i in range(len(mat))]
        t.sort(key=lambda x: x[1])
        return [t[i][0] for i in range(k)]

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        t=sorted([(i, (sum(mat[i]))) for i in range(len(mat))], key=lambda x: x[1])
        return [t[i][0] for i in range(k)]

# @lc code=end
