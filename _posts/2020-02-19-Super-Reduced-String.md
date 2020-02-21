---
layout: post
title: "Super Reduced String"
published: true
created:  2020 Feb 19 11:04:01 PM
tags: [python, string, recursive, list, hackerrank, stringtips, easy, medium]
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
    if len(s)==1: return s
    if len(s)==2: return "Empty String" if s[0] == s[1] else s
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            return superReducedString(s[0:i]+s[i+2:])
            break
    return s
```

## ping

### no recursion

```python
def superReducedString(s):
    res, l = [], list(s)        #convert to list, so we can del
    while len(l) >= 2:          #avoid range hell, use while + del
        if l[0] is l[1]:        # if dup pairs are found, remove them
            l.pop(0);l.pop(0)
        else:                   # check if match with the last item in res
            if res and l[0] is res[-1]:
                res.pop(); l.pop(0)
            else:
                res.extend([l.pop(0), l.pop(0)])
    if l:                       # the (possible) leftover one
        if res and l[0] is res[-1]:
            res.pop(); l.pop()
        else:
            res.append(l.pop())
    return "".join(res) or "Empty String"
```

### test

```python
s='aaabccddd'
superReducedString(s)
s='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
superReducedString(s)
s='ppffccmmssnnhhbbmmggxxaaooeeqqeennffzzaaeeyyaaggggeessvvssggbbccnnrrjjxxuuzzbbjjrruuaaccaaoommkkkkxx'
superReducedString(s)
s='baabc'
superReducedString(s)
s='dqrrqd'
superReducedString(s)
s='daqrrqad'
superReducedString(s)
s='a'
superReducedString(s)
s='acdqglrfkqyuqfjkxyqvnrtysfrzrmzlygfveulqfpdbhlqdqrrqdqlhbdpfqluevfgylzmrzrfsytrnvqyxkjfquyqkfrlacdqj'
superReducedString(s)

```

## tips

* how to delete in strings?
  - convert to list, delete item, then join back
  - compose a new string and reassign


