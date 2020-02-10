# [Longest Consecutive Sequence]
(https://www.interviewbit.com/problems/longest-consecutive-sequence/)
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Example:
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.


## solution (Owen) 
  - within DP ,then return max value in this dp list
  
 ```python
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        if not A:
            return 0
        if len(A)==1:
            return 1
        B=list(set(list(A)))
        B.sort()
        dp=[1]*len(B)
        for i in range(1,len(B)):
            if B[i]-B[i-1]<=1:
                dp[i]=dp[i-1]+1
        return max(dp)
```
