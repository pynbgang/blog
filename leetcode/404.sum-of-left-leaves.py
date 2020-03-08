#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:     #lmv
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        result, stack = 0, [(root, False)]
        while stack:
            curr, is_left = stack.pop()
            if not curr:                            #if no root, return 0
                continue
            if not curr.left and not curr.right:    #if root no children
                if is_left:                         #and self is left
                    result += curr.val              #add its value
            else:                                   #otherwise
                stack.append((curr.left, True))     #append left, mark it
                stack.append((curr.right, False))   #append right, mark it
        return result
        """
        ||   ✔ Accepted
        ||   ✔ 102/102 cases passed (20 ms)
        ||   ✔ Your runtime beats 99.27 % of python3 submissions
        ||   ✔ Your memory usage beats 100 % of python3 submissions (13 MB)
        """

class Solution(object):     #owen: recursive
    def sumOfLeftLeaves(self, root):
        self.sum1 = 0
        self.helper(root)
        return self.sum1

    def helper(self, root):
        if not root:
            return
        if not root.left and not root.right:
            return
        if root.left and not root.left.left and not root.left.right:
            self.sum1 += root.left.val
        self.helper(root.left)
        self.helper(root.right)
        """
        ||   ✔ Accepted
        ||   ✔ 102/102 cases passed (28 ms)
        ||   ✔ Your runtime beats 82.81 % of python3 submissions
        ||   ✔ Your memory usage beats 100 % of python3 submissions (13 MB)
        """
# @lc code=end
