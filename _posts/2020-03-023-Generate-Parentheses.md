---
layout: post
title: "[22] Generate Parentheses"
published: true
created:  2020 Mar 23 03:32:50 PM
tags: [python, leetcode, DFS,DP, medium]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[22] Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)

    ||Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
    ||                                                                                                       
    ||For example, given n = 3, a solution set is:                                                           
    ||                                                                                                       
    ||[                                                                                                      
    ||  "((()))",                                                                                            
    ||  "(()())",                                                                                            
    ||  "(())()",                                                                                            
    ||  "()(())",                                                                                            
    ||  "()()()"                                                                                             
      ]                                                                                                      


## owen fake DP
extend the scale of matrix to +2 and +2

```python
class Solution(object):
    def generateParenthesis(self, n):
        if n==0:return []
        if n==1:return ["()"]
        if n==2:return ["()()","(())"]
        temp=["()()","(())"]
        temp1=set()
        for i in range(3,n+1):
            for j in temp:
                temp1.add("()"+j)
                temp1.add(j+"()")
                temp1.add("("+j+")")
                m=self.helper(j)
                for x in range(1,len(m)-1):
                    for y in range(x+1,len(m)):
                        if m[y][1]-m[x][1]==m[y][0]-m[x][0]+1:
                            temp1.add(j[0:x]+"("+j[x:y+1]+")"+j[y+1:]) 
            temp=list(temp1)
            temp1=set()
        return temp   
    def helper(self,str1):
        l=[]
        count0,count1=0,0
        for i in str1:
            if i=="(":count0+=1
            if i==")":count1+=1
            l.append((count0,count1))
        return l
```


