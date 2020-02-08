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

S = Solution()
test = "[{[{}]"
print(S.isValid(test))

# @lc code=end
