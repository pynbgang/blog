#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start

class Solution(object):     #brute force
    def twoSum(self, nums, target):
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [-1, -1]

class Solution(object):     #using "in", no comment, easiest
    # no comment
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            if target - nums[i] in nums[i+1:]:
                return [i, i+1+nums[i+1:].index(target - nums[i])]
        return [-1, -1]

class Solution(object):     #using "in", debug version
    def twoSum(self, nums, target):
        # 循环nums数值，并添加映射
        for i in range(len(nums)):
            print(i, ":", nums[i])
            if target - nums[i] in nums[i+1:]:
                print(
                    "found it! %d (%d - %d) in nums" %
                    (target - nums[i], target, nums[i])
                )
                return [i, i+1+nums[i+1:].index(target - nums[i])]
        # 无解的情况
        return [-1, -1]


class Solution(object):     # one liner: doesn't work:
    def twoSum(self, nums, target):
        return [
            [i, i+1+nums[i+1:].index(target - nums[i])]
            for i in range(len(nums))
            if target - nums[i] in nums[i+1:]
        ] or [-1, -1]

        """
        $ leetcode submit 1.two-sum.py
        ✘ Wrong Answer
        ✘ 0/29 cases passed (N/A)
        ✘ Testcase: [2,7,11,15]
        9
        ✘ Answer: [[0, 1]]
        ✘ Expected Answer: [0,1]
        ✘ Stdout:
        """

class Solution(object):     #with dict
    def twoSum(self, nums, target):
        #use dict to record the 1st num
        # d用于建立数值到下标的映射
        d = {}
        # 循环nums数值，并添加映射
        for i in range(len(nums)):
            # print(i, ":", nums[i], d)
            if target - nums[i] in d:
                # print(
                #     "found it! %d (%d - %d) in d" %
                #     (target - nums[i], target, nums[i])
                # )
                return [d[target - nums[i]], i]
            # print("not in current d, put into it")
            d[nums[i]] = i
        # 无解的情况
        return [-1, -1]

class Solution:             #with dict, another version
    #use dict to record the expected 2nd num
    # @return a tuple, (index1, index2)
    # 8:42
    def twoSum(self, num, target):
        d = {}
        for i in range(len(num)):
            if num[i] not in d:
                d[target - num[i]] = i
            else:
                return d[num[i]], i
        return -1, -1

        """
        ✔ Accepted
        ✔ 29/29 cases passed (44 ms)
        ✔ Your runtime beats 92.62 % of python3 submissions
        ✔ Your memory usage beats 58.6 % of python3 submissions (14.2 MB)
        """

# @lc code=end
