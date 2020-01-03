---
layout: post
title: "yanghui triangle"
published: true
created:  2020 Jan 03 03:58:31 PM
tags: [python, generator, liaoxuefeng]
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
def triangles():
    L = [1]
    while True:
        yield L
        L = [sum(i) for i in zip([0]+L, L+[0])]
```


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

