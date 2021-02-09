#
# @lc app=leetcode id=270 lang=python3
#
# [270] Closest Binary Search Tree Value
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        mindiff, value = sys.maxsize, root.val
        currdiff = abs(root.val - target)
        if currdiff < mindiff:
            return (currdiff, root.val)
        closestValue(root.left, target)

class Solution:     #leetcode
    def closestValue(self, root: TreeNode, target: float) -> int:
        def inorder(r: TreeNode):
            return (inorder(r.left) + [r.val] + inorder(r.right)) if r else []
        return min(inorder(root), key = lambda x: abs(target - x))

# @lc code=end
