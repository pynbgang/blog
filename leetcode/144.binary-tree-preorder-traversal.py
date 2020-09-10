#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root is None:
            return
        res.append(root.val)
        self.helper(root.left, res)
        self.helper(root.right, res)

class Solution:     #ping: BFS template: not preorder
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        from queue import Queue
        q, res = Queue(), []
        if not root:
            return
        q.put(root)
        while not q.empty():
            root = q.get()
            res.append(root.val)
            if root.left:
                q.put(root.left)
            if root.right:
                q.put(root.right)
        return res

class Solution:     #lmv, BFS, stack (LIFO)
    def preorderTraversal(self, root):
        ret = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                ret.append(node.val)
                stack.append(node.right) #put right first, so get left first
                stack.append(node.left)
        return ret

class Solution:     #ping: BFS template, preorder
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack, res = [], []
        if not root:
            return
        stack.append(root)
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return res


# @lc code=end
