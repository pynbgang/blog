#
# @lc app=leetcode id=941 lang=python3
#
# [941] Valid Mountain Array
#

# @lc code=start
class Solution:     #ping: without loop
    def validMountainArray(self, A: List[int]) -> bool:
        if not A: return False
        maxpos = A.index(max(A))
        half1, half2 = A[0:maxpos], A[maxpos:]
        return (
            True if                             #in order to be True Mountain
            len(A) >= 3 and                     #the length has to be 3 or more
            maxpos is not len(A)-1 and          #peak has to be not at end
            maxpos is not 0 and                 # or beginning
            half1 == sorted(half1) and          #first half has to be same as
            len(half1) == len(set(half1)) and   #sorted and no dup, 2nd half
            half2 == sorted(half2, reverse=True) and #same as reversely sorted
            len(half2) == len(set(half2))       # and also no dup
            else False                          # otherwise can't be Mountain
        )
        """
        ||   ✔ Accepted
        ||   ✔ 51/51 cases passed (200 ms)
        ||   ✔ Your runtime beats 99.59 % of python3 submissions
        ||   ✔ Your memory usage beats 5.26 % of python3 submissions (14.6 MB)
        """

class Solution:     #ping: with loop
    def validMountainArray(self, A: List[int]) -> bool:
        #for (i, j) in zip(range(1, len(A)), range(len(A)-1, 0, -1)):
        i, len1, half1, half2 = 1, len(A), False, False
        while i < len1 and A[i] > A[i-1]:  #set 1st half true if increasing
            half1 = True
            i += 1
        while i < len1 and A[i] < A[i-1]:  #set 2nd half true if decreasing
            half2 = True
            i += 1 #true only if reach end now and both halves are true
        return True if i == len1 and half1 and half2 else False

        """
        ||   ✔ Accepted
        ||   ✔ 51/51 cases passed (208 ms)
        ||   ✔ Your runtime beats 96.12 % of python3 submissions
        ||   ✔ Your memory usage beats 47.37 % of python3 submissions (14.1 MB)
        """
# @lc code=end
