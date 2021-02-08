---
layout: post
title: "[938] Range Sum of BST"
published: true
created:  2021 Feb 07 16:37:28
tags: [python, leetcode, easy, recursion, tree]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -


# [[938] Range Sum of BST](https://leetcode.com/problems/range-sum-of-bst/description/)

    || * algorithms
    || * Easy (82.68%)
    || * Likes:    2024
    || * Dislikes: 279
    || * Total Accepted:    330.3K
    || * Total Submissions: 398.2K
    || * Testcase Example:  '[10,5,15,3,7,null,18]\n7\n15'
    || * Source Code:       938.range-sum-of-bst.py
    || 
    || Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].
    || 
    ||  
    || Example 1:
    || 
    || 
    || Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
    || Output: 32
    || 
    || 
    || Example 2:
    || 
    || 
    || Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
    || Output: 23
    || 
    || 
    ||  
    || Constraints:
    || 
    || 
    || 	The number of nodes in the tree is in the range [1, 2 * 10^4].
    || 	1 <= Node.val <= 10^5
    || 	1 <= low <= high <= 10^5
    || 	All Node.val are unique.

![image](https://user-images.githubusercontent.com/2038044/107160536-df5d1e80-6964-11eb-9675-c33e7601f482.png)

# solution

```python
class Solution:
    def __init__(self):
        self.res = 0
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.dfs(root, low, high)
        return self.res

    def dfs(self, root, low, high):
        if root is None: return
        if low <= root.val <= high:
            self.res += root.val
        if root.val > low:
            self.dfs(root.left, low, high)
        if root.val < high:
            self.dfs(root.right, low, high)
```

# recursion

https://www.defprogramming.com/quotes-by/l-peter-deutsch/
To iterate is human, to recurse, divine.

http://algosaur.us/recursion/

a few considerations:

1. helper or not

2. global or not
    * use global var (member var), just update the value, no neet to return
    * without global var, need to return


