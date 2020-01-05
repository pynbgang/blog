---
layout: post
title: "map reduce"
published: true
created:  2020 Jan 04 07:39:29 PM
tags: [map, reduce, lambda, zip]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# map 

what it does:

```python
l=[x1, x2, x3, x4]
map(f, l) = [f(i) for i in l]
```

## example1: sqrt of list

```python
def f(x):
    return x * x

l=[1, 2, 3, 4, 5, 6, 7, 8, 9]
lmap=list(map(f, l))
print(lmap)
```

equals to:

```python
l=[1, 2, 3, 4, 5, 6, 7, 8, 9]
lmap = []

for n in l:
    lmap.append(f(n))
print(lmap)
```

## example2: digit to char

```python
l=[1, 2, 3, 4, 5, 6, 7, 8, 9]
list(map(str, l))
```

# reduce

what it does:

```python
l=[x1, x2, x3, x4]
reduce(f, l) = f(f(f(x1, x2), x3), x4)
```

## example1: sum

```python
from functools import reduce

l=[1, 3, 5, 7, 9]

def add(x, y):
  return x + y

reduce(add, l)
```

output:

    25

## example2: list to num


```python
from functools import reduce

def fn(x, y):
    return x * 10 + y

reduce(fn, [1, 3, 5, 7, 9])
```

output:

    13579

## example3: string to num

```python
from functools import reduce
DIGITS=dict( ( zip( [i for i in '0123456789'], range(10) ) )  )

def str2int(s):

    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return DIGITS[s]

    return reduce(fn, map(char2num, s))
```

                              +--1.map--+
                              |         |
                           ---+----     v
    return  reduce(fn, map(char2num,    s))
                   |   ----------------------
                   |        [1, 3, 5, 7, 9]
                   |              A
                   |              |
                   +---2.reduce---+


## example4: string to num (lamda version)

```python
from functools import reduce
DIGITS=dict( ( zip( [i for i in '0123456789'], range(10) ) )  )
reduce(lambda x,y: x*10+y, map(lambda s:DIGITS[s], s))
```

# resources
http://research.google.com/archive/mapreduce.html
