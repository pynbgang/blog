---
layout: post
title: "Valid Parentheses"
published: true
created:  2020 Feb 07 01:57:42 PM
tags: [python, easy, stack]
categories: [tech]
---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# Valid Parentheses

https://www.lintcode.com/problem/valid-parentheses/leaderboard?_from=ladder&&fromId=137

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

## Tips
   - 面试题目
   - 典型的STACK应用题目
   - 左括号为KEY 右括号为内容 
   - 每个字符都要判断下 是否和最后压入栈的成为一对 
