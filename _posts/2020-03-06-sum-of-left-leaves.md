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

# [[409]  Longest Palindrome](https://leetcode.com/problems/longest-palindrome/)

    ||Find the sum of all left leaves in a given binary tree.
    ||                                                       
    ||Example:                                               
    ||                                                       
    ||    3                                                  
    ||   / \                                                 
    ||  9  20                                                
    ||    /  \                                               
    ||   15   7                                              
    ||                                                       
      There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
                                                                                                                                                       
    ||Output:                                                                                                                                          
    ||7                                                                                                                                                
    ||                                                                                                                                                                                                                                                                                                                                                                                      
      Explanation:                                                                                                                                     
Owen: recursive                                                                        

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        if not root:return 0
        self.sum1=0
        self.helper(root)
        print self.sum1
        return self.sum1
    def helper(self,root):
        if not root:return 
        if not root.left and not root.right:
            return 
        if root.left and (not root.left.left and not root.left.right ):self.sum1+=root.left.val
        self.helper(root.left)
        self.helper(root.right)

        """
```
