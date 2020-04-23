---
layout: post
title: "[29] Combination Sum"
published: true
created:  2020 Apr 13 12:16:56 PM
tags: [python, leetcode, medium,dfs]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[39] Combination Sum](https://leetcode.com/problems/combination-sum/)

    ||Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), 
    ||find all unique combinations in candidates where the candidate numbers sums to target.
    ||                                                                                                                                                                                       
    ||The same repeated number may be chosen from candidates unlimited number of times.                                                                                                      
    ||                                                                                                                                                                                       
    ||Note:                                                                                                                                                                                  
    ||                                                                                                                                                                                       
    ||All numbers (including target) will be positive integers.                                                                                                                              
    ||The solution set must not contain duplicate combinations.                                                                                                                              
    ||Example 1:                                                                                                                                                                             
    ||                                                                                                                                                                                       
    ||Input: candidates = [2,3,6,7], target = 7,                                                                                                                                             
    ||A solution set is:                                                                                                                                                                     
    ||[                                                                                                                                                                                      
    ||  [7],                                                                                                                                                                                 
    ||  [2,2,3]                                                                                                                                                                              
      ]                                                                                                                                                                                      
      Example 2:   
                                                                                                                                                                                
## Owen  DFS,but need to think a way to remove the bold line                                                                                                                                                                                     

```python
class Solution(object):
    def combinationSum(self, candidates, target):
        self.l = []
        candidates.sort()
        self.helper(candidates, target, [])
        return self.l

    def helper(self, candidates, target, list1):
        if target<0:return
        if target==0:
            list1.sort()
            if list1 not in self.l:self.l.append(list1)
            …………………………………………………………………………………………………………
            return 
        for i in range(len(candidates)):
            self.helper(candidates,target-candidates[i],list1+[candidates[i]])
```

