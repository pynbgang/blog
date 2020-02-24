---
layout: post
title: "minimum-moves-to-equal-array-elements"
published: true
created:  2020 Feb 24 11:44:22 AM
tags: [lintcode, python, easy, medium, list, math]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[453] Minimum Moves to Equal Array Elements](https://leetcode.com/problems/minimum-moves-to-equal-array-elements/description/)

|| * algorithms
|| * Easy (49.77%)
|| * Likes:    472
|| * Dislikes: 694
|| * Total Accepted:    67.1K
|| * Total Submissions: 134.8K
|| * Testcase Example:  '[1,2,3]'
|| * Source Code:       453.minimum-moves-to-equal-array-elements.py
|| 
|| Given a non-empty integer array of size n, find the minimum number of moves
|| required to make all array elements equal, where a move is incrementing n - 1
|| elements by 1.
|| 
|| Example:
|| 
|| Input:
|| [1,2,3]
|| 
|| Output:
|| 3
|| 
|| Explanation:
|| Only three moves are needed (remember each move increments two elements):
|| 
|| [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

# lmv

Python Greedy -- Sum - Min*Len

https://leetcode.com/problems/minimum-moves-to-equal-array-elements/discuss/272994

* Lang:    python3
* Author:  WangQiuc
* Votes:   5

## idea

The greedy heuristics here is that we always add |max-min| to all elements
except the maximum until all elements are equal. In such way, we keep making
current minimum catch up with maximum without wasting any unnecessary steps.
Suppose we now sort our array as `{X1,...,Xn}` For first catch up, we take `(Xn
- X1)` steps. 

And now `Xn-1` becomes the new maximum as `Xn + Xn-1 - X1` and new minimum is
`Xn`. So next catch take `(Xn-1 - X1)` steps. And similiarly, for `ith`
iteration, the catch up takes `(Xi - X1)` steps. So total number of step would
be `∑Xi - X1 * n` or `sum(X) - min(X) * len(X)`.

tips:

* illustration: 

        `len=4, n=3: x0..x3`

        0   1   2   3

        1   2   4   8
        ---------       +7(x3-x0)
        8   10  11  8
        ------      --  +3(x2-x0)
        11  13  11  11
        --      ------  +2(x1-x0)
        13  13  13  13

        ∑(xi-x0): i:range(len)
            = (x3-x0)+(x2-x0)+(x1-x0) 
            = (x3-x0)+(x2-x0)+(x1-x0)+(x0-x0)
            = (x0+...xn) - x0 * len
            = sum - x0*len

* ∑: \u2211. so vim input: `<c-v>u2211`

## code

```python
def minMoves(nums):
    return sum(nums) - min(nums)*len(nums)
```
