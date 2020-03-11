---
layout: post
title: "[20] Valid Parentheses"
published: true
created:  2020 Feb 07 01:57:42 PM
tags: [python, easy, stack, lintcode, leetcode]
categories: [tech]
---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# Valid Parentheses

* [lintcode](https://www.lintcode.com/problem/valid-parentheses/leaderboard?_from=ladder&&fromId=137)
* [leetcode](https://leetcode.com/problems/valid-parentheses/description/)

|| Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
|| determine if the input string is valid.
|| An input string is valid if:
||    1. Open brackets must be closed by the same type of brackets.
||    2. Open brackets must be closed in the correct order.
|| Note that an empty string is also considered valid.
|| Example 1:
|| Input: "()"
|| Output: true
|| Example 2:
|| Input: "()[]{}"
|| Output: true
|| Example 3:
|| Input: "(]"
|| Output: false
|| Example 4:
|| Input: "([)]"
|| Output: false
|| Example 5:
|| Input: "{[]}"
|| Output: true

## owen

### solution

```python
class Solution:

    def isValidParentheses(self, s):
        if not s:
            return False
        stack=[]
        mapping = {'(':')','{':'}','[':']'}
        for i in s:
            if i in mapping:
                stack.append(i)
            elif not stack or (mapping[stack.pop()] != i):
                return False
        return len(stack)==0
```

### Tips
   - 面试题目
   - 典型的STACK应用题目
   - 左括号为KEY 右括号为内容 
   - 每个字符都要判断下 是否和最后压入栈的成为一对 

## ping

### solution

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['[', '{', '(']:
                stack.append(c)
            else:
                if not stack:
                    return False
                if (stack.pop(), c) not in [('[', ']'), ('(', ')'), ('{', '}')]:
                    return False
        if stack:
            return False
        else:
            return True
```

### optimization1

* use a `match` to represent the 3 matching conditions
* merge the 2 conditions leading to same `False`
* merge `if stack else `

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack, match = [], [('[', ']'), ('(', ')'), ('{', '}')]
        for c in s:
            if c in ['[', '{', '(']:
                stack.append(c)
            else:
                if not stack or (stack.pop(), c) not in match:
                    return False
        return not stack
```

### optimization2
* use dict to also include the `['[', '{', '(']` list (by its keys)

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack, match = [], {'[': ']', '(': ')', '{': '}'}
        for c in s:
            if c in match:
                stack.append(c)
            else:
                if not stack or c is not match[stack.pop()]:
                    return False
        return not stack
```

### optimization3

* merge `not x or not y` to `not (x and y)`
* flip the match strings

(lmv)

```python
class Solution:
    def isValid(self, s):
        stack, match = [], {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch in match:
                if not (stack and stack.pop() == match[ch]):
                    return False
            else:
                stack.append(ch)
        return not stack
```

