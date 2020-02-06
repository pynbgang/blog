#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.helper(1, 1, m, n)

    def helper(self, r, c, m, n):
        if r == m and c == n:
            return 1
        if r > m or c > n:
            return 0
        return self.helper(r+1, c, m, n) + self.helper(r, c+1, m, n)

S = Solution()
S.uniquePaths(23, 12)

"""
$ leetcode test 62.unique-paths.py -t '10\n10'
  ✔ Finished
  ✔ Your Input: 10
                10
  ✔ Output (84 ms): 48620
  ✔ Expected Answer: 48620
  ✔ Stdout:

✘ Time Limit Exceeded
✘ 37/62 cases passed (N/A)
✘ Testcase: 23
            12
✘ Answer:
✘ Expected Answer:
✘ Stdout:

local test:

"""


# @lc code=end
