#
# @lc app=leetcode id=650 lang=python3
#
# [650] 2 Keys Keyboard
#

# @lc code=start
#https://leetcode-cn.com/problems/2-keys-keyboard/solution/python-bi-jiao-rong-yi-li-jie-de-tan-xin-si-xiang-/
class Solution(object):
    def minSteps(self, n):
        a, b, s = 1, 0, 0  #当前记事本上的字符数, 剪切板里的字符数, 操作步数
        while a < n:             #在已有字符数到达目标前循环：
            if (n-a) % a == 0:   #  仅当所剩字符数能被当前字符数整除，
                b = a; s += 1    #  此情况下可以复制，步骤加一
            a += b; s += 1       #  （无论是否已复制）黏贴, 步骤加一
        return s

class Solution:         #sum of all primes
    def minSteps(self, n: int) -> int:
        res = 0 #iterate to find all primes, w/ sqrt old trick from #?
        for i in range(2, int(math.sqrt(n)) + 1): # use each num in range
            while n % i == 0:   #to devide, if exact dividable
                res += i        #add it and
                n /= i          #repeat same num, until not exactly dividable
        # either totally divided (to 1), or one last prime left (7 in 2x2x3x7)
        return int(res if n==1 else res+n) #collect the last prime if any

# @lc code=end
