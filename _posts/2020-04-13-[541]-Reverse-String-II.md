---
layout: post
title: "[541] Reverse String II"
published: true
created:  2020 Apr 13 12:16:56 PM
tags: [python, leetcode, easy,recurisve]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[541] Reverse String II](https://leetcode.com/problems/reverse-string-ii/)

    ||Given a string and an integer k, you need to reverse the first k characters for every 2k characters 

    |counting from the start of the string. If there are less than k characters left, reverse all of them. 
      If there are less than 2k but greater than or equal to k characters, then reverse the first k characters 
      and left the other as original.
    


## Owen: follow basic rules

```python
	class Solution(object):
	    def reverseStr(self, s, k):
		if len(s)==1:return s
		if k==0:return s
		if k==len(s):return s[::-1]
		m=len(s)/k
		l=[]
		for i in range(m):
		    l.append(s[i*k:(i+1)*k])
		l.append(s[m*k:])
		str1=""
		for i in range(len(l)):
		    if i%2==0:str1+=l[i][::-1]
		    else:str1+=l[i]
		return str1
		"""
```

## owen: recursive

```python
	class Solution(object):
	    def reverseStr(self, s, k):
	        if s=="" ：return “” 
	        return s[0:k][::-1] + s[k:2*k] + self.reverseStr(s[2*k:], k) 
```

