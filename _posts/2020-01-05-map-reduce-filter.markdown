---
layout: post
title: "map reduce filter"
published: true
created:  2020 Jan 04 07:39:29 PM
tags: [python, functools, map, reduce, filter, lambda, zip, prime, generator, liaoxuefeng, math, reversed]
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
map(f, l)
#same as
[f(i) for i in l]
```

高阶函数 - 函数做参数。

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

## example2: sum of list


```python
from functools import reduce

def fn(x, y):
    return x * 10 + y

reduce(fn, [1, 3, 5, 7, 9])
```

output:

    13579

# map and reduce

## example3: implement `int()`

```python
from functools import reduce
digits=dict( ( zip('0123456789', range(10)) )  )

def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return digits[s]

    return reduce(fn, map(char2num, s))
```

how it works:

                              +--1.map--+
                              |         |
                           ---+----     v
     return reduce(fn, map(char2num,    s))
                   |                  "13579"
                   |   ----------------------
                   |     2. [1, 3, 5, 7, 9]
                   |              A
                   |              | ==> 4. 13579
                   +---3.reduce---+


## example4: implement `int()` (lamda version)

```python
from functools import reduce
digits=dict( ( zip('0123456789', range(10)) )  )
def str2int(s):
    return reduce(lambda x,y: x*10+y, map(lambda s:digits[s], s))
```

# more exercises

## exercise1: map 实现capitalize

利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

```python
def normalize(name):
    return name.capitalize()
ls = ['adam', 'LISA', 'barT']
res = list(map(normalize, ls))
print(res)

```
or:

```
ls = ['adam', 'LISA', 'barT']
res = list(map(lambda x: x.capitalize(), ls))
print(res)
```

## exercise2: reduce 实现乘法器

Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个
list并利用reduce()求积：

```python
from functools import reduce
def prod(l):
    return reduce(lambda x,y: x*y, l)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
```

## exercise3: map and reduce: str2float

利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：

### v1

```python
from functools import reduce

def str2float(s):

    digits=dict( ( zip('0123456789', range(10)) )  )

    def map1(c):
        return digits[c] if c in '0123456789' else '.'

    def rd1(x, y):
        return x*10+y

    def rd2(x, y):
        return x*0.1+y

    #121.23 => [1, 2, 1, '.', 2, 3]
    l=list(map(map1, s))

    #l1=[1, 2, 1]
    l1=l[0:l.index('.')]

    #l2=[2, 3]
    l2=l[l.index('.')+1:]

    return reduce(rd1, l1) + reduce(rd2, reversed(l2)) * 0.1

print('str2float(\'123.456\') =', str2float('123.456'))

if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

```

                                            [3, 2]
                                         -----------
    return reduce(rd1, l1) + reduce(rd2, reversed(l2)) * 0.1
           --------------    -------------------------
           121                      2.3

### v2: lambda

```python
from functools import reduce
def str2float(s):
    digits=dict( zip('0123456789', range(10)) )
    l=list(map(lambda c: digits[c] if c in '0123456789' else '.', s))
    l1, l2 = l[0:l.index('.')], l[l.index('.')+1:]
    return reduce(lambda x,y:x*10+y, l1) + reduce(lambda x,y:x*0.1+y, reversed(l2)) * 0.1

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

```


### v3: zb solution

```python
from functools import reduce
def str2float(s):
    digits=dict( zip('0123456789', range(10)) ) #build str to int map
    l=list(map(lambda c: digits[c] if c in '0123456789' else '.', s)) #to list
    power, div = len(l)-l.index('.')-1, 1       #get power 123.23 => 2
    for i in range(power): div *= 10            #get div (/100) per power(2)
    l.pop(l.index('.'))                         #remove '.' in list
    return reduce(lambda x,y:x*10+y, l) / div   #integer(12323) / div(100)

print('str2float(\'123.456\') =', str2float('123.456'))

if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

```

1. map: "123.23" => [1, 2, 3, '.', 2, 3]
2. locate "." position: 3
3. base on that, calculate how much to divide (100) if
   we want to get 123.23 from 12323
3. remove "." => [1,2,3,2,3]
4. reduce: [1,2,3,2,3] => 12323
5. 12323/100 = 123.23

# filter

## filter example1: get odd number from list

```python
def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
```

## filter example2: remove empty string from list

```python
def not_empty(s):
    return s and s.strip()

list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
```

## filter example3: find primes

```python
#先构造一个从3开始的奇数序列
#[3, 5, 7]
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

#然后定义一个筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0

#最后，定义一个生成器，不断返回下一个素数
def primes():
    yield 2
    #[3, 5, 7]
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        #i for i in [3, 5, 7] if i % 3
        it = filter(_not_divisible(n), it) # 构造新序列

# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
```

idea:

* 素数必然在奇数里找
* 每一个奇数, 只要不被所有比自己小的奇数整除, 必然是素数

运行：

    yield 2
    it=[3,5,7,9,11,13,15,17,19,21,23,25]
    loop:
        yield next(it) => yield 3
        it=[i for i in [3,5,7,9,11,13,15,17,19,21,23,25] if i % 3] 
        =>          it=[x,5,7,x,11,13,xx,17,19,xx,23,25]
        =>          it=[5,7,11,13,17,19,23,25]
        最小的数'5' 已经尝试过所有比自己小的奇数(3)，都不能整除，所以5必是素数
        primes() return 2, print 2

        yield next(it) => yield 5
        it=[i for i in [5,7,11,13,17,19,23,25] if i % 5]
        =>          it=[x,7,11,13,17,19,23,xx]
        =>          it=[7,11,13,17,19,23]
        最小的数'7' 已经尝试过所有比自己小的奇数(3,5)，都不能整除，所以7必是素数
        primes() return 3, print 3

        yield next(it) => yield 7
        ......
        primes() return 5, print 5

        ......


## filter exercises1

回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：


```python
def is_palindrome(n):
    return str(n) == str(n)[::-1]

# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))

if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
```

# resources
http://research.google.com/archive/mapreduce.html
