#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:     #lmv
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not (root and p and q):
            return None
        if max(p.val, q.val) < root.val:    #if both pq smaller than root, look
            return self.lowestCommonAncestor(root.left, p, q) #in left branch
        elif min(p.val, q.val) > root.val:  #if both pq bigger than root, look
            return self.lowestCommonAncestor(root.right, p, q) #in right branch
        else:               #otherwise (one is smaller and one is bigger)
            return root     #root is the common ancestor
        """
        ||   ✔ Accepted
        ||   ✔ 27/27 cases passed (72 ms)
        ||   ✔ Your runtime beats 90.31 % of python3 submissions
        ||   ✔ Your memory usage beats 31.9 % of python3 submissions (18.3 MB)
        """

# @lc code=end
