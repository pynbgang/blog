#
# @lc app=leetcode id=835 lang=python3
#
# [835] Image Overlap
#

# @lc code=start
class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        Aones = [(i, j) for i in range(len(A)) for j in range(len(A[0])) if A[i][j]]
        Bones = [(i, j) for i in range(len(B)) for j in range(len(B[0])) if B[i][j]]
        d = dict()
        for a in Aones:
            for b in Bones:
                offset = (a[0] - b[0], a[1] - b[1])
                d[offset] = d.get(offset, 0) + 1
        #return max([d[offset] for offset in d] or [0])
        return max(d.values() or [0])


# @lc code=end
