---
layout: post
title: "yanghui triangle"
published: true
created:  2020 Jan 03 03:58:31 PM
tags: [python, generator, zip, liaoxuefeng, goodone]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# generator: yanghui triangle

## solution

```python
def yanghui_tri():
    ret = [1]
    while True:
        yield ret
        for i in range(1, len(ret)):
            ret[i] = pre[i] + pre[i - 1]
        ret.append(1)
        pre = ret[:]
```

    [1]
    [1, 1]
    [1, 2, 1]
    [1, 3, 3, 1]
    [1, 4, 6, 4, 1]
    [1, 5, 10, 10, 5, 1]
    [1, 6, 15, 20, 15, 6, 1]
    [1, 7, 21, 35, 35, 21, 7, 1]
    [1, 8, 28, 56, 70, 56, 28, 8, 1]
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]

## zb solution

```python
def yanghui_triangles():
    L = [1]
    while True:
        yield L
        L = [sum(i) for i in zip([0]+L, L+[0])]
```

illustration:

    [1]
    ||
    vv
    [0, 1]
            =zip=> (0,1), (1,0) =sum=> [1,1]
    [1, 0]

    [1, 1]
    ||
    vv
    [0, 1, 1]
            =zip=> (0,1), (1,1), (1,0) =sum=> [1,2,1]
    [1, 1, 0]


## about zip

zip

    In [45]: a = [1,2,3]
        ...: b = [4,5,6]
        ...: c = [4,5,6,7,8]

    In [58]: z=zip(a,b)
    In [60]: from collections import Iterable
    In [61]: isinstance(z, Iterable)
    Out[61]: True

    In [46]: x=list(z)

    In [47]: x
    Out[47]: [(1, 4), (2, 5), (3, 6)]

unzip: zip(*...)

    In [49]: y=zip(*z)

    In [50]: y
    Out[50]: <zip at 0x7f50fd2bb808>

    In [51]: a1,a2=y

    In [52]: a1
    Out[52]: (1, 2, 3)

    In [53]: a2
    Out[53]: (4, 5, 6)

    In [54]: a1,a2,a3=y
    ---------------------------------------------------------------------------
    ValueError                                Traceback (most recent call last)
    <ipython-input-54-41d44e776e2a> in <module>
    ----> 1 a1,a2,a3=y

    ValueError: not enough values to unpack (expected 3, got 0)


## test

```python
n=0
for t in yanghui_tri():
    print(" "*(10-n),t)
    n=n+1
    if n==10:
        break
```


               [1]
              [1, 1]
             [1, 2, 1]
            [1, 3, 3, 1]
           [1, 4, 6, 4, 1]
          [1, 5, 10, 10, 5, 1]
         [1, 6, 15, 20, 15, 6, 1]
        [1, 7, 21, 35, 35, 21, 7, 1]
       [1, 8, 28, 56, 70, 56, 28, 8, 1]
      [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
