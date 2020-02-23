#
# @lc app=leetcode id=339 lang=python3
#
# [339] Nested List Weight Sum
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

"""
if 0:

    class Solution:
        def depthSum(self, nestedList: List[NestedInteger]) -> int:
            res = 0
            heler(l, level):
                if isinstance(l, int):
                    res += l
                else:
                    level += 1
                    helper(l, level)

            for l in nestedList:
                level = 1
                return helper(l, 1)
"""

if 0:  # owen

    class Solution:
        # @param {NestedInteger[]} nestedList a list of NestedInteger Object
        # @return {int} an integer
        def depthSum(self, nestedList):
            self.sum = 0
            def dfs(nestedList,depth):
                for i in nestedList:
                    if i.isInteger():
                        self.sum+=i.getInteger()*depth
                    else:
                        dfs(i.getList(),depth+1)

            dfs(nestedList,1)
            return self.sum

if 1:  #xiaofo

    class Solution(object):
        # @param {NestedInteger[]} nestedList a list of NestedInteger Object
        # @return {int} an integer
        def depthSum(self, nestedList):
            # Write your code here
            return sum(self.helper(1, i) for i in nestedList)

        def helper(self, depth, i):
            return i.getInteger() * depth if i.isInteger() else sum(self.helper(depth + 1, n) for n in i.getList())

if 1:  #xiaofo, break longline

    class Solution(object):
        # @param {NestedInteger[]} nestedList a list of NestedInteger Object
        # @return {int} an integer
        def depthSum(self, nestedList):
            # Write your code here
            return sum(self.helper(1, i) for i in nestedList)

        def helper(self, depth, i):
            return (
                i.getInteger() * depth
                if i.isInteger() else
                sum(self.helper(depth + 1, n) for n in i.getList())
            )

if 0:
    class Solution(object):
        # @param {NestedInteger[]} nestedList a list of NestedInteger Object
        # @return {int} an integer
        def depthSum(self, nestedList):
            # Write your code here
            rtn, q = 0, [(ni, 1) for ni in nestedList]
            while q:
                item = q.pop(0)
                if item[0].isInteger():
                    rtn += item[0].getInteger() * item[1]
                else:
                    q += [(ni, item[1] + 1) for ni in item[0].getList()]
            return rtn


# @lc code=end
