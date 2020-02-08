#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start
if 0:
    class Solution:
        def searchMatrix(self, matrix, target):
            """
            :type matrix: List[List[int]]
            :type target: int
            :rtype: bool
            """
            for l in matrix:
                if target in l:
                    return True
            return False

"""
||   ✔ Accepted
||   ✔ 129/129 cases passed (24 ms)
||   ✔ Your runtime beats 98.41 % of python3 submissions
||   ✔ Your memory usage beats 88.89 % of python3 submissions (17.5 MB)
"""

if 1:
    class Solution:
        def searchMatrix(self, matrix, target):
            return any([target in row for row in matrix])

"""
||   ✔ Accepted
||   ✔ 129/129 cases passed (32 ms)
||   ✔ Your runtime beats 82.37 % of python3 submissions
||   ✔ Your memory usage beats 92.59 % of python3 submissions (17.4 MB)
"""
if 0:
    class Solution:
        def searchMatrix(self, matrix, target):
            j = -1
            for row in matrix:
                if row:
                    while j + len(row) and row[j] > target:
                        j -= 1
                    if row[j] == target:
                        return True
            return False

"""
||   ✔ Accepted
||   ✔ 129/129 cases passed (40 ms)
||   ✔ Your runtime beats 37.36 % of python3 submissions
||   ✔ Your memory usage beats 74.07 % of python3 submissions (17.5 MB)
"""

if 0:
    class Solution:
        """
        @param matrix: A list of lists of integers
        @param target: An integer you want to search in matrix
        @return: An integer indicate the total occurrence of target in the given matrix
        """
        def searchMatrix(self, matrix, target):
            if not matrix:
                return False
            count=0
            for i in matrix:
                if i and i[0]<=target and i[-1]>=target and self.helper(i,target):
                    return True
            return False

        def helper(self,list1, target):
            if not list1:
                return False
            if list1[0]==target or  list1[-1]==target:
                return True
            l,r=0,len(list1)-1
            while (l<r-1):
                m=l+(r-l)//2
                if list1[m]==target:
                    return True
                if list1[m]<target:
                    l=m
                else:
                    r=m
            if list1[l]==target or list1[r]==target:
                return True
            return False

"""
||   ✔ Accepted
||   ✔ 129/129 cases passed (28 ms)
||   ✔ Your runtime beats 94.19 % of python3 submissions
||   ✔ Your memory usage beats 92.59 % of python3 submissions (17.4 MB)
"""

# @lc code=end
