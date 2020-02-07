#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#
# @lc code=start

if 1:
    from math import factorial as fa
    class Solution:
        def uniquePaths(self, A: int, B: int) -> int:
            return fa(A-1+B-1)//(fa(B-1) * fa(A-1))

if 0:
    class Solution:
        def uniquePaths(self, m: int, n: int) -> int:
            return self.helper(1, 1, m, n)

        def helper(self, r, c, m, n):
            if r == m and c == n:
                return 1
            if r > m or c > n:
                return 0
            return self.helper(r+1, c, m, n) + self.helper(r, c+1, m, n)

    print("testing...")
    S = Solution()
    s = S.uniquePaths(2, 3)
    print(s)

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
    [ins] In [3]: S.uniquePaths(23, 12)
    Out[3]: 193536720

    """

# @lc code=end
