#
# @lc app=leetcode id=937 lang=python3
#
# [937] Reorder Data in Log Files
#

# @lc code=start

class Solution: # ping: make use of sorted 'key'
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        """
        "let1 0art can",
        "let3 0art zero"
        "let2 0own kit dig",
        "dig2 a3 6",
        "dig1 a8 1 5 1",
        """

        def helper(s):
            l = s.split()
            if l[1].isalpha():  l = ['0']+l[1:]+l[0:1]
            else:               l = ['a']
            return ' '.join(l)

        return sorted(logs, key=helper)

class Solution: # ping: compacted
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def helper(s):
            l = s.split()
            return ' '.join(['0']+l[1:]+l[0:1] if l[1].isalpha() else ['a'])

        return sorted(logs, key=helper)

        """
        ||   ✔ Accepted
        ||   ✔ 63/63 cases passed (24 ms)
        ||   ✔ Your runtime beats 99.38 % of python3 submissions
        ||   ✔ Your memory usage beats 100 % of python3 submissions (12.8 MB)
        """
class Solution: # ping: oneliner
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        return sorted(logs, key=lambda s: '0'+s[s.index(' ')+1:]+' '+s[0:s.index(' ')] if s[s.index(' ')+1].isalpha() else 'a')

        """
        ||   ✔ Accepted
        ||   ✔ 63/63 cases passed (36 ms)
        ||   ✔ Your runtime beats 56.1 % of python3 submissions
        ||   ✔ Your memory usage beats 100 % of python3 submissions (12.7 MB)
        """

class Solution: # lmv
    """
    Reorder Data in Log Files

    Solution in Python 3 (beats ~100%) (five lines)

    https://leetcode.com/problems/reorder-data-in-log-files/discuss/382667

    * Lang:    python3
    * Author:  junaidmansuri
    * Votes:   5
    """

    def reorderLogFiles(self, G: List[str]) -> List[str]:
        A, B, G = [], [], [i.split() for i in G]
        for g in G:
            if g[1].isnumeric(): B.append(g)
            else: A.append(g)
        return [" ".join(i) for i in sorted(A, key = lambda x: x[1:]+[x[0]]) + B]

        """
        ||   ✔ Accepted
        ||   ✔ 63/63 cases passed (32 ms)
        ||   ✔ Your runtime beats 83.02 % of python3 submissions
        ||   ✔ Your memory usage beats 100 % of python3 submissions (12.8 MB)
        """

# @lc code=end
