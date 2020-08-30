#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start

#revisit: (Sat 29 Aug 2020 07:48:04 PM DST)
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if s[i:j] == s[i:j][::-1]:
                    count += 1
        return count

class Solution:
    def countSubstrings(self, s: str) -> int:
        return sum(s[i:j] == s[i:j][::-1] for i in range(len(s)) for j in range(i+1, len(s)+1))



# @lc code=end
