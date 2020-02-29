#
# @lc app=leetcode id=1014 lang=python3
#
# [1014] Best Sightseeing Pair
#

# @lc code=start

class Solution:  # ping: brute force: timeout
    import sys
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        max1 = -sys.maxsize-1
        for i in range(len(A)-1):
            for j in range(i+1, len(A)):
                max1 = max(A[i]+A[j]+i-j, max1)
        return max1

class Solution:  # ping: use dict, not done
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        A=[5,10,20,20,30,30,30,10]
        #A.sort()
        d={}

        # use a d to store the indice for any value
        for i,v in enumerate(A):
            k = d.get(v, [])
            k.append(i)
            d[v] = k

        #Out[123]: {5: [0], 10: [1, 7], 20: [2, 3], 30: [4, 5, 6]}

        #d={k: sorted(d[k]) for k in d}
        nums=sorted(list(d.keys()), reverse=True)
        for i in range(0, len(nums)):
            print("get i,nums[i]: ", i, nums[i])
            num = nums[i]; lindex = d[num]
            if len(lindex) > 1:
                d[num]=[ lindex[j]-lindex[j-1] for j in range(1, len(lindex))]
            else:
                if i<len(nums):
                    num1 = nums[i+1]; lindex1 = d[num1]
                    d[num]=[min(abs(d[num][0]-lindex1[x]) for x in range(len(lindex1)))]

        max1 = 0
        for i in range(0, len(nums)):
            pass

class Solution:  #lmv
    """
    https://leetcode.com/problems/best-sightseeing-pair/discuss/400283

    * Lang:    python3
    * Author:  junaidmansuri
    * Votes:   0
    """

    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        maxi = max1 = 0
        for j in range(1, len(A)):
            maxi = max(maxi, A[i]+i)
            max1 = max(max1, maxi+A[j]-j)
        return max1


# @lc code=end
