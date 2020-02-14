---
layout: post
title: "prime-factorization"
published: true
date: 2020-02-11
created:  2020 Feb 13 02:46:27 PM
tags: [python, math, lintcode, easy, brute force]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [prime-factorization](https://www.lintcode.com/problem/prime-factorization/description?_from=ladder&&fromId=99)

Prime factorize a given integer.

You should sort the factors in ascending order.

Have you met this question in a real interview?  
Example
Example 1:

Input: 10
Output: [2, 5]
Example 2:

Input: 660
Output: [2, 2, 3, 5, 11]

## jj original: brute force: timeout

```python
def primeFactorization(self, num):
    # write your code here
    rtn, pri = [], 2
    while pri <= num:
        if num % pri == 0:
            rtn.append(pri)
            num = num / pri
        else:
            pri += 1
    return rtn
```

## jj (best)

```python
def primeFactorization(self, num):
    # write your code here
    rtn, pri, ori = [], 2, num
    while pri * pri <= ori:
        if num % pri == 0:
            rtn.append(pri)
            num = num / pri
        else:
            pri += 1
    return rtn if num == 1 else rtn + [int(num)]
```

## wangmazi: original

```python
class Solution:
    # @param {int} num an integer
    # @return {int[]} an integer array
    def primeFactorization(self, num):
        # Write your code here

        ##step1: get sqrt: up
        up = int(math.sqrt(num)) + 1

        ##step2: using 素数筛 to get all primes under 'up'
        f = [0 for x in xrange(up)]
        prime = []
        for i in xrange(2, up):
            if f[i] == 0:
                prime.append(i)
                for j in xrange(i * i, up, i):
                    f[j] = 1

        ##using these primes to get all the prime factors of a num
        rt = []
        for a in prime:
            while num % a == 0:
                rt.append(a)
                num /= a
        if num != 1:
            rt.append(num)
        return rt
```

### tips:

- the idea: find all primes under sqrt(num), and iterate them to find all prime
  factors of num

- why sqrt(num) ?

    what is the biggest primes factors for num?
    assuming num has 2 biggest primes: AxB
    then one of them (assuming A) has to be `<` sqrt(num)
    find A then B(bigger than sqrt(num)) is easy to know

- how to find all primes under a number (A)

    素数筛

### wangmazi: print to debug


```python
class Solution:
    # @param {int} num an integer
    # @return {int[]} an integer array
    def primeFactorization(self, num):
        # Write your code here

        num=100
        print('num is: ',num)
        up = int(math.sqrt(num)) + 1
        print('up is: ',up)
        f = [0 for x in range(up)]
        print('f is: ',f)

        prime = []
        for i in range(2, up):
            print('i=',i)
            if f[i] == 0:
                print('f=',f)
                prime.append(i)
                print('append into prime, prime=',prime)
                print('j start from ixi=', i*i)
                for j in range(i * i, up, i):
                    print('j=',j)
                    f[j] = 1
                    print('set f[',j,'], f=',f)
                    print('j+=',i)
                print('j>up(',up,') now')
                print()

        rt = []
        for a in prime:
            while num % a == 0:
                rt.append(a)
                num /= a
        if num != 1:
            rt.append(num)
        print('result is:', rt)
        return rt
```

### wangmazi: manually run the code

```python
    In [258]: num=100

    In [259]: print('num is: ',num)
    num is:  100

    In [260]: up = int(math.sqrt(num)) + 1

    In [261]: print('up is: ',up)
    up is:  11

    In [262]: f = [0 for x in range(up)]

    In [263]: print('f is: ',f)
    f is:  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    In [264]: prime = []

    In [265]: for i in range(2, up):
         ...:     print('i=',i)
         ...:     if f[i] == 0:
         ...:         print('f=',f)
         ...:         prime.append(i)
         ...:         print('append into prime, prime=',prime)
         ...:         print('j start from ixi=', i*i)
         ...:         for j in range(i * i, up, i):
         ...:             print('j=',j)
         ...:             f[j] = 1
         ...:             print('set f[',j,'], f=',f)
         ...:             print('j+=',i)
         ...:         print('j>up(',up,') now')
         ...:         print()
         ...:
    i= 2
    f= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    append into prime, prime= [2]
    j start from ixi= 4
    j= 4
    set f[ 4 ], f= [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    j+= 2
    j= 6
    set f[ 6 ], f= [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0]
    j+= 2
    j= 8
    set f[ 8 ], f= [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0]
    j+= 2
    j= 10
    set f[ 10 ], f= [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1]
    j+= 2
    j>up( 11 ) now

    i= 3
    f= [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1]
    append into prime, prime= [2, 3]
    j start from ixi= 9
    j= 9
    set f[ 9 ], f= [0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1]
    j+= 3
    j>up( 11 ) now

    i= 4
    i= 5
    f= [0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1]
    append into prime, prime= [2, 3, 5]
    j start from ixi= 25
    j>up( 11 ) now

    i= 6
    i= 7
    f= [0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1]
    append into prime, prime= [2, 3, 5, 7]
    j start from ixi= 49
    j>up( 11 ) now

    i= 8
    i= 9
    i= 10

    In [266]: rt = []

    In [267]: for a in prime:
         ...:     while num % a == 0:
         ...:         rt.append(a)
         ...:         num /= a
         ...:

    In [268]: if num != 1:
         ...:     rt.append(num)
         ...:

    In [269]: print('result is:', rt)
    result is: [2, 2, 5, 5]
```

## resources

* https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

