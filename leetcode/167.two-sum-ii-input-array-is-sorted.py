#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start

# ping
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            if target-numbers[i] in numbers[i+1:]:
                return [i+1, i+2+numbers[i+1:].index(target-numbers[i])]
        return None

# lmv

    """
    Two Sum II - Input array is sorted

    Python different solutions (two-pointer, dictionary, binary search).

    https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/discuss/51249

    * Lang:    python3
    * Author:  caikehe
    * Votes:   218
    """

class Solution:
    # two-pointer
    def twoSum1(self, numbers, target):
        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1

class Solution:
    # dictionary
    def twoSum2(self, numbers, target):
        dic = {}
        for i, num in enumerate(numbers):
            if target-num in dic:
                return [dic[target-num]+1, i+1]
            dic[num] = i

class Solution:
    # binary search
    def twoSum(self, numbers, target):
        for i in range(len(numbers)):
            l, r = i+1, len(numbers)-1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r-l)//2
                if numbers[mid] == tmp:
                    return [i+1, mid+1]
                elif numbers[mid] < tmp:
                    l = mid+1
                else:
                    r = mid-1

# @lc code=end
