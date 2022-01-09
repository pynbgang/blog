---
layout: post
title: "[415] Add Strings"
author: "owen"
published: true
created:  2020 Jan 13 23:13:29 PM
tags: [python, string, int, fb, math, lstrip, assert, zip, itertools,
zip_longest, map, reduce]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[415] Add Strings](https://leetcode.com/problems/add-strings/description/)

    || * algorithms
    || * Easy (45.80%)
    || * Likes:    932
    || * Dislikes: 266
    || * Total Accepted:    181.9K
    || * Total Submissions: 386.4K
    || * Testcase Example:  '"0"\n"0"'
    || * Source Code:       415.add-strings.py
    ||
    || Given two non-negative integers num1 and num2 represented as string,
    return the sum of num1 and num2.
    ||
    || Note:
    ||
    || The length of both num1 and num2 is < 5100.
    || Both num1 and num2 contains only digits 0-9.
    || Both num1 and num2 does not contain any leading zero.
    || You must not use any built-in BigInteger library or convert the inputs
    || to integer directly.

## ping

### w/o int str

```python
def addtwostring(str1,str2):
    str2num, num2str = dict((zip('0123456789', range(10)))), dict((zip(range(10), '0123456789')))
    l1, l2 = [i for i in str1][::-1], [i for i in str2][::-1]
    if len(l1) >= len(l2): l1, l2 = l2, l1
    for i in range(len(l2)):
        l2[i] = str2num[l1[i]]+str2num[l2[i]] if i < len(l1) else str2num[l2[i]]
    l2.append(0)
    for i in range(len(l2)-1):
        l2[i], l2[i+1] = l2[i] % 10, l2[i+1] + l2[i] // 10
    return "0" if str1==str2=='0' else ''.join(num2str[i] for i in l2)[::-1].lstrip('0')
```

### comments/tests, most readable


     123   3, 2, 1
    6789   9, 8, 7, 6
    ---    ==========
    l2:   12, 10, 8, 6
    l2:   2,  1,  9, 6, 0
          21960
          06912
          6912

```python
def addtwostring(str1,str2):
    # char <--> digit mapping
    # str2num={'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    str2num=dict((zip('0123456789', range(10))))  #generate mapping while avoid
    num2str={str2num[k]:k for k in str2num}       #using 'int' and 'str'

    # string to reverse list
    # str1: '123' -> ['1','2','3']     -> ['3','2','1']
    # str2:  '49'  ->    ['4','9']     -> ['9','4']
    l1, l2 = [s for s in str1][::-1] , [s for s in str2][::-1]
    #or,
    #l1, l2 = reversed(str1), reversed(str2)
    #l1, l2 = map(reversed, (str1, str2)) 

    # make sure l2 is the longer one
    if len(l1) >= len(l2): l1, l2 = l2, l1

    # convert to digit and plus the 2 lists -> [12, 6, 1]
    for i in range(len(l2)):
        l2[i] = str2num[l1[i]]+str2num[l2[i]] if i < len(l1) else str2num[l2[i]]

    # give one more digit for carry: [12, 6, 1, 0]
    l2.append(0)

    # process carry, for each num, keep only ones, contribute the tens
    # [12, 6, 1, 0]
    # [2, 7, 1, 0]
    for i in range(len(l2)-1):
        l2[i], l2[i+1] = l2[i] % 10, l2[i+1] + l2[i] // 10

    # back to string, reverse, and remove leading '0'
    # [2, 7, 1, 0] -> "2710" -> "0172" -> "172"
    return "0" if str1==str2=='0' else ''.join(num2str[i] for i in l2)[::-1].lstrip('0')


# tests:
str1, str2 = '123', '456'
assert addtwostring(str1, str2) == str(int(str1) + int(str2)), "wrong!"
str1, str2 = '999', '1999'
assert addtwostring(str1, str2) == str(int(str1) + int(str2)), "wrong!"
str1, str2 = '0999', '1999'
assert addtwostring(str1, str2) == str(int(str1) + int(str2)), "wrong!"
str1, str2 = '011', '1'
assert addtwostring(str1, str2) == str(int(str1) + int(str2)), "wrong!"
```

## lmv

### orignal post

Python: 7-line & 52ms (+ 1-liner for fun)

https://leetcode.com/problems/add-strings/discuss/90449

* Lang:    python3
* Author:  dalwise
* Votes:   21

```python
def addStrings(self, num1, num2):
    z = itertools.zip_longest(num1[::-1], num2[::-1], fillvalue='0')
    res, carry, zero2 = [], 0, 2*ord('0')
    for i in z:
        cur_sum = ord(i[0]) + ord(i[1]) - zero2 + carry
        res.append(str(cur_sum % 10))
        carry = cur_sum // 10
    return ('1' if carry else '') + ''.join(res[::-1])
```

The above I think would be the expected answer in an interview. But just for fun
based on a similar idea we can have a (rather long :-) one-liner. It technically
satisfies the problem conditions, although it may warrant disqualification from
the contest, depending on interpretation:

 - "You must not use any built-in BigInteger library" -> I don't use a library;
   I am just making use of the fact that Python's standard int supports
   arbitrarily large integers.
 - "or convert the inputs to integer directly" -> I don't; I sum them digit by
   digit. It is the result that I convert to integer and back.

Formated for added clarity, although everything can be put on the same line:

```python
def addStrings(self, num1, num2):
     return str(
              reduce(lambda a, b: 10*a + b,
                 map(lambda x: ord(x[0])+ord(x[1])-2*ord('0'),
                   list(itertools.zip_longest(num1[::-1], num2[::-1], fillvalue='0'))[::-1]
                 )
              )
            )
```

Would the one liner be acceptable in the contest?

### with comments


```python
class Solution:     #lmv
    def addStrings(self, num1, num2):
        #num1="3451"; num2="823"
        #num1="1543"; num2="328"
        #      1543
        #      328
        #z=[('1', '3'), ('5', '2'), ('4', '8'), ('3', '0')]
        z = itertools.zip_longest(num1[::-1], num2[::-1], fillvalue='0')
        res, carry, zero2 = [], 0, 2*ord('0')
        for i in z:
            #cur_sum = ord(i[0]) - ord('0') + ord(i[1]) - ord('0') + carry
            cur_sum = ord(i[0]) + ord(i[1]) - zero2 + carry
            res.append(str(cur_sum % 10))
            carry = cur_sum // 10
        return ('1' if carry else '') + ''.join(res[::-1])
```

### oneliner version

```python
class Solution:     #lmv
    def addStrings(self, num1, num2):
        return str(
            reduce(lambda a, b: 10*a + b,
                map(lambda x: ord(x[0])+ord(x[1])-2*ord('0'),
                    list(itertools.zip_longest(num1[::-1], num2[::-1], fillvalue='0'))[::-1]
                )
            )
        )
```

    num1="3451"; num2="823"

    [ins] In [70]: l=list(itertools.zip_longest(num1[::-1],
            ...: num2[::-1], fillvalue='0'))

    [ins] In [72]: l
    Out[72]: [('1', '3'), ('5', '2'), ('4', '8'), ('3', '0')
    ]

    [ins] In [71]: l[::-1]
    Out[71]: [('3', '0'), ('4', '8'), ('5', '2'), ('1', '3')
    ]

    [ins] In [74]: l1=list(map(lambda x: ord(x[0])+ord(x[1])
            ...: -2*ord('0'),l))

    [ins] In [75]: l1
    Out[75]: [4, 7, 12, 3]

    [ins] In [78]: reduce(lambda a, b: 10*a+b, l1)
    Out[78]: 4823

### problem (jj/owen)

in reduce 10*a+b may not satisfy the requirement

## takeaways

* str to list: `list(str1), [i for i in str1]`
* list to str: `"".join(list1)`
* list x N: `[0,1] * 10`
* list1+list2: `list1.extend(list2)`
* reverse str/list: `str1/list1[::-1]`
* iterate reversely: `range(len(str1)-1, -1, -1)`
* `dict(zip(seq1, seq2))`
* `zip_longest`

## code (owen in field)

重点

- 不能直接更换字符串到数字
- 需要考虑到一些特殊的CASE比如进位
- 这个CODE里没有COVER这个情况如果某个输入是"00000012312313131"
- 不能多位数相加 (可以个位)

```python
def addtwostring(str1,str2):
    if not str1 and str2:
        return str2
    if not str2 and str1:
        return str1
    if len(str2)>len(str1):
        return addtwostring(str2,str1)
    l1=list(str1)
    l2=["0"]*(len(str1)-len(str2))+list(str2)
    listcarry=[0]+[0]*len(str1)
    sumstr=""
    for i in range(len(l1)-1,-1,-1):
        temp=int(l1[i])+int(l2[i])+listcarry[i+1]
        if temp<10:
            sumstr+=str(temp)
        else:
            sumstr+=str(temp)[-1]
            listcarry[i]=1
    if listcarry[0]==1:
        return "1"+sumstr[::-1]
    return sumstr[::-1]
```

