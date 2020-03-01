#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#

# @lc code=start
class Solution:     # ping: sort and compare
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums1=sorted(nums)
        start=stop=-1
        for i in range(len(nums)):
            if nums[i] is not nums1[i]:
                start = i; break
        for i in range(len(nums)-1,-1,-1):
            if nums[i] is not nums1[i]:
                stop = i; break
        return stop-start+1 if start is not -1 else 0
    """
    ||   ✔ Accepted
    ||   ✔ 307/307 cases passed (192 ms)
    ||   ✔ Your runtime beats 99.82 % of python3 submissions
    ||   ✔ Your memory usage beats 100 % of python3 submissions (13.8 MB)
    """

class Solution:     #lmv, nothing spcial
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        start, end = -1, -1
        i = 0
        while(i < len(nums)):
            if nums[i] != sortedNums[i]:
                start = i
                break
            i += 1
        if start == -1: return 0 # already sorted
        i = len(nums) - 1
        while(i >= 0):
            if nums[i] != sortedNums[i]:
                end = i
                break
            i -= 1
        return end - start + 1

    """
    ||   ✔ Accepted
    ||   ✔ 307/307 cases passed (196 ms)
    ||   ✔ Your runtime beats 99.49 % of python3 submissions
    ||   ✔ Your memory usage beats 85 % of python3 submissions (14.1 MB)
    """

class Solution:     # ping: merge the two loops
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start, stop, nums1 = -1, -1, sorted(nums)
        for i,j in zip(range(len(nums)), range(len(nums)-1,-1,-1)):
            if nums[i] is not nums1[i] and start==-1:
                start = i;
            if nums[j] is not nums1[j] and stop==-1:
                stop = j;
            if start != -1 and stop != -1: break
        return stop-start+1 if start is not -1 else 0

    """
    ||   ✔ Accepted
    ||   ✔ 307/307 cases passed (208 ms)
    ||   ✔ Your runtime beats 88.51 % of python3 submissions
    ||   ✔ Your memory usage beats 80 % of python3 submissions (14.1 MB)
    """

# @lc code=end
