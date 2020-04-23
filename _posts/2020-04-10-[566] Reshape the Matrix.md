---
layout: post
title: "[566]  Reshape the Matrix"
published: true
created:  2020 Apr 19 12:16:56 PM
tags: [python, leetcode, easy,2D matrix]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[566] Reshape the Matrix](https://leetcode.com/problems/reshape-the-matrix/)

    ||In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.                                    
                                                                                                                                                                                          
    ||cYou're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.
                                                                                                                                                                                                
      The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.                                                         
                                                                                                                                                                                              
      If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.                                            

## Owen

```python
class Solution(object):
    def matrixReshape(self, nums, r, c):
        r1,c1=len(nums),len(nums[0])
        if r1*c1!=r*c :return nums
        l=[[0  for i in range(c)]for j in range(r)]
        for i in range(r*c):
            l[i/c][i%c]=nums[i/c1][i%c1]     
        return l
```

## owen: numpy from LMV

```python
import numpy as np

class Solution(object):
    def matrixReshape(self, nums, r, c):
        try:
            return np.reshape(nums, (r, c)).tolist()
        except:
            return nums
```

