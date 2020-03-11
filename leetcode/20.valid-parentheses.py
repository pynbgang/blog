#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
if 0:
    class Solution:
        def isValid(self, s: str) -> bool:
            stack, match = [], [('[', ']'), ('(', ')'), ('{', '}')]
            for c in s:
                if c in ['[', '{', '(']:
                    stack.append(c)
                else:
                    if not stack:
                        return False
                    if (stack.pop(), c) not in match:
                        return False
            return not stack

if 1:
    class Solution:
        def isValid(self, s: str) -> bool:
            stack, match = [], {'[': ']', '(': ')', '{': '}'}
            for c in s:
                if c in match:
                    stack.append(c)
                else:
                    if not stack or c is not match[stack.pop()]:
                        return False
            return not stack

        """
        ||   ✔ Accepted
        ||   ✔ 76/76 cases passed (32 ms)
        ||   ✔ Your runtime beats 35.31 % of python3 submissions
        ||   ✔ Your memory usage beats 100 % of python3 submissions (12.8 MB)
        """
S = Solution()
test = "[{[{}]"
print(S.isValid(test))

# @lc code=end
