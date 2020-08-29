#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
#(Fri 28 Aug 2020 08:03:46 PM DST)
class Solution:
    def longestPalindrome(self, s: str) -> int:
        d, count, isthereodd = {}, 0, 0
        for i in s:
            d[i] = d.get(i, 0) + 1
        for i in d.values():
            if not i % 2:
                count += i
            if i % 2:
                count += i-1
                if not isthereodd:
                    count += 1
                    isthereodd = 1
        return count
#(Fri 28 Aug 2020 08:21:25 PM DST)
# @lc code=end
