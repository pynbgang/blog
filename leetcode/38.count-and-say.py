#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:     #ping
    def countAndSay(self, n: int) -> str:
        if n == 1: return "1"
        s = self.countAndSay(n-1)
        c0, count, res = s[0], 0, ""
        for c in s:
            if c==c0:
                count += 1
            else:
                res += str(count) + c0
                count, c0 = 1, c
        res += str(count) + c
        return res

class Solution:     #lmv
    def countAndSay(self, n):
        s = '1'
        for _ in range(n - 1):
            s = ''.join(str(len(group)) + digit
                        for group, digit in re.findall(r'((.)\2*)', s))
        return s

class Solution:     #lmv
    def countAndSay(self, n):
        s = '1'
        for _ in range(n - 1):
            s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
            #          ---------   -------------------------------------------
            #           regex           repl
        return s

# @lc code=end
