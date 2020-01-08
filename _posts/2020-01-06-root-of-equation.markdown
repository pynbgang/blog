---
layout: post
title: "root-of-equation"
published: true
created:  2020 Jan 06 09:40:23 AM
tags: [lintcode, dayoushi, python, math]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [easy:root-of-equation](https://www.lintcode.com/problem/root-of-equation/description?_from=ladder&&fromId=99)

## 有诗云

        偶闻一

    京都明月潇潇夜
    寒露爬窗催解题
    酒醒不知身何处
    再续簋街不夜席

## mine

```python
class Solution:
    """
    @param: a: parameter of the equation
    @param: b: parameter of the equation
    @param: c: parameter of the equation
    @return: a double array, contains at most two root
    """
    import math
    def rootOfEquation(self, a, b, c):
        # write your code here
        if not a:
            return [-c / b]
        sq=b*b-4*a*c
        if sq < 0:
            return []
        else:
            r1=(-b+math.sqrt(sq))/(2*a)
            r2=(-b-math.sqrt(sq))/(2*a)
            if r1==r2: return [r1]
            return [r1, r2] if r1<r2 else [r2,r1]
```

keys:

            -b+-sqrt(b^2-4ac)
    root =  -----------------
            2a


## zhangba

```python
class Solution:
    # @param {double} a, a decimal
    # @param {double} b, a decimal
    # @param {double} c, a decimal
    # @return {double[]} a float array
    def rootOfEquation(self, a, b, c):
        # Write your code here
        if b * b - 4 * a * c < 0:
            return []
        if b * b - 4 * a * c == 0:
            return [-b * 1.0 / 2 / a]
        if b * b - 4 * a * c > 0:
            delta = math.sqrt(b * b - 4 * a * c)
            return sorted([(-b - delta) / (2 * a), (-b + delta) / (2 * a)])
```


