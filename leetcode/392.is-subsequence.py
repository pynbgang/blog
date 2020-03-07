#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:     #ping: time exceeded
    def isSubsequence(self, s: str, t: str) -> bool:
        pos = 0
        for c in s:                         #for each char of s
            if c in t[pos:]:                #if in t, find its pos and
                pos = t.find(c, pos) + 1    #update the next search base
            else:                           #if not found, False
                return False
        return True

class Solution:     #ping: passed, remove 'in' which wasted time
    def isSubsequence(self, s: str, t: str) -> bool:
        pos = 0
        for c in s:                     #for each char of s, just find the index
            pos = t.find(c, pos) + 1    #and update the next search base
            if not pos:                 #when not found, find return '-1'
                return False            #then pos is 0, return False
        return True
        """
        ||   ✔ Accepted
        ||   ✔ 14/14 cases passed (32 ms)
        ||   ✔ Your runtime beats 92.51 % of python3 submissions
        ||   ✔ Your memory usage beats 26.67 % of python3 submissions (17.3 MB)
        """

class Solution:  #lmv: use exception
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in range(len(s)):
            try:
                index = t.index(s[i])
            except ValueError:
                return False
            t = t[index+1:]
        return True

        """
        ||   ✔ Accepted
        ||   ✔ 14/14 cases passed (28 ms)
        ||   ✔ Your runtime beats 96.58 % of python3 submissions
        ||   ✔ Your memory usage beats 26.67 % of python3 submissions (17.3 MB)
        """

class Solution(object):     #lmv: use iter
    def isSubsequence(self, s, t):
        t = iter(t)
        return all(c in t for c in s)
        """
        ||   ✔ Accepted
        ||   ✔ 14/14 cases passed (56 ms)
        ||   ✔ Your runtime beats 83 % of python3 submissions
        ||   ✔ Your memory usage beats 26.67 % of python3 submissions (17.4 MB)
        """
# @lc code=end
