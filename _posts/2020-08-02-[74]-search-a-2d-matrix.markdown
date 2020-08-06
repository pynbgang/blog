---
layout: post
title: "[74] Search a 2D Matrix"
published: true
created:  2020 Aug 02 11:30:49 PM
tags: [python, leetcode, medium]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[74]-Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)

    || https://leetcode.com/problems/search-a-2d-matrix/
    || 
    || Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
    ||                                                                                                                     
    || Integers in each row are sorted from left to right.                                                                 
    || The first integer of each row is greater than the last integer of the previous row.                                 
    || Example 1:                                                                                                          
    ||                                                                                                                     
    || Input:                                                                                                              
    || matrix = [                                                                                                          
    ||   [1,   3,  5,  7],                                                                                                 
    ||   [10, 11, 16, 20],                                                                                                 
    ||   [23, 30, 34, 50]                                                                                                  
    || ]                                                                                                                   
    || target = 3                                                                                                          
    || Output: true                                                                                                        
    || Example 2:                                                                                                          
    ||                                                                                                                     
    || Input:                                                                                                              
    || matrix = [                                                                                                          
    ||   [1,   3,  5,  7],                                                                                                 
    ||   [10, 11, 16, 20],                                                                                                 
    ||   [23, 30, 34, 50]                                                                                                  
    || ]                                                                                                                   
    || target = 13                                                                                                         
    || Output: false                                                                                                       
    || ]
    || 
    || Example 2:
    || 
    || Input: 
    || [
    || ? [0,1,2,0],
    || ? [3,4,5,2],
    || ? [1,3,1,5]
    || ]
    || Output: 
    || [
    || ? [0,0,0,0],
    || ? [0,4,5,0],
    || ? [0,3,1,0]
    || ]
    || 
    || 
    || Follow up:
    || 
    || 	A straight forward solution using O(mn) space is probably a bad idea.
    || 	A simple improvement uses O(m + n) space, but still not the best solution.
    || 	Could you devise a constant space solution?



# Owen 
## binary search 
```python
class Solution(object):
    def searchMatrix(self, matrix, target):
            if not matrix or target is None:
                return False

            rows, cols = len(matrix), len(matrix[0])
            low, high = 0, rows * cols - 1

            while low <= high:
                mid = (low + high) / 2
                num = matrix[mid / cols][mid % cols]

                if num == target:
                    return True
                elif num < target:
                    low = mid + 1
                else:
                    high = mid - 1

            return False
```

## reduce 
```python
class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix :return False
        l=reduce(lambda a,b:a+b,matrix)
        return target in l
```



