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

## owen

```python
class Solution:
    def allipaddress(self, ipstr):
        #0/8 is reversed by IANA#        
        if ipstr[0]=="0":
            return self.allipaddress(ipstr[1:])

        #check if the len is valid#
        if len(ipstr)<4 or len(ipstr)>12 or not ipstr:
            return []

        list1=[]
        #only need to put 3 dots,so just use 3 for #
        for i in range(0,3):
            if ipstr[i+1]!="0" and  int(ipstr[0:i+1])<256:
                temp1=ipstr[0:i+1]+"."
                layer1=ipstr[i+1:]
                for j in range(0,3):
                    if j<len(layer1)-1 and layer1[j+1]!="0" and int(layer1[0:j+1])<256:
                        if layer1[j+1]!="0" and int(layer1[0:j+1])<256:
                            temp2=layer1[0:j+1]+"."
                            layer2=layer1[j+1:]
                            for z in range(0,3):
                                if z+1<len(layer2) and layer2[z+1]!="0" and int(layer2[0:z+1])<256:
                                    if int(layer2[z+1:])<256:
                                        temp3=layer2[0:z+1]+"."+layer2[z+1:]
                                        list1.append(temp1+temp2+temp3)
        return list1
```



## test result

    k=Solution()
    print k.allipaddress("1111111111")

    ['1.111.111.111', '11.11.111.111', '11.111.11.111', '11.111.111.11', '111.1.111.111', '111.11.11.111', '111.11.111.11', '111.111.1.111', '111.111.11.11', '111.111.111.1']

## wangmazi

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

## test

```python
S=Solution()
ipstr="987654321"
ipstr="12345678"
S.restoreIpAddresses(ipstr)
```
Out[16]: ['1.234.56.78', '12.34.56.78', '123.4.56.78', '123.45.6.78', '123.45.67.8']

## run code manually


```python
ipstr="12345678"
ips=[]
dfs(ipstr, 0, ips, '')

  sub0==4? no its 0
  for i in range(1,4):
    i==1
    i<=len(ipstr)==8? yes
      int(ipstr[:1])==1<=255? yes
        dfs(ipstr[1:]=='2345678', sub+1==1, ips([]), ''+'.'+ipstr[:1]=='.1')

          sub1==4? no
          for i in range(1,4):
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
                          if 1<=len(ipstr)==len(345678)==6: yes
                            if int(ipstr[:1]=='4')==4 <= 255? yes
                              dfs(ipstr[1:]=='5678', sub3+1==4, ips([]), ''+'.'+ipstr[:1]=='.4')

                                sub4==4? yes
                                  if ipstr('5678')==''? no
                                    skip
                                  return
                          i=2
                          if 2<=len(ipstr)==len(345678)==6: yes
                            if int(ipstr[:2]=='45')==45 <= 255? yes
                              dfs(ipstr[2:]=='678', sub3+1==4, ips([]), ''+'.'+ipstr[:2]=='.45')

                                sub4==4? yes
                                  if ipstr('678')==''? no
                                    skip
                                  return
                          i=3
                          if 3<=len(ipstr)==len(345678)==6: yes
                            if int(ipstr[:3]=='456')==456 <= 255? no
```
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
