#
# @lc app=leetcode id=961 lang=python3
#
# [961] N-Repeated Element in Size 2N Array
#

# @lc code=start

from collections import Counter
class Solution:     #ping: with Counter
    def repeatedNTimes(self, A: List[int]) -> int:
        return Counter(A).most_common(1)[0][0]
        """
        ||   ✔ Accepted
        ||   ✔ 102/102 cases passed (236 ms)
        ||   ✔ Your runtime beats 37.72 % of python3 submissions
        ||   ✔ Your memory usage beats 73.47 % of python3 submissions (14.1 MB)
        """

def repeatedNTimes(self, A: List[int]) -> int:  #lmv
    unique = set()       # empty set
    for i in A:
        if i in unique:  # if i already exists then it is a duplicate
            return i     # loop is exited as value is directly returned
        unique.add(i)    # this can be kept in else: part but not required

    """
    ||   ✔ Accepted
    ||   ✔ 102/102 cases passed (232 ms)
    ||   ✔ Your runtime beats 44.44 % of python3 submissions
    ||   ✔ Your memory usage beats 93.88 % of python3 submissions (14 MB)
    """
# @lc code=end
