---
layout: post
title: "3Grid Unique Paths"
published: true
created:  2020 Feb 05 02:21:26 PM
tags: [python, medium, math, leetcode]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -


# [3Grid Unique Paths](https://www.interviewbit.com/problems/grid-unique-paths/)

https://leetcode.com/problems/unique-paths/description/

## Owen: math

```python
import math
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        n=A-1+B-1
        m=A-1
        return self.helper(n,m)
    def helper(self,n,m):
        return math.factorial(n)/(math.factorial(n-m)*math.factorial(m))
```
### takeaway 

- just a math quiz 
- another way is f(x,y)=f(x-1,y)+f(x,y-1)

## ping: recursion (dfs)

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.helper(1, 1, m, n)

    def helper(self, r, c, m, n):
        # if any step made it to the target, that step is ONE valid one
        if r == m and c == n:
            return 1
        # if any step made it beyond the target, that step is NOT valid
        if r > m or c > n:
            return 0
        return self.helper(r+1, c, m, n) + self.helper(r, c+1, m, n)

S = Solution()
S.uniquePaths(23, 12)

"""
$ leetcode test 62.unique-paths.py -t '10\n10'
  ✔ Finished
  ✔ Your Input: 10
                10
  ✔ Output (84 ms): 48620
  ✔ Expected Answer: 48620
  ✔ Stdout:

✘ Time Limit Exceeded
✘ 37/62 cases passed (N/A)
✘ Testcase: 23
            12
✘ Answer:
✘ Expected Answer:
✘ Stdout:

local test:
[ins] In [3]: S.uniquePaths(23, 12)
Out[3]: 193536720
"""

```

## run code manually

    m=n=2

    helper(1,1,2,2)

    1.(2,1,2,2)                 +  4.(1,2,2,2)

        2.(3,1,2,2)+3.(2,2,2,2) +     5.(2,2,2,2) + 6.(1,3,2,2)

           0       +     1  =1  +        1    +     0=1

                                2



