#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
if 0:  #ping: brute force
    class Solution:
        def longestConsecutive(self, nums: List[int]) -> int:
            maxcount = 0

            for i in nums:

                count = 0
                i1 = i

                print("take i:", i)
                while i in nums:
                    i += 1
                    count += 1
                else:
                    print("not in nums")

                print("take i-1:", i1-1)
                while i1-1 in nums:
                    i1 -= 1
                    count += 1
                else:
                    print("not in nums")

                maxcount = max(count, maxcount)

            return maxcount

if 0:  #ping: use set: 1. remove dup 2. record checked
    class Solution:
        def longestConsecutive(self, nums: List[int]) -> int:
            maxcount, checked = 0, set()

            nums=set(nums)
            for i in nums:

                count = 0
                i1 = i

                if i not in checked:
                    print("take i:", i)
                    while i in nums:
                        i += 1
                        count += 1
                        checked.add(i)

                    print("take i-1:", i1-1)
                    while i1-1 in nums:
                        i1 -= 1
                        count += 1
                        checked.add(i1)

                maxcount = max(count, maxcount)

            return maxcount

    """
    ||   ✔ Accepted
    ||   ✔ 68/68 cases passed (56 ms)
    ||   ✔ Your runtime beats 66.84 % of python3 submissions
    ||   ✔ Your memory usage beats 7.41 % of python3 submissions (14.8 MB)
    """

if 0:  #ping: use set pop and remove, to remove extra check set
    class Solution:
        def longestConsecutive(self, nums: List[int]) -> int:
            maxcount, nums = 0, set(nums)
            while nums:
                i1 = i = nums.pop()
                count = 1

                while i+1 in nums:
                    count += 1
                    nums.remove(i+1)
                    i += 1

                while i1-1 in nums:
                    count += 1
                    nums.remove(i1-1)
                    i1 -= 1

                maxcount = max(count, maxcount)

            return maxcount
    """
    ||   ✔ Accepted
    ||   ✔ 68/68 cases passed (64 ms)
    ||   ✔ Your runtime beats 31.28 % of python3 submissions
    ||   ✔ Your memory usage beats 100 % of python3 submissions (13.7 MB)
    """

if 1:  # owen
    class Solution:
        def longestConsecutive(self, A: List[int]) -> int:
            A=sorted(list(set(list(A))))
            dp=[1]*len(A)
            for i in range(1,len(A)):
                if A[i]-A[i-1]==1:
                    dp[i]=dp[i-1]+1
            return max(dp or [0])
    """
    ||   ✔ Accepted
    ||   ✔ 68/68 cases passed (60 ms)
    ||   ✔ Your runtime beats 43.04 % of python3 submissions
    ||   ✔ Your memory usage beats 96.3 % of python3 submissions (13.8 MB)
    """

if 0:   #lmv
    class Solution:
        # @param num, a list of integer
        # @return an integer
        def longestConsecutive(self, num):
            num=set(num)
            maxLen=0
            while num:
                n=num.pop()
                i=n+1
                l1=0
                l2=0
                while i in num:
                    num.remove(i)
                    i+=1
                    l1+=1
                i=n-1
                while i in num:
                    num.remove(i)
                    i-=1
                    l2+=1
                maxLen=max(maxLen,l1+l2+1)
            return maxLen
    """
    ||   ✔ Accepted
    ||   ✔ 68/68 cases passed (52 ms)
    ||   ✔ Your runtime beats 86.48 % of python3 submissions
    ||   ✔ Your memory usage beats 96.3 % of python3 submissions (13.8 MB)
    """
# @lc code=end
