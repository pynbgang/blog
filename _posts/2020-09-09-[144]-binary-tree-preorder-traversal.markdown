---
layout: post
title: "[144] Binary Tree Preorder Traversal"
published: true
created:  2020 Sep 09 05:52:28 PM
tags: [python, leetcode, medium]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -


# [[144] Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/description/)

    || * algorithms
    || * Medium (53.75%)
    || * Likes:    1698
    || * Dislikes: 62
    || * Total Accepted:    527.8K
    || * Total Submissions: 942.3K
    || * Testcase Example:  '[1,null,2,3]'
    || * Source Code:       144.binary-tree-preorder-traversal.py
    ||
    || Given a binary tree, return the preorder traversal of its nodes' values.
    ||
    || Example:
    ||
    ||
    || Input: [1,null,2,3]
    ||  1
    ||   \
    ||    2
    ||   /
    ||  3
    ||
    || Output: [1,2,3]
    ||
    ||
    || Follow up: Recursive solution is trivial, could you do it iteratively?

## owen

```python
class Solution(object):
    def preorderTraversal(self, root):
        if not root:return []
        self.l=[]
        self.helper(root)
        return self.l
    def helper(self,root):
        if not root.left and not root.right:
            self.l.append(root.val)
            return
        self.l.append(root.val)
        if root.left:self.helper(root.left)
        if root.right:self.helper(root.right)
```

## ping: from template

```python
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
```

NOTE: comparing with owen's solution:
* with member var (a 'global' var in class scope), one less param in helper func
* this won't work. because res will be init.ed only once.

        class Solution:
            res = []
            def preorderTraversal(self, root: TreeNode) -> List[int]:
                self.helper(root, self.res)
                return res

            def helper(self, root, res):
                if root is None:
                    return
                res.append(root.val)
                self.helper(root.left, res)
                self.helper(root.right, res)

        ||   ✘ 1/68 cases passed (N/A)
        ||   ✘ Testcase: []
        ||   ✘ Answer: [1,2,3]
        ||   ✘ Expected Answer: []


## w/o recursion, with stack

```python
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
```

* with stack: LIFO
* so, put (append) right first => left is in tail => get(pop) left first
