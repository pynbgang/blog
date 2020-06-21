---
layout: post
title: "iterator vs iterable"
published: true
created:  2020 Jan 11 12:41:31 PM
tags: [python, iterable, iterator, generator, zip, python2]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -


# all about Iterable/iterator/generator

## facts

iterable::  anything that can be iterated over: `for i in iter1`

- string/list/tuple/dict/set
- iterator (e.g. generator)

iterator:: the `agent` that perform the iteration.

- objects support `next()`
- create from:
  - BIFs (e.g enumerate, zip, reversed, list(), etc)
  - generator
- if iter1 is already an iterator, then `iter(iter1) is iter1`

____
Python 的 Iterator 对象表示的是一个数据流， Iterator 对象可
以被 next()函数调用并不断返回下一个数据，直到没有数据时抛出
StopIteration 错误。可以把这个数据流看做是一个有序序列，但我们却
不能提前知道序列的长度，只能不断通过 next()函数实现按需计算下一
个数据，所以 Iterator 的计算是惰性的，只有在需要返回下一个数据时
它才会计算。
Iterator 甚至可以表示一个无限大的数据流，例如全体自然数。而使用
list 是永远不可能存储全体自然数的。
____

.convert between iterable/list

                list()
    iterable ----------> list
    list     <---------- iterable
                iter()

- `iter()`: iterable(e.g. list) to iterator
- `list()`: iterator to a list


## test cases


```python
l=[1,2,3,4]
i = iter(l)
list(zip(i, i))         #zip do "next" on one same iterator
[(1, 2), (3, 4)]
```

```python
l=[1,2,3,4]
list(zip(l, l))         #zip do "next" on two diff iterator
[(1, 1), (2, 2), (3, 3), (4, 4)]
```

why? because:

```python
l=[1,2,3,4]
i=iter(l); iter(i) is i         #True
iter(l) is not iter(l)          #True
```

and what zip does:

- convert both params to iterator
- next() on both get a new tuple
- first test give **same** iterators
- 2nd test give **two** iterators (same content though)

## iterable or not

    In [528]: from collections import Iterable

    In [529]: isinstance('abc',Iterable)
    Out[529]: True

    In [530]: isinstance(100,Iterable)
    Out[530]: False

    In [11]: isinstance(range(2), Iterable)
    Out[11]: True

## iterators or not? (support next() or not)

next: will be called by 'for/while' loop internally.

### py3:

    In [72]: l
    Out[72]: [2, 1, 0, 0]

not an iterator

    In [14]: next(l)
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-14-cdc8a39da60d> in <module>
    ----> 1 next(l)

    TypeError: 'list' object is not an iterator

convert to iterator

    In [74]: iter1=iter(l)

    In [73]: iter1
    Out[73]: <list_iterator at 0x7f672bfe5b38>

    In [76]: next(iter1)
    Out[76]: 2

    In [77]: next(iter1)
    Out[77]: 1

### py2

    >>> l
    ['a', 'b', 'c']
    >>> iter1=iter(l)
    >>> iter1.next()
    'a'
    >>> iter1.next()
    'b'
    >>> iter1.next()
    'c'
    >>> iter1.next()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      StopIteration
      >>>

- py2 only?

* iterkeys
* itervalues
* iteritems

