#
# @lc app=leetcode id=532 lang=python3
#
# [532] K-diff Pairs in an Array
#

# @lc code=start

# ping: fail
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = 0
        while len(nums):
            num = nums.pop()
            if num-k in nums:
                count += 1
                nums.remove(nums-k)
            if num+k in nums:
                count += 1
                nums.remove(nums+k)
        return count

# ping: time limit exceeded
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        count, set1 = 0, set()
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[j]-nums[i]==k and nums[j] not in set1:
                    set1.add(nums[j])
                    count += 1
                    break
        return count

# ping: 2 treat conditions differently: passed
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count, newdup = 0, True
        nums.sort()
        if k > 0:
            nums = set(nums)
            for num in nums:
                if num+k in nums:
                    count += 1
        if k == 0:
            for i in range(len(nums)-1):
                if nums[i] is nums[i+1] and newdup:
                    count += 1
                    newdup = False
                if nums[i] is not nums[i+1]:
                    newdup = True
        return count

# ping: use Counter, not faster
from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = 0
        if k > 0:
            nums = set(nums)
            for num in nums:
                if num+k in nums:
                    count += 1
        if k == 0:
            d = Counter(nums)
            count = sum(1 for num in d if d[num] > 1)
        return count

# lmv
from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
		#If k is less than 0, then the result is 0 since we are looking fpr pairs with an ABSOLUTE difference of k.
        if k < 0:
            return 0

        count = Counter(nums)
        pairs = set([])

        for num in count.keys():
			#Special case: If k == 0, then there needs to be at least two occurences of a particular num in nums
			#in order for there to be a pair (num, num).
            if k == 0:
                if count[num] > 1:
                    pairs.add((num, num))

			#Regular case: k != 0. Simply check if num + k is a member of the array nums.
			#Insert the pair into the set of pairs (smallerNum, largerNum) so that there are no duplicate pairs.
            else:
                otherNum = num + k
                if otherNum in count:
                    pairs.add((num, otherNum) if num <= otherNum else (otherNum, num))

        return len(pairs)

# internet https://blog.csdn.net/fuxuemingzhu/article/details/79255633
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        if k < 0: return 0
        elif k == 0:
            count = collections.Counter(nums)
            for n, v in count.items():
                if v >= 2:
                    res += 1
            return res
        else:
            nums = set(nums)
            for num in nums:
                if num + k in nums:
                    res += 1
            return res
# @lc code=end
