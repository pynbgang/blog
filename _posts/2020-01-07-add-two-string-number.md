---
layout: post
title: "max-area-of-island"
subtitle: ""
date: 2020-01-12
author: "owen"
tags: 
    - str
    - array
    - FB
    - easy
    - python

created:  2020 Jan 12 03:46:15 PM
categories: [tech]
published: true

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -



## solution (after peeping most voted solution) 

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
## takeaway 

- can not use int(str),then add them together
- need to have a list(list carry) to remember the carry info
