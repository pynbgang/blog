---
layout: post
title: "adding two stringnum"
published: true
created:  2020 Jan 13 23:13:29 PM
tags: [python, string, int, fb, math]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# addtwostring

## code

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

## ping

```python
def addtwostring(str1,str2):
    str2num={'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    num2str={str2num[i]:i for i in str2num}
    l1=[i for i in str1]
    l2=[i for i in str2]

    if len(l1) >= len(l2):
        l1, l2 = l2, l1

    for i in range(len(l1)):
        l2[i] = str2num[l1[i]]+str2num[l2[i]]

    l2.reverse();l2.append(0)
    for i in range(len(l2)):
        a=l2[i]
        l2[i]=a % 10
        if a // 10:
            l2[i+1] += 1

    return ''.join([num2str[i] for i in l2])[::-1]

addtwostring('456', '789')
```





# 重点

- 不能直接更换字符串到数字
- 需要考虑到一些特殊的CASE比如进位 
- 这个CODE里没有COVER这个情况如果某个输入是"00000012312313131"
