---
layout: post
title: "Super Reduced String"
published: true
created:  2020 Feb 19 11:04:01 PM
tags: [python, string, recursive]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [Super Reduced String](https://www.hackerrank.com/challenges/reduced-string/problem)

Steve has a string of lowercase characters in range ascii[‘a’..’z’]. He wants
to reduce the string to its shortest length by doing a series of operations. In
each operation he selects a pair of adjacent lowercase letters that match, and
he deletes them. For instance, the string aab could be shortened to b in one
operation.

Steve’s task is to delete as many characters as possible using this method and
print the resulting string. If the final string is empty, print Empty String

Function Description

Complete the superReducedString function in the editor below. It should return
the super reduced string or Empty String if the final string is empty.

superReducedString has the following parameter(s):

Sample Input 0

aaabccddd

Sample Output 0

abd

Explanation 0

Steve performs the following sequence of operations to get the final string:

aaabccddd → abccddd → abddd → abd


## ideas

1. recursive
2. break

## owen

```python
def superReducedString(s):
    if len(s)==1:
        return s
    if len(s)==2:
        if s[0]==s[-1]:
            return "Empty String"
        else:
            return s
    len1=len(s)
    for i in range(len1-1):
        if s[i]==s[i+1]:
            print s,i,s[0:i]+s[i+2:]
            return superReducedString(s[0:i]+s[i+2:])
            break
        else:
            flag = True
    if flag:
        return s

```


## ping: no recursion

```python
def superReducedString(s):
    res=[]
    i = 0
    l=list(s)
    while l:
        if res and res[-1]: 
            l.insert(0, res.pop())
        while len(l) >= 2 and l[0] == l[1]:
            l.pop(0);l.pop(0)
        if len(l) >= 2:
            res.extend([l.pop(0), l.pop(0)])
        elif l:
            res.extend([l.pop(0)])
    return "".join(res) or "Empty String"

```

not pass yet `baab`

test:

```python
s='aaabccddd'
s='ppffccmmssnnhhbbmmggxxaaooeeqqeennffzzaaeeyyaaggggeessvvssggbbccnnrrjjxxuuzzbbjjrruuaaccaaoommkkkkxx'
s='baab'
superReducedString(s)

```


