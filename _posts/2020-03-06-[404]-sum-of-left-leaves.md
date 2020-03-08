---
layout: post
title: "[404] Sum of Left Leaves"
published: true
created:  2020 Mar 06 10:08:19 PM
tags: [python, leetcode, binary tree,easy]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[404] sum-of-left-leaves](https://leetcode.com/problems/sum-of-left-leaves/description/)

    || * algorithms
    || * Easy (50.13%)
    || * Likes:    911
    || * Dislikes: 104
    || * Total Accepted:    156.9K
    || * Total Submissions: 312.3K
    || * Testcase Example:  '[3,9,20,null,null,15,7]'
    || 
    || Find the sum of all left leaves in a given binary tree.
    || 
    || Example:
    || 
    || ⁠   3
    || ⁠  / \
    || ⁠ 9  20
    || ⁠   /  \
    || ⁠  15   7
    || 
    || There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
    || 
    || 


## Owen: recursive

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        self.sum1 = 0
        self.helper(root)
        return self.sum1

    def helper(self, root):
        if not root: 
            return
        if not root.left and not root.right:
            return
        if root.left and (not root.left.left and not root.left.right):
            self.sum1 += root.left.val
        self.helper(root.left)
        self.helper(root.right)
```

tip:
* only add when it is left+leaf


## lmv: use stack

```python
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
```
