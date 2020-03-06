#
# @lc app=leetcode id=989 lang=python3
#
# [989] Add to Array-Form of Integer
#

# @lc code=start
class Solution:  #ping
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        return str(int(''.join(str(i) for i in A))+K)
        """
        ||   ✔ Accepted
        ||   ✔ 156/156 cases passed (316 ms)
        ||   ✔ Your runtime beats 66.76 % of python3 submissions
        ||   ✔ Your memory usage beats 55 % of python3 submissions (13.6 MB)
        """

class Solution:  #lmv
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        for i in range(len(A) - 1, -1, -1):
            if not K: break
            K, A[i] = divmod(A[i] + K, 10)
        while K:
            K, a = divmod(K, 10)
            A = [a] + A
        return A
        """
        ||   ✔ Accepted
        ||   ✔ 156/156 cases passed (288 ms)
        ||   ✔ Your runtime beats 91.38 % of python3 submissions
        ||   ✔ Your memory usage beats 40 % of python3 submissions (13.7 MB)
        """

# @lc code=end
