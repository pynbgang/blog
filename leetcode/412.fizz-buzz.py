#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        l = []
        for i in range(1, n+1):
            if not i % 3 and i % 5:
                l.append("Fizz")
            elif not i % 5 and i % 3:
                l.append("Buzz")
            elif not i % 5 and not i % 3:
                l.append("FizzBuzz")
            else:
                l.append(str(i))
        return l

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        l = []
        for i in range(1, n+1):
            l.append(str(i) * bool(i%3 and i%5) + "Fizz" * (not i%3) + "Buzz" * (not i%5))
        return l

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [str(i) * bool(i%3 and i%5) + "Fizz" * (not i%3) + "Buzz" * (not i%5) for i in range(1, n+1)]



# @lc code=end
