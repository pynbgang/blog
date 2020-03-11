#
# @lc app=leetcode id=476 lang=python3
#
# [476] Number Complement
#

# @lc code=start
class Solution:     #ping: brute force: bit flip
    def findComplement(self, num: int) -> int:
        return int(''.join(str(1-int(i)) for i in bin(num)[2:]), 2)
        """
        ||   ✔ Accepted
        ||   ✔ 149/149 cases passed (24 ms)
        ||   ✔ Your runtime beats 85.4 % of python3 submissions
        ||   ✔ Your memory usage beats 100 % of python3 submissions (12.8 MB)
        """
class Solution(object):     #owen: (2**n-1)-num
    def findComplement(self, num):
        return 2 ** (len(bin(num))-2) - 1 - num

class Solution:     #lmv: num ^ (2**n-1)
    def findComplement(self, num: int) -> int:
        return num ^ (2 ** num.bit_length() - 1)
        """
        Python XOR one line - no loops
        https://leetcode.com/problems/number-complement/discuss/324332

        * Lang:    python3
        * Author:  w2schmitt
        * Votes:   3
        """
# @lc code=end
