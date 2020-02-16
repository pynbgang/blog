---
layout: post
title: "Closest Numbers"
published: true
created:  2020 Feb 14 11:04:01 AM
tags: [python, sort, list, hackerrank, brute force]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# Closest Numbers

## [hackerrank](https://www.hackerrank.com/challenges/closest-numbers/problem)

Sorting is useful as the first step in many different tasks. The most common
task is to make finding things easier, but there are other uses as well. In
this case, it will make it easier to determine which pair or pairs of elements
have the smallest absolute difference between them.
                                                                                                                                                                                                                                                                                        g
For example, if you've got the list , sort it as  to see that several pairs
have the minimum difference of : . The return array would be .

Given a list of unsorted integers, , find the pair of elements that have the
smallest absolute difference between them. If there are multiple pairs, find
them all.

Function Description
Complete the closestNumbers function in the editor below. It must return an array of integers as described.

closestNumbers has the following parameter(s):

arr: an array of integers
Input Format

The first line contains a single integer , the length of .
The second line contains  space-separated integers, .

Constraints

## owen

```python
def closestNumbers(arr):
    if not arr or len(arr)<=1:
        return
    arr.sort()
    if len(arr)==2:
        print arr[0],arr[1]
        return
    list1=[[arr[0],arr[1],arr[1]-arr[0]]]
    for i in range(2,len(arr)):
        if arr[i]-arr[i-1]>list1[-1][2]:
            continue
        elif arr[i]-arr[i-1]==list1[-1][2]:
            list1.append([arr[i-1],arr[i],arr[i]-arr[i-1]])
        else:
            list1=[]
            list1.append([arr[i-1],arr[i],arr[i]-arr[i-1]])
    temp1=[]
    for i in list1:
        temp1.append(i[0])
        temp1.append(i[1])
    return temp1
```

## ping: brute force

```python
def closestNumbers(arr):
    res=[]
    arr.sort()
    mingap=min(arr[i] - arr[i-1] for i in range(1, len(arr)))
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] == mingap:
            res.extend([arr[i-1], arr[i]])
    return res
```

arr= [-5, 15, 25, 71, 63]
closestNumbers(arr)
Out[9]: [63, 71]

## test output

    Input (stdin)
    -5 15 25 71 63
    Output
    63 71


