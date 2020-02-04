#
# @lc app=leetcode id=1021 lang=python3
#
# [1021] Remove Outermost Parentheses
#
# https://leetcode.com/problems/remove-outermost-parentheses/description/
#
# algorithms
# Easy (76.51%)
# Likes:    308
# Dislikes: 450
# Total Accepted:    66.3K
# Total Submissions: 86.6K
# Testcase Example:  '"(()())(())"'
#
# A valid parentheses string is either empty (""), "(" + A + ")", or A + B,
# where A and B are valid parentheses strings, and + represents string
# concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid
# parentheses strings.
# 
# A valid parentheses string S is primitive if it is nonempty, and there does
# not exist a way to split it into S = A+B, with A and B nonempty valid
# parentheses strings.
# 
# Given a valid parentheses string S, consider its primitive decomposition: S =
# P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.
# 
# Return S after removing the outermost parentheses of every primitive string
# in the primitive decomposition of S.
# 
# 
# 
# Example 1:
# 
# 
# Input: "(()())(())"
# Output: "()()()"
# Explanation: 
# The input string is "(()())(())", with primitive decomposition "(()())" +
# "(())".
# After removing outer parentheses of each part, this is "()()" + "()" =
# "()()()".
# 
# 
# 
# Example 2:
# 
# 
# Input: "(()())(())(()(()))"
# Output: "()()()()(())"
# Explanation: 
# The input string is "(()())(())(()(()))", with primitive decomposition
# "(()())" + "(())" + "(()(()))".
# After removing outer parentheses of each part, this is "()()" + "()" +
# "()(())" = "()()()()(())".
# 
# 
# 
# Example 3:
# 
# 
# Input: "()()"
# Output: ""
# Explanation: 
# The input string is "()()", with primitive decomposition "()" + "()".
# After removing outer parentheses of each part, this is "" + "" = "".
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# S.length <= 10000
# S[i] is "(" or ")"
# S is a valid parentheses string
# 
# 
# 
# 
# 
# 
# 
#

# @lc code=start

#     3    2
#0  1 2 3  4    5
#(  ( ( )  )    )
class Solution:
#    def removeOuterParentheses(self, S: str) -> str:
#        stack=[]
#        icount=jcount=0
#        new=''
#        for i in range(len(S)):
#            if S[i] == '(': 
#                icount+=1
#            if S[i] == ')': 
#                jcount+=1
#                if icount==jcount: 
#                    new+=S[i-2*icount+2: i]
#                    icount=jcount=0
#        return new

    #def removeOuterParentheses(self, S: str) -> str:
    #    stack, rtn = [], ""
    #    for c in S:
    #        if c == ")" : stack.pop()
    #        if stack    : rtn += c
    #        if c == "(" : stack.append(c)
    #    return rtn
    
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        rtn = ""
        for c in S:
            if c == "(":
                if stack:
                    rtn += c
                stack.append(c)
            if c == ")":
                stack.pop()
                if stack:
                    rtn += c
        return rtn


# @lc code=end
