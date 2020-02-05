---
layout: post
title: "reverse integer"
published: true
created:  2020 Feb 05 02:21:26 PM
tags: [python, easy, integer, bit]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# posted: [reverse-integer](https://leetcode.com/problems/reverse-integer/description)

https://www.lintcode.com/problem/reverse-integer/my-submissions?_from=ladder&&fromId=99

## code and test

```python
class Solution:
    if 1:  # ping

        def reverse(self, x: int) -> int:
            res = int(str(abs(x))[::-1])
            if res > 2 ** 31 - 1:
                return 0
            return res if x > 0 else -res

    """
    ✔ Accepted
    ✔ 1032/1032 cases passed (28 ms)
    ✔ Your runtime beats 78.45 % of python3 submissions
    ✔ Your memory usage beats 100 % of python3 submissions (12.6 MB)
    """

    if 0:  # ping

        def reverse(self, n):
            res=int(str(abs(n))[::-1])
            res = res if n > 0 else -res
            return 0 if res > 2 ** 31 - 1 or res < -(2 ** 31) else res


    """
    ✔ Accepted
    ✔ 1032/1032 cases passed (32 ms)
    ✔ Your runtime beats 51.57 % of python3 submissions
    ✔ Your memory usage beats 100 % of python3 submissions (12.8 MB)
    """


    if 0:  # lmv

        def reverse(self, x):
            s = (x > 0) - (x < 0)
            r = int(str(s*x)[::-1])
            return s * r * (r < 2**31)

    """
    ✔ Accepted
    ✔ 1032/1032 cases passed (32 ms)
    ✔ Your runtime beats 51.57 % of python3 submissions
    ✔ Your memory usage beats 100 % of python3 submissions (12.7 MB)
    """
```

## wangmazi (without str/int/pow/**)

```python
class Solution:
    # @param {int} n the integer to be reversed
    # @return {int} the reversed integer
    def reverseInteger(self, n):
        if n == 0:
            return 0

        neg = 1
        if n < 0:
            neg, n = -1, -n

        reverse = 0
        while n > 0:
            reverse = reverse * 10 + n % 10
            n = n / 10

        reverse = reverse * neg
        if reverse < -(1 << 31) or reverse > (1 << 31) - 1:
            return 0
        return reverse
```

## tips

- what is a signed integer:

        positive
        |
        v
        0 1 1
        1 1 1
        ^
        |
        minus

- range of a signed integer: `[2 ** (n-1), 2 ** (n-1) - 1]`, why?

    - 00000000到01111111，表示0到+127。
    - 10000001到11111111，表示-1到-127。
    - 10000000没有用到。因为如果我们把它看成-0，那么会和00000000发生重复。于是
    计算机将10000000定义为-128。

- 反码：除了符号位以外取反
- 补码：反码+1

- bit shift for power

        [ins] In [1]: 2**31 == 1<<31                                                    
        Out[1]: True

- reverse integer without str/int

        while n > 0:
            reverse = reverse * 10 + n % 10
            n = n / 10

## resources:
https://www.cnblogs.com/zhangziqiu/archive/2011/03/30/ComputerCode.html

