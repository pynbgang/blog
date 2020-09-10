---
layout: post
title: "[145] Binary Tree Postorder Traversal"
published: true
created:  2020 Sep 09 08:56:33 PM
tags: [python, leetcode]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -


# [[145] Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/description/)

    || * algorithms
    || * Hard (52.02%)
    || * Likes:    2004
    || * Dislikes: 102
    || * Total Accepted:    403.6K
    || * Total Submissions: 727.5K
    || * Testcase Example:  '[1,null,2,3]'
    || * Source Code:       145.binary-tree-postorder-traversal.py
    || 
    || Given the root of a binary tree, return the postorder traversal of its nodes' values.
    || 
    || Follow up: Recursive solution is trivial, could you do it iteratively?
    || 
    || Example 1:
    || 
    || Input: root = [1,null,2,3]
    || Output: [3,2,1]
    || 
    || Example 2:
    || Input: root = []
    || Output: []
    || 
    || Example 3:
    || Input: root = [1]
    || Output: [1]
    || 
    || Example 4:
    || Input: root = [1,2]
    || Output: [2,1]
    || 
    || Example 5:
    || Input: root = [1,null,2]
    || Output: [2,1]
    ||  
    || Constraints:
    || 
    || 
    || 	The number of the nodes in the tree is in the range [0, 100].
    || 	-100 <= Node.val <= 100
