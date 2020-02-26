---
layout: post
title: "Best Sightseeing Pair"
published: true
created:  2020 Feb 26 02:45:47 PM
tags: [python, list, leetcode, mdedium]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [Best Sightseeing Pair](https://leetcode.com/problems/best-sightseeing-pair/)

||Given an array A of positive integers, A[i] represents the value of the i-th sightseeing spot, and two sightseeing spots i and j have distance j - i between them.
||                                                                                                                                                                  
||The score of a pair (i < j) of sightseeing spots is (A[i] + A[j] + i - j) : the sum of the values of the sightseeing spots, minus the distance between them.      
||                                                                                                                                                                  
||Return the maximum score of a pair of sightseeing spots.                                                                                                          
||                                                                                                                                                                  
||                                                                                                                                                                  
||                                                                                                                                                                  
||Example 1:                                                                                                                                                        
||                                                                                                                                                                  
||Input: [8,1,5,2,6]                                                                                                                                                
||Output: 11                                                                                                                                                        
||                                                                                                                                                                                                                                                                                                                                                                                                                                          

## Owen - find the max from end 

```python
class Solution(object):
    def maxScoreSightseeingPair(self, A):
        len1,l2,temp=len(A),[0]*(len(A)-1)+[A[-1]+1-len(A)],0
        for i in range(len1-2,0,-1):
            l2[i]=max(A[i]-i,l2[i+1])
        for i in range(len1-1):
            temp=max(temp,A[i]+i+l2[i+1])
        return temp
```




