---
layout: post
title: "valid-ip-address-list"
date: 2020-01-22
author: "Owen"
tags: 
    - list
    - google
    - python
    - medium
    - dfs

created:  2020 Jan 22 11:35:49 PM
categories: [tech]
published: true

---


TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [restore-ip-addresses](https://www.lintcode.com/problem/restore-ip-addresses/description)

## owen1

```python
class Solution:
    """
    @param s: the IP string
    @return: All possible valid IP addresses
    """
    def restoreIpAddresses(self, s):
        if not s or len(s)<=1:
            return []
        ipstr=s
        list1=[]
        if len(ipstr)<4 or len(ipstr)>12 or not ipstr:
            return []
        for i in range(0,3):
            if  self.helper(ipstr[0:i+1]) and int(ipstr[0:i+1])<256:
                temp1=ipstr[0:i+1]+"."
                layer1=ipstr[i+1:]
                for j in range(0,3):
                    if j<len(layer1)-1  and int(layer1[0:j+1])<256 and self.helper(layer1[0:j+1]):
                        temp2=layer1[0:j+1]+"."
                        layer2=layer1[j+1:]
                        for z in range(0,3):
                            if z<len(layer2)-1  and self.helper(layer2[0:z+1]) and self.helper(layer2[z+1:]):
                                print layer2[z+1:]
                                temp3=layer2[0:z+1]+"."+layer2[z+1:]
                                list1.append(temp1+temp2+temp3)
        return list1
    def helper(self,str1):
        if len(str1)==1:
            return True
        if int(str1)>255 :
            return False
        if str1[0]!="0":
            return True
        return False 
```

## owen2

```python
class Solution:
    """
    @param s: the IP string
    @return: All possible valid IP addresses
    """
    def restoreIpAddresses(self, s):
        if not s or len(s)<=1:
            return []
        ipstr=s
        list1=[]
        if len(ipstr)<4 or len(ipstr)>12 or not ipstr:
            return []
        for i in range(0,3):
            if  self.helper(ipstr[0:i+1]) and int(ipstr[0:i+1])<256:
                temp1=ipstr[0:i+1]+"."
                layer1=ipstr[i+1:]
                for j in range(0,3):
                    if j<len(layer1)-1  and int(layer1[0:j+1])<256 and self.helper(layer1[0:j+1]):
                        temp2=layer1[0:j+1]+"."
                        layer2=layer1[j+1:]
                        for z in range(0,3):
                            if z<len(layer2)-1  and self.helper(layer2[0:z+1]) and self.helper(layer2[z+1:]):
                                print layer2[z+1:]
                                temp3=layer2[0:z+1]+"."+layer2[z+1:]
                                list1.append(temp1+temp2+temp3)
        return list1
    def helper(self,str1):
        if len(str1)==1:
            return True
        if int(str1)>255 :
            return False
        if str1[0]!="0":
            return True
        return False 
```



## owen test result

    k=Solution()
    print k.allipaddress("1111111111")

    ['1.111.111.111', '11.11.111.111', '11.111.11.111', '11.111.111.11',
    '111.1.111.111', '111.11.11.111', '111.11.111.11', '111.111.1.111',
    '111.111.11.11', '111.111.111.1']

## a solution in leetcode (best, easy to understand)

```python
class Solution:
    res=[]
    for i in [1,2,3]:
        for j in [i+1,i+2,i+3]:
            for k in [j+1,j+2,j+3]:
                if k>=len(s):
                    break
                s1,s2,s3,s4=s[:i],s[i:j],s[j:k],s[k:]
                add_ip = True
                for st in [s1,s2,s3,s4]:
                    if (st!="0" and st[0]=="0") or int(st)>255:
                        add_ip=False
                        break
                if add_ip: res.append(s1+"."+s2+"."+s3+"."+s4)
    return res
```

### idea

just brute force iterating different methods to cut in four pieces, and check each result.

    s1,s2,s3,s4=s[:i],s[i:j],s[j:k],s[k:]

i=1

    i=1, j=2, k=3,4,5
       i j k rest
      1|2|3|45678 
      1|2|34|5678
      1|2|345|678

    i=1, j=3, k=4,5,6
       i  j k rest
      1|23|4|5678
      1|23|45|678
      1|23|456|78

    i=1, j=4, k=5,6,7
      1|234|5|678
      1|234|56|78
      1|234|567|8

i=2

    i=2, j=3, k=4,5,6
      12|3|4|5678
      12|3|45|678
      12|3|456|78

    i=2, j=4, k=5,6,7
      12|34|5|678
      12|34|56|78
      12|34|567|8

    i=2, j=5, k=6,7,8
      12|34|5|678
      12|34|56|78
      12|34|567|8

i=3

    i=3, j=4, k=5,6,7
      123|4|5|678
      123|4|56|78
      123|4|567|8

    i=3, j=5, k=6,7,8
      123|45|6|78
      123|45|67|8
      123|45|678|       #<---k>=len(s): break

    i=3, j=6, k=7,8,9
      123|456|7|8
      123|456|78|       #<---k>=len(s): break
      123|456|78|       #<---k>=len(s): break

### test

```python
S=Solution()
ipstr="987654321"
ipstr="12345678"
S.restoreIpAddresses(ipstr)
```
Out[16]: ['1.234.56.78', '12.34.56.78', '123.4.56.78', '123.45.6.78', '123.45.67.8']

## wangmazi: DFS

```python
class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        def dfs(ipstr, sub, ips, ip):
            if sub == 4:               # should be 4 parts
                if ipstr == '':
                    ips.append(ip[1:]) # remove first '.'
                return
            for i in range(1, 4):      # the three ifs' order cannot be changed!
                if i <= len(ipstr):        # if i > len(s), s[:i] will make false!!
                    if int(ipstr[:i]) <= 255:
                        dfs(ipstr[i:], sub+1, ips, ip+'.'+ipstr[:i])
                    # make sure that res just can be '0.0.0.0' and remove like '00'
                    if ipstr[0] == '0': break

        ips = []
        dfs(ipstr, 0, ips, '')
        return ips
```

### run DFS code manually


```python
ipstr="12345678"
ips=[]
dfs(ipstr, 0, ips, '')

  sub0==4?
  for i in range(1,4):
    i==1
    i<=len(ipstr)==8? yes
      int(ipstr[:1])==1<=255? yes
        dfs(ipstr[1:]=='2345678', sub+1==1, ips([]), ''+'.'+ipstr[:1]=='.1')

          sub1==4? no
          for i in range(1,4):
            i==1
            i<=len(ipstr)==7? yes
              if int(ipstr[:1]=='2')==2 <= 255? yes
                dfs(ipstr[1:]=='345678', sub1+1==2, ips([]), ''+'.'+ipstr[:1]=='.2')

                  sub2==4? no
                  for i in range(1,4):
                    i=1
                    if 1<=len(ipstr)==len(345678)==6: yes
                      if int(ipstr[:1]=='3')==3 <= 255? yes
                        dfs(ipstr[1:]=='45678', sub2+1==3, ips([]), ''+'.'+ipstr[:1]=='.3')

                          sub3==4? no
                          for i in range(1,4):
                            i=1
                            if 1<=len(ipstr)==len(45678)==5: yes
                              if int(ipstr[:1]=='4')==4 <= 255? yes
                                dfs(ipstr[1:]=='5678', sub3+1==4, ips([]), ''+'.'+ipstr[:1]=='.4')

                                  sub4==4? yes
                                    if ipstr('5678')==''? no
                                      skip
                                    return
                            i=2
                            if 2<=len(ipstr)==len(45678)==5: yes
                              if int(ipstr[:2]=='45')==45 <= 255? yes
                                dfs(ipstr[2:]=='678', sub3+1==4, ips([]), ''+'.'+ipstr[:2]=='.45')

                                  sub4==4? yes
                                    if ipstr('678')==''? no
                                      skip
                                    return
                            i=3
                            if 3<=len(ipstr)==len(45678)==5: yes
                              if int(ipstr[:3]=='456')==456 <= 255? no
                              if ipstr[0]=='0'? no
                    i=2
                    if 2<=len(ipstr)==len(345678)==6: yes
                      if int(ipstr[:2]=='34')==34 <= 255? yes
                        dfs(ipstr[2:]=='5678', sub2+1==3, ips([]), ''+'.'+ipstr[:2]=='.34')

                          sub3==4? no
                          for i in range(1,4):
                            i=1
                            if 1<=len(ipstr)==len(5678)==4: yes
                              if int(ipstr[:1]=='5')==5 <= 255? yes
                                dfs(ipstr[1:]=='678', sub3+1==4, ips([]), ''+'.'+ipstr[:1]=='.5')

                                  sub4==4? yes
                                    if ipstr('5678')==''? no
                                      skip
                                    return
                            i=2
                            if 2<=len(ipstr)==len(5678)==4: yes
                              if int(ipstr[:2]=='56')==56 <= 255? yes
                                dfs(ipstr[2:]=='78', sub3+1==4, ips([]), ''+'.'+ipstr[:2]=='.56')

                                  sub4==4? yes
                                    if ipstr('5678')==''? no
                                      skip
                                    return
                            i=3
                            if 3<=len(ipstr)==len(5678)==4: yes
                              if int(ipstr[:3]=='567')==567 <= 255? no

                    i=3
                    if 3<=len(ipstr)==len(345678)==6: yes
                      if int(ipstr[:3]=='345')==345 <= 255? no
                      if ipstr[0]=='0'? no
            i==2
            i<=len(ipstr)==7? yes
              if int(ipstr[:2]=='23')==23 <= 255? yes
                dfs(ipstr[1:]=='45678', sub1+1==2, ips([]), ''+'.'+ipstr[:1]=='.23')

                  sub2==4? no
                  for i in range(1,4):
                    i=1
                    if 1<=len(ipstr)==len(345678)==6: yes
                      if int(ipstr[:1]=='3')==3 <= 255? yes
                        dfs(ipstr[1:]=='45678', sub2+1==3, ips([]), ''+'.'+ipstr[:1]=='.3')

                          sub3==4? no
                          for i in range(1,4):
                            i=1
                            if 1<=len(ipstr)==len(45678)==5: yes
                              if int(ipstr[:1]=='4')==4 <= 255? yes
                                dfs(ipstr[1:]=='5678', sub3+1==4, ips([]), ''+'.'+ipstr[:1]=='.4')

                                  sub4==4? yes
                                    if ipstr('5678')==''? no
                                      skip
                                    return
                            i=2
                            if 2<=len(ipstr)==len(45678)==5: yes
                              if int(ipstr[:2]=='45')==45 <= 255? yes
                                dfs(ipstr[2:]=='678', sub3+1==4, ips([]), ''+'.'+ipstr[:2]=='.45')

                                  sub4==4? yes
                                    if ipstr('678')==''? no
                                      skip
                                    return
                            i=3
                            if 3<=len(ipstr)==len(45678)==5: yes
                              if int(ipstr[:3]=='456')==456 <= 255? no
                              if ipstr[0]=='0'? no
                    i=2
                    if 2<=len(ipstr)==len(345678)==6: yes
                      if int(ipstr[:2]=='34')==34 <= 255? yes
                        dfs(ipstr[2:]=='5678', sub2+1==3, ips([]), ''+'.'+ipstr[:2]=='.34')
  #<---until here so far
                          sub3==4? no
                          for i in range(1,4):
                            i=1
                            if 1<=len(ipstr)==len(5678)==4: yes
                              if int(ipstr[:1]=='5')==5 <= 255? yes
                                dfs(ipstr[1:]=='678', sub3+1==4, ips([]), ''+'.'+ipstr[:1]=='.5')

                                  sub4==4? yes
                                    if ipstr('5678')==''? no
                                      skip
                                    return
                            i=2
                            if 2<=len(ipstr)==len(5678)==4: yes
                              if int(ipstr[:2]=='56')==56 <= 255? yes
                                dfs(ipstr[2:]=='78', sub3+1==4, ips([]), ''+'.'+ipstr[:2]=='.56')

                                  sub4==4? yes
                                    if ipstr('5678')==''? no
                                      skip
                                    return
                            i=3
                            if 3<=len(ipstr)==len(5678)==4: yes
                              if int(ipstr[:3]=='567')==567 <= 255? no

                    i=3
                    if 3<=len(ipstr)==len(345678)==6: yes
                      if int(ipstr[:3]=='345')==345 <= 255? no
                      if ipstr[0]=='0'? no
