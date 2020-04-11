#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:     #ping
    def countBits(self, num: int) -> List[int]:
        res = []
        for i in range(num+1):
            res.append(bin(i).count('1'))
        return res

        """
        ||   ✔ Accepted
        ||   ✔ 15/15 cases passed (96 ms)
        ||   ✔ Your runtime beats 34.85 % of python3 submissions
        ||   ✔ Your memory usage beats 5 % of python3 submissions (20.7 MB)
        """

class Solution(object): #lmv
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        iniArr = [0]
        if num > 0:
            amountToAdd = 1
            while len(iniArr) < num + 1:
                iniArr.extend([x+1 for x in iniArr])
        return iniArr[0:num+1]

        """
        https://leetcode.com/problems/counting-bits/discuss/79538
        * Lang:    python3
        * Author:  startingwars
        * Votes:   29
        Code works by constantly extending a list with itself but with the values
        incremented by 1.
        Simple python solution that runs in O(n) time. Let me know if there are any
        ways to improve it.
        ||   ✔ Accepted
        ||   ✔ 15/15 cases passed (84 ms)
        ||   ✔ Your runtime beats 68.83 % of python3 submissions
        ||   ✔ Your memory usage beats 5 % of python3 submissions (20.7 MB)
        """
class Solution(object): #owen
    def countBits(self, num):
        res = [0]
        for i in range(1, num+1):
            res.append(res[i//2] + 1) if i % 2 else res.append(res[i//2])
        return res

        """
        ||   ✔ Accepted
        ||   ✔ 15/15 cases passed (84 ms)
        ||   ✔ Your runtime beats 68.83 % of python3 submissions
        ||   ✔ Your memory usage beats 5 % of python3 submissions (20.6 MB)
        """

# @lc code=end
