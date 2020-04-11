#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        pass

"""
Easy Recursive Python 7 lines Solution

https://leetcode.com/problems/path-sum-iii/discuss/91942

* Lang:    python3
* Author:  YJL1228
* Votes:   20

Similar to #112 and #113, check the whole tree.
The only difference is: Any node can play as start or end in a valid path.
After each visit, use current node as start, and update the "targets" list.
Pass the updated targets and initial target through.

Base case:
1. node is None

Recursive case:
1. node fits in certain path sum.
2. node doesn't meet.
"""

class Solution(object):         #lmv
    def pathSum(self, root, s):
        return self.helper(root, s, [s])

    def helper(self, node, origin, targets):
        if not node: return 0
        hit = 0
        for t in targets:
            if not t-node.val: hit += 1                  # count if sum == target
        targets = [t-node.val for t in targets]+[origin] # update the targets
        return (hit +
                self.helper(node.left, origin, targets) +
                self.helper(node.right, origin, targets)
                )

class Solution(object):         #lmv: debug
    def pathSum(self, root, s):
        print("| start...")
        self.spaces = 0
        return self.helper(root, s, [s])

    def helper(self, node, origin, targets):
        if not node:
            self.spaces-=4
            msg = "| no more node, return..."
            print(' '*self.spaces+msg, sep='')
            return 0
        else:
            self.spaces+=4
            msg = "| checking node: " + str(node.val)
            print(' '*self.spaces+msg, sep='')
        hit = 0
        for t in targets:
            msg="| take a target: " + str(t) + " from " + str(targets)
            print(' '*self.spaces+msg, sep='')
            if not t-node.val:
                hit += 1                  # count if sum == target
                msg="| match target: " + str(t) + " hit:" + str(hit)
                print(' '*self.spaces+msg, sep='')
            else:
                msg="| not match target: " + str(t) + " hit:" + str(hit) + ", diff: " + str(t-node.val)
                print(' '*self.spaces+msg, sep='')
        targets = [t-node.val for t in targets]+[origin] # update the targets
        msg="| update targets: " + str(targets)
        print(' '*self.spaces+msg, sep='')
        return (hit +
                self.helper(node.left, origin, targets) +
                self.helper(node.right, origin, targets)
                )

#S = Solution()
#root=[10,5,-3,3,2,"null",11,3,-2,"null",1]
#S.pathSum(root, 8)
# @lc code=end
