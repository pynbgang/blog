---
layout: post
title: "valid-ip-address-list"
subtitle: ""
date: 2020-01-22
author: "Owen"
tags: 
    - list
    - for
    - Google
    - onsite
    - python

created:  2020 Jan 22 11:35:49 PM
categories: [tech]
published: true

---


TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# Code

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



# test result
k=Solution()
print k.allipaddress("1111111111")

['1.111.111.111', '11.11.111.111', '11.111.11.111', '11.111.111.11', '111.1.111.111', '111.11.11.111', '111.11.111.11', '111.111.1.111', '111.111.11.11', '111.111.111.1']

