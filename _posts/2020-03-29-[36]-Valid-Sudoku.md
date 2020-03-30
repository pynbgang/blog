---
layout: post
title: "[36] Valid Sudoku"
published: true
created:  2020 Mar 29 03:32:50 PM
tags: [python, leetcode, list, medium,]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[36] Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)

    ||Each row must contain the digits 1-9 without repetition.   
    ||Each column must contain the digits 1-9 without repetition.
    ||Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

   
## Brute Force Owen

```python

class Solution(object):
    def isValidSudoku(self, board):
        row,col=9,9
        for i in board:
            temp="".join(i).replace(".","")
            if len(temp)!=len(set(temp)):return False
        for j in range(len(board[0])):
            temp=""
            for i in range(len(board)):
                if board[i][j]!=".":temp+=board[i][j]
            if  len(temp)!=len(set(temp)):return False
        for z in range(3):
            temp,temp1,temp2="","",""
            for i in range(z*3,z*3+3):
                for j in range(0,3):
                    if board[i][j]!=".":temp+=board[i][j]
                    if board[i][j+3]!=".":temp1+=board[i][j+3]
                    if board[i][j+6]!=".":temp2+=board[i][j+6]
            if  len(temp)!=len(set(temp)):return False
            if  len(temp1)!=len(set(temp1)):return False
            if  len(temp2)!=len(set(temp2)):return False
        return True
        
```

