#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:     #lmv
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root: return 0
        return self.rangeSumBST(root.left, L, R) + \
                self.rangeSumBST(root.right, L, R) + \
                (root.val if L <= root.val <= R else 0)

class Solution:     #lmv
    #https://leetcode.com/problems/range-sum-of-bst/discuss/409173
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root: return 0
        if root.val > R: return self.rangeSumBST(root.left,L,R)
        if root.val < L: return self.rangeSumBST(root.right,L,R)
        return root.val + self.rangeSumBST(root.left,L,R) + self.rangeSumBST(root.right,L,R)

class Solution:     #ping
    def __init__(self):
        self.res = 0

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.dfs(root, low, high)
        return self.res

    def dfs(self, root, low, high):
        if root is None: return 0
        if low <= root.val <= high:
            self.res += root.val
        if root.val > low:
            self.dfs(root.left, low, high)
        if root.val < high:
            self.dfs(root.right, low, high)

class Solution:     #remove helper
    def __init__(self):
        self.res = 0    #member var as global var for recursion

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if root is None: return 0
        if low <= root.val <= high:     #if curr root is in range, add it in
            self.res += root.val
        if root.val > low: #recursively do left only when root is higher than
            self.rangeSumBST(root.left, low, high) #low end, otherwise no need
        if root.val < high: #same for right
            self.rangeSumBST(root.right, low, high)
        return self.res

class Solution:     #one liner

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        return 0 if root is None else \
            root.val * (low <= root.val <= high) + \
            self.rangeSumBST(root.left, low, high) * (root.val > low) + \
            self.rangeSumBST(root.right, low, high) * (root.val < high)


# @lc code=end
