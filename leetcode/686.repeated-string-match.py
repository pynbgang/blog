#
# @lc app=leetcode id=686 lang=python3
#
# [686] Repeated String Match
#

# @lc code=start

class Solution:     #lmv
    def repeatedStringMatch(self, A: str, B: str) -> int:
        """
        https://leetcode.com/problems/repeated-string-match/discuss/330741

        * Lang:    python3
        * Author:  junaidmansuri
        * Votes:   3
        """
        if not set(B).issubset(set(A)): return -1
        for i in range(1, len(B) // len(A) + 3):
            if B in A * i: return i
        return -1
        """
        ✔ Accepted
        ✔ 55/55 cases passed (32 ms)
        ✔ Your runtime beats 96.17 % of python3 submissions
        ✔ Your memory usage beats 5.55 % of python3 submissions (13.9 MB)
        """

class Solution:     #ping: brute force, blink test, fail
    def repeatedStringMatch(self, A: str, B: str) -> int:
        for i in range(10):
            if B in A * i: return i
        return -1
        """
        ✘ Wrong Answer
        ✘ 51/55 cases passed (N/A)
        ✘ Testcase: "baaabbbaba"
        "baaabbbababaaabbbababaaabbbababaaabbbababaaabbbababaaabbbababaaabbbababaaabbbababaaabbbababaaabbbaba"
        ✘ Answer: -1
        ✘ Expected Answer: 10
        ✘ Stdout:
        """

class Solution:     #ping: brute force, passed
    def repeatedStringMatch(self, A: str, B: str) -> int:
        for i in range(1, len(B) // len(A) + 5):
            if B in A * i: return i
        return -1
        """
        ✔ Accepted
        ✔ 55/55 cases passed (696 ms)
        ✔ Your runtime beats 5.07 % of python3 submissions
        ✔ Your memory usage beats 5.55 % of python3 submissions (14.1 MB)
        """

class Solution:     #ping: brute force, test +1
    def repeatedStringMatch(self, A: str, B: str) -> int:
        for i in range(1, len(B) // len(A) + 1):
            if B in A * i: return i
        return -1
        """
        ✘ Wrong Answer
        ✘ 29/55 cases passed (N/A)
        ✘ Testcase: "abcd"
        "cdabcdab"
        ✘ Answer: -1
        ✘ Expected Answer: 3
        ✘ Stdout:
        """

class Solution:     #ping: brute force, test +2
    def repeatedStringMatch(self, A: str, B: str) -> int:
        for i in range(1, len(B) // len(A) + 2):
            if B in A * i: return i
        return -1
        """
        ✘ Wrong Answer
        ✘ 47/55 cases passed (N/A)
        ✘ Testcase: "abc"
        "cabcabca"
        ✘ Answer: -1
        ✘ Expected Answer: 4
        ✘ Stdout:
        """

class Solution:     #ping: brute force, test +3
    def repeatedStringMatch(self, A: str, B: str) -> int:
        for i in range(1, len(B) // len(A) + 3):
            if B in A * i: return i
        return -1
        """
        ✔ Accepted
        ✔ 55/55 cases passed (204 ms)
        ✔ Your runtime beats 17.79 % of python3 submissions
        ✔ Your memory usage beats 5.55 % of python3 submissions (14.1 MB)
        """

# @lc code=end
