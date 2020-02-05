#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start


class Solution:

    if 1:  # ping

        def reverse(self, x: int) -> int:
            res = int(str(abs(x))[::-1])
            if res > 2 ** 31 - 1:
                return 0
            return res if x > 0 else -res

    """
    ✔ Accepted
    ✔ 1032/1032 cases passed (28 ms)
    ✔ Your runtime beats 78.45 % of python3 submissions
    ✔ Your memory usage beats 100 % of python3 submissions (12.6 MB)
    """

    if 0:  # ping

        def reverse(self, n):
            res=int(str(abs(n))[::-1])
            res = res if n > 0 else -res
            return 0 if res > 2 ** 31 - 1 or res < -(2 ** 31) else res


    """
    ✔ Accepted
    ✔ 1032/1032 cases passed (32 ms)
    ✔ Your runtime beats 51.57 % of python3 submissions
    ✔ Your memory usage beats 100 % of python3 submissions (12.8 MB)
    """

    if 0:  #wangmazi

        def reverse(self, n):
            if n == 0:
                return 0

            neg = 1
            if n < 0:
                neg, n = -1, -n

            reverse = 0
            while n > 0:
                reverse = reverse * 10 + n % 10
                n = n // 10

            reverse = reverse * neg
            if reverse < -(1 << 31) or reverse > (1 << 31) - 1:
                return 0
            return reverse
    """
    ✔ Accepted
    ✔ 1032/1032 cases passed (28 ms)
    ✔ Your runtime beats 78.45 % of python3 submissions
    ✔ Your memory usage beats 100 % of python3 submissions (12.6 MB)
    """

    if 0:  # lmv

        def reverse(self, x):
            s = (x > 0) - (x < 0)
            r = int(str(s*x)[::-1])
            return s * r * (r < 2**31)

    """
    ✔ Accepted
    ✔ 1032/1032 cases passed (32 ms)
    ✔ Your runtime beats 51.57 % of python3 submissions
    ✔ Your memory usage beats 100 % of python3 submissions (12.7 MB)
    """
# @lc code=end
