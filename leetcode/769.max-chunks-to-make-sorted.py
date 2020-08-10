#
# @lc app=leetcode id=769 lang=python3
#
# [769] Max Chunks To Make Sorted
#

# @lc code=start

class Solution(object):     #lmv
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        intervals = []
        for i, n in enumerate(arr):
            intervals.append([min(i, arr[i]), max(i, arr[i])])
        intervals.sort()
        stack = []
        for interval in intervals:
            if not stack or  interval[0] > stack[-1][1]:
                stack.append(interval)
            else:
                a = stack.pop()
                stack.append([a[0], max(a[1], interval[1])])

        return len(stack)

class Solution:     #ping
    def maxChunksToSorted(self, arr: List[int]) -> int:
        if not arr: return 1
        res = 0
        for i in range(len(arr)):      #whenever index equals curr max, split
            if i==max(arr[:i+1]):
                res += 1
        return res

# @lc code=end
