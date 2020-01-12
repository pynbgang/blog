---
layout: post
title: "max-area-of-island"
subtitle: ""
date: 2020-01-07
author: "xiaofo"
tags: 
    - dfs
    - array
    - leetcode
    - medium
    - python
    - xiaofo
created:  2020 Jan 07 10:46:15 PM
categories: [tech]
published: true

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [max-area-of-island](https://leetcode.com/problems/max-area-of-island/)

## solution (after peeping most voted solution) 

```python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(g, r, c):
            if 0 <= r < len(g) and 0 <= c < len(g[0]) and g[r][c]:
                g[r][c] = 0
                return 1 + dfs(g, r + 1, c) + dfs(g, r - 1, c) + dfs(g, r, c + 1) + dfs(g, r, c - 1)
            return 0 
        rtn = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                rtn = max(rtn, dfs(grid, i, j))
        return rtn
```
## takeaway 

- use dfs to explore an 'island'
- set each element to 0 while exploring to avoid repeated traversal, after dfs, the island should have disappeared from the map
