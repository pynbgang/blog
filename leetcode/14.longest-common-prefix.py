#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
from typing import List

class Solution:     #ping: brute force, use compare
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        maxpos = -1
        for i in range(len(strs[0])):   #use 1st string as base chars
            for j in range(len(strs)):  #check each string
                if len(strs[j]) > i and strs[j][i] == strs[0][i]:
                    maxpos = i          #if same char in each string @same pos
                else:                   #update the pos, otherwise return until
                    return strs[0][0:maxpos]  #-the previous pos, if no return
        return strs[0][0:maxpos+1]      #in loop, include the current pos also
        """
        ||   ✔ Accepted
        ||   ✔ 118/118 cases passed (32 ms)
        ||   ✔ Your runtime beats 66.3 % of python3 submissions
        ||   ✔ Your memory usage beats 100 % of python3 submissions (12.9 MB)
        """

class Solution:     #ping: brute force, use find
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        maxpos = -1
        for i in range(len(strs[0])):           #for each char in 1st string
            for j in range(len(strs)):          #try to find it in each string
                ind = strs[j].find(strs[0][i], i, i+1)  #-at same pos only
                if ind >= 0:                    #if found
                    maxpos = ind                #update the max matching pos
                if ind == -1:                   #otherwise (no found get -1)
                    return strs[0][0:maxpos]    #return until current pos
        return strs[0][0:maxpos+1] if maxpos >=0 else ""
        """
        ||   ✔ Accepted
        ||   ✔ 118/118 cases passed (36 ms)
        ||   ✔ Your runtime beats 33.67 % of python3 submissions
        ||   ✔ Your memory usage beats 100 % of python3 submissions (12.9 MB)
        """

class Solution:     #ping: use set intersection
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""  #get (char, index) tuples set
        common_set = set((c, i) for i, c in enumerate(strs[0]))
        for str1 in strs:       #get common set of all (char, index) tuples
            common_set &= set((c, i) for i, c in enumerate(str1))
        i, ind = -1, [t[1] for t in common_set] #get indice from it
        for i in range(len(set1)):  #check highest index reachable from 0
            if i not in ind:
                i -= 1; break
        return strs[0][0:i+1]
        """
        ||   ✔ Accepted
        ||   ✔ 118/118 cases passed (44 ms)
        ||   ✔ Your runtime beats 12.23 % of python3 submissions
        ||   ✔ Your memory usage beats 100 % of python3 submissions (12.9 MB)
        """

class Solution(object):     #lmv: use zip
    def longestCommonPrefix(self, strs):
        sz, ret = zip(*strs), ""        #use zip to group chars w/ same index
        for c in sz:                    #also cut all str to the shortest
            if len(set(c)) > 1: break   #exclude any tuple that has a diff char
            ret += c[0]                 #and collect those w/ same letter
        return ret

S=Solution()
strs=["flower","flow","flight"]
strs=["dog","racecar","car"]
strs=["aca","cba"]
S.longestCommonPrefix(strs)

# @lc code=end
