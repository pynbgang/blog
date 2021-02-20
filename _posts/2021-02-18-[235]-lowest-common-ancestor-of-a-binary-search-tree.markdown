---
layout: post
title: "[235] Lowest Common Ancestor of a Binary Search Tree"
published: true
created:  2021 Feb 18 20:39:21
tags: [python, leetcode, easy, tree, recursion]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[235] Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/)

    || * algorithms
    || * Easy (51.09%)
    || * Likes:    2824
    || * Dislikes: 125
    || * Total Accepted:    476.7K
    || * Total Submissions: 922.3K
    || * Testcase Example:  '[6,2,8,0,4,7,9,null,null,3,5]\n2\n8'
    || * Source Code:       235.lowest-common-ancestor-of-a-binary-search-tree.py
    || 
    || Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
    || 
    || According to the definition of LCA on Wikipedia: “The lowest common
    ancestor is defined between two nodes p and q as the lowest node in T that
    has both p and q as descendants (where we allow a node to be a descendant
    of itself).”
    || 
    ||  
    || Example 1:
    || 
    || 
    || Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
    || Output: 6
    || Explanation: The LCA of nodes 2 and 8 is 6.
    || 
    || 
    || Example 2:
    || 
    || 
    || Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
    || Output: 2
    || Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a
    descendant of itself according to the LCA definition.
    || 
    || Example 3:
    || 
    || Input: root = [2,1], p = 2, q = 1
    || Output: 2
    ||  
    || Constraints:
    || 
    || 	The number of nodes in the tree is in the range [2, 10^5].
    || 	-10^9 <= Node.val <= 10^9
    || 	All Node.val are unique.
    || 	p != q
    || 	p and q will exist in the BST.

# solution

```python
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
```

