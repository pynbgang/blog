#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:     #ping: brute force, dummy code repeat
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for l in board:
            if "." not in l:
                if len(set(l)) != 9:
                    return False
            else:
                if len(set(l)) != sorted(l, reverse=True).index('.') + 1:
                    return False
        for l in map(list, zip(*board)):
            if "." not in l:
                if len(set(l)) != 9:
                    return False
            else:
                if len(set(l)) != sorted(l, reverse=True).index('.') + 1:
                    return False
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                l = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if "." not in l:
                    if len(set(l)) != 9:
                        return False
                else:
                    if len(set(l)) != sorted(l, reverse=True).index('.') + 1:
                        return False
        return True

class Solution:     #ping: brute force, compacted
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        superb = (                          #compose a superboard
            board +                         #from original board, plus
            list(map(list, zip(*board))) +  #rotated board, and subbox rows
            [[board[x][y] for x in range(i, i+3) for y in range(j, j+3)] for i in (0,3,6) for j in (0,3,6)]
        )
        for l in superb:
            if "." not in l:                #if no '.', set len must be 9
                if len(set(l)) != 9:
                    return False
            else:                           #with '.', # of digits must be..
                if len(set(l)) != sorted(l, reverse=True).index('.') + 1:
                    return False
        return True

# @lc code=end
