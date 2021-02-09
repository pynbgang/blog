---
layout: post
title: "[270] Closest Binary Search Tree Value"
published: true
created:  2021 Feb 07 22:29:00
tags: [python, leetcode, easy, tree, bst, dfs, bfs, min]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[270] Closest Binary Search Tree Value](https://leetcode.com/problems/closest-binary-search-tree-value/description/)

    || * algorithms
    || * Easy (49.42%)
    || * Likes:    949
    || * Dislikes: 74
    || * Total Accepted:    175.8K
    || * Total Submissions: 353K
    || * Testcase Example:  '[4,2,5,1,3]\n3.714286'
    || * Source Code:       270.closest-binary-search-tree-value.py
    || 
    || Given a non-empty binary search tree and a target value, find the value
    in the BST that is closest to the target.
    || 
    || Note:
    || 
    || 
    || 	Given target value is a floating point.
    || 	You are guaranteed to have only one unique value in the BST that is
    closest to the target.
    || 
    || 
    || Example:
    || 
    || 
    || Input: root = [4,2,5,1,3], target = 3.714286
    || 
    || ⁠   4
    || ⁠  / \
    || ⁠ 2   5
    || ⁠/ \
    || 1   3
    || 
    || Output: 4

# solution

```python
class Solution:     #leetcode: DFS
    def closestValue(self, root: TreeNode, target: float) -> int:
        def inorder(r: TreeNode):
            return (inorder(r.left) + [r.val] + inorder(r.right)) if r else []
        return min(inorder(root), key = lambda x: abs(target - x))
```

```python
class Solution:         #BFS, with q
    def closestValue(self, root: TreeNode, target: float) -> int:
        nodes, values = [root], []
        while nodes:
            values.append(nodes[0].val)
            root = nodes.pop(0)
            if root.left:  nodes.append(root.left)
            if root.right: nodes.append(root.right)
        return min(values, key = lambda x: abs(x-target))
```

# tips

* min with key

