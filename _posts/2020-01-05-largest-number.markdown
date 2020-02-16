---
layout: post
title: "largest number"
published: true
created:  2020 Jan 05 07:54:57 PM
tags: [lintcode, python, sorted, join, lambda, functools, wangmazi]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# largest-number

https://www.lintcode.com/problem/largest-number/description?_from=ladder&&fromId=99

## wangmazi

py2:

```python
class Solution:    
    # @param num: A list of non negative integers
    # @return: A string
    def largestNumber(self, num):
        nums = sorted(
            nums, 
            cmp=lambda x, y: 1 if str(x) + str(y) < str(y) + str(x) else -1
        )
        largest = ''.join([str(x) for x in nums])
        i, length = 0, len(largest)
        while i + 1 < length:
            if largest[i] != '0':
                break
            i += 1
        return largest[i:]
```

py3:

```python
class Solution:    
    # @param num: A list of non negative integers
    # @return: A string
    def largestNumber(self, num):
        import functools
        nums = sorted(
            nums, 
            key=functools.cmp_to_key(
                lambda x, y: 1 if str(x) + str(y) < str(y) + str(x) else -1
            )
        )
        largest = ''.join([str(x) for x in nums])
        i, length = 0, len(largest)
        while i + 1 < length:
            if largest[i] != '0':
                break
            i += 1
        return largest[i:]
```


## sorted in p2

p2: `sorted` with `cmp`

    In [1]: nums=[2, 20, 23,3]

    In [2]: nums = sorted(nums, cmp=lambda x, y: 1 if str(x) + str(y) < str(y) + str
       ...: (x) else -1)

            In [3]: nums
            Out[3]: [3, 23, 2, 20]

            In [4]: nums = sorted(nums, cmp=lambda x, y: -1 if str(x) + str(y) < str(y) + st
               ...: r(x) else 1)

            In [5]: nums
            Out[5]: [20, 2, 23, 3]

    In [6]: 'a' < 'b'
    Out[6]: True

    In [7]: 'ab' < 'ba'
    Out[7]: True

the cmp logic is: convert x, y comparison to xy yx comparison.
making `x+y < y+x` to return 1 to indicate: 'make sure in the sorted list: xy is less than yx'

    x+y < y+x == -1 => x b4 y => [x, y]
    x+y > y+x == 1 => x after y => [y, x]

therefore, take:

    [2, 20]
     x, y

will get:

    x2+y20=220 > y20+x2=202 => 1 => [x, y] => [2, 20]

## sorted in p3

p3: `sorted` with `key` and `functools.cmp_to_key`

```python
import functools
l = [1, 9, 92, 3, 12, 7]
a = sorted(l, key=functools.cmp_to_key(lambda x, y: 1 if str(x) + str(y) < str(y) + str(x) else -1))
print("".join([str(c) for c in a]))
```
