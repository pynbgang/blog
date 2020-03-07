#
# @lc app=leetcode id=401 lang=python3
#
# [401] Binary Watch
#

# @lc code=start
from itertools import combinations
class Solution:     #lmv: with combinations
    def readBinaryWatch(self, n: int) -> List[str]:
        T, m = [], [480,240,120,60,32,16,8,4,2,1]
        for i in combinations(m,n):
            if 32 in i and 16 in i and 8 in i and 4 in i: continue
            h, m = divmod(sum(i),60)
            if h > 11: continue
            T.append(str(h)+':'+'0'*(m < 10)+str(m))
        return T
        """
        ||   ✔ Accepted
        ||   ✔ 10/10 cases passed (28 ms)
        ||   ✔ Your runtime beats 81.29 % of python3 submissions
        ||   ✔ Your memory usage beats 100 % of python3 submissions (12.9 MB)
        """

class Solution:     #lmv: brute force
    def readBinaryWatch(self, n: int) -> List[str]:
        return [str(h)+':'+'0'*(m<10)+str(m) for h in range(12) for m in range(60) if (bin(m)+bin(h)).count('1') == n]
        """
        ||   ✔ Accepted
        ||   ✔ 10/10 cases passed (32 ms)
        ||   ✔ Your runtime beats 55.24 % of python3 submissions
        ||   ✔ Your memory usage beats 100 % of python3 submissions (12.7 MB)
        """
# @lc code=end
