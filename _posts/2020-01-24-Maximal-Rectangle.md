---
layout: post
title: "Maximal Rectangle"
date: 2020-01-24
author: "Owen"
tags: 
    - 2D Matrix
    - lintcode
    - hard
    - python
    - google 
    - 
created:  20120 Jan 24 12:39:49 PM
categories: [tech]
published: true

---


TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

#  [Maximal Rectangle](https://www.lintcode.com/problem/maximal-rectangle/description)

## Owen 

original approach is too slow..

```python
class Solution:

    # find L/R first smaller than itself, increasing monotone stack
    def largestRectangleArea(self, height):
        height = [0] + height + [0]

        # monotonic stack in the sense that height_ext[id_stack[:]] is monotonic
        id_stack = []  

        area = 0
        for i, h in enumerate(height):
            # find the left / right first smaller than itself
            # montone increasing pop out all top element from stack if larger
            # than new comer
            while id_stack and h <= height[id_stack[-1]]: 
            # kick out all greater than comming value h
                id = id_stack.pop()
                nh = height[id]
                w = (i - 1) - id_stack[-1] if len(id_stack) > 0 else i
                area = max(area, nh * w)
            id_stack.append(i)
        return area

    # similar problem
    # @param {boolean[][]} matrix, a list of lists of boolean
    # @return {int} an integer

    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        M = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    M[i][j] = 0
                else:
                    M[i][j] = M[i - 1][j] + 1 if i >= 1 else 1
        max_area = 0
        print M
        for row in M:
            max_area = max(max_area, self.largestRectangleArea(row))
        return max_area

```

### Basic idea on how to solve this 

- 首先HELPER函数是为了检查每行 LIST的最大面积
- 所以需要构建一个新的2D MATRIX M ，是为了收集这行+上面的所有行的和
- 需要计算每行也就是一个LIST的最大面积，这里需要用到STACK/LIST，思路就是横截面积最大
- Youtube上有一些印度工程师的讲解可以参考

## wangmazi

<!--
要做这个题之前先做直方图最大矩阵（Largest Rectangle in Histogram） 这个题。
这个题其实就是包了一层皮而已。一行一行的计算以当前行为矩阵的下边界时，最大矩阵是什么。
计算某一行为下边界时的情况，就可以转换为直方图最大矩阵问题了。
-->

```python
class Solution:
    """
    @param matrix: a boolean 2D matrix
    @return: an integer
    """
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        max_rectangle = 0
        heights = [0] * len(matrix[0])
        for row in matrix:
            for index, num in enumerate(row):
                heights[index] = heights[index] + 1 if num else 0
            max_rectangle = max(
                max_rectangle,
                self.find_max_rectangle(heights),
            )

        return max_rectangle

    def find_max_rectangle(self, heights):
        indices_stack = []
        max_rectangle = 0
        for index, height in enumerate(heights + [-1]):
            while indices_stack and heights[indices_stack[-1]] >= height:
                popped = indices_stack.pop(-1)
                left_bound = indices_stack[-1] if indices_stack else -1
                max_rectangle = max(
                    max_rectangle,
                    (index - left_bound - 1) * heights[popped],
                )
            indices_stack.append(index)
            print(indices_stack)

        return max_rectangle
```
