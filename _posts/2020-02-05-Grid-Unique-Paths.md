---
layout: post
title: "3Grid Unique Paths"
published: true
created:  2020 Feb 05 02:21:26 PM
tags: [python, medium, math, leetcode, lintcode, math, itertools, scipy]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -


# [3Grid Unique Paths](https://www.interviewbit.com/problems/grid-unique-paths/)

https://leetcode.com/problems/unique-paths/description/

## owen: math.factorial

```python
from math import factorial as fa
class Solution:
    def uniquePaths(self, A: int, B: int): -> int
        return fa(A-1+B-1)/( fa(B-1) * fa(A-1))
```

### takeaway 

- just a math quiz 
- another way is f(x,y)=f(x-1,y)+f(x,y-1)

## ping: recursion/dfs (leetcode)

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
s = S.uniquePaths(10, 10)
print(s)

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

### run code manually

    m=n=2

    helper(1,1,2,2)

    1.(2,1,2,2)                 +  4.(1,2,2,2)

        2.(3,1,2,2)+3.(2,2,2,2) +     5.(2,2,2,2) + 6.(1,3,2,2)

           0       +     1  =1  +        1    +     0=1

                                2



## ping: combination (leetcode)

    C(m+n-2, n-1)

why?

        0  1  2  3  4  5  6
       +--+--+--+--+--+--+--+
     0 |S |  |  |  |  |  |  |
       +--+--+--+--+--+--+--+
     1 |  |  |  |  |  |  |  |
       +--+--+--+--+--+--+--+
     2 |  |  |  |  |  |  | E|
       +--+--+--+--+--+--+--+

* total 7+3=10 grids
* total 6+2=8 steps, 2 D(own) and 6 R(ight)
* e.g:

        S: D R R R R R D R :E
        S: R D R R R D R R :E
        S:   ......        :E
        S:   ......        :E

* the original problem becomes combination of choosing 2(n3-1) out of
  8(m7-1+n3-1)

why?

https://www.youtube.com/watch?v=M8BYckxI8_U

### calculate combinations/permutations

#### scipy.special (need install)

    [ins] In [12]: from scipy.special import comb, perm               

    [ins] In [13]: comb(10,2)                                         
    Out[13]: 45.0

    [ins] In [14]: comb(10,8)                                         
    Out[14]: 45.0

    [ins] In [15]: comb(10,3)                                         
    Out[15]: 120.0

    [ins] In [16]: comb(10,7)                                         
    Out[16]: 120.0

#### itertools (built in)

    [ins] In [7]: from itertools import permutations as perm1         
    [ins] In [8]: from itertools import combinations as comb1         

    [ins] In [9]: perm1(range(10), 2)                                 
    Out[9]: <itertools.permutations at 0x7fd8e8b73f10>

    [ins] In [19]: list(comb1(range(5),2))                            
    Out[19]: 
    [(0, 1),
    (0, 2),
    (0, 3),
    (0, 4),
    (1, 2),
    (1, 3),
    (1, 4),
    (2, 3),
    (2, 4),
    (3, 4)]

    [ins] In [20]: list(comb1(range(4),2))                            
    Out[20]: [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

    [ins] In [21]: list(perm1(range(5),2))                            
    Out[21]: 
    [(0, 1),
    (0, 2),
    (0, 3),
    (0, 4),
    (1, 0),
    (1, 2),
    (1, 3),
    (1, 4),
    (2, 0),
    (2, 1),
    (2, 3),
    (2, 4),
    (3, 0),
    (3, 1),
    (3, 2),
    (3, 4),
    (4, 0),
    (4, 1),
    (4, 2),
    (4, 3)]

#### math.factorial

    [ins] In [22]: math.factorial(4)                                  
    Out[22]: 24

* permutations A(n,m)

        A(n,m) = n! / (n-m)!

* combinations C(m,n)

        C(n,m) = A(n,m) / m! = n! / (n-m)!m!

#### reduce (leetcode)

```python
from functools import reduce
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if 1 in [n, m]: return 1
        return reduce(lambda x, y: x*y, range(n, n + m - 1)) / reduce(lambda x, y: x*y, range(1, m))
S = Solution()
s = S.uniquePaths(10, 10)
print(s)
```


