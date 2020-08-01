---
layout: post
title: "[415] Add Strings"
author: "owen"
published: true
created:  2020 Jan 13 23:13:29 PM
tags: [python, string, int, fb, math, lstrip, assert, zip]
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
    || Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
    || 
    || Note:
    || 
    || The length of both num1 and num2 is < 5100.
    || Both num1 and num2 contains only digits 0-9.
    || Both num1 and num2 does not contain any leading zero.
    || You must not use any built-in BigInteger library or convert the inputs to integer directly.

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

## ping: w/o int str

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

## ping(w/ comments and tests)

```python
def addtwostring(str1,str2):
    # char <--> digit mapping
    # str2num={'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    str2num=dict((zip('0123456789', range(10))))
    num2str=dict((zip(range(10), '0123456789')))

    # '123' -> ['1','2','3'] -> ['3','2','1']
    #  '49'  ->['4','9']     -> ['9','4']
    l1, l2 = [i for i in str1][::-1] , [i for i in str2][::-1]
    #or, 
    #l1, l2 = sorted(str1, reverse=True), sorted(str2, reverse=True)

    # get the longer one to iterate
    if len(l1) >= len(l2): l1, l2 = l2, l1

    # convert to digit and plus the 2 lists -> [12, 6, 1]
    for i in range(len(l2)):
        l2[i] = str2num[l1[i]]+str2num[l2[i]] if i < len(l1) else str2num[l2[i]]


    # give one more digit for carry: [12, 6, 1, 0]
    l2.append(0)

    # process carry, for each num, keep only ones, contribute the tens
    for i in range(len(l2)-1):
        l2[i], l2[i+1] = l2[i] % 10, l2[i+1] + l2[i] // 10

    # back to string, reverse, and remove leading '0'
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

Python: 7-line & 52ms (+ 1-liner for fun)

https://leetcode.com/problems/add-strings/discuss/90449

* Lang:    python3
* Author:  dalwise
* Votes:   21

```python
def addStrings(self, num1, num2):
    z = itertools.izip_longest(num1[::-1], num2[::-1], fillvalue='0')
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
                   list(itertools.izip_longest(num1[::-1], num2[::-1], fillvalue='0'))[::-1]
                 ) 
              )
            )
```

Would the one liner be acceptable in the contest?


## tips

* str to list: list(str1), [i for i in str1]
* list to str: "".join(list1)
* list x N: [0,1] * 10
* list1+list2: list1.extend(list2)
* revert str/list: str1/list1[::-1]
* iterate reversely: range(len(str1)-1, -1, -1)
* zip(seq1, seq2) => dict
