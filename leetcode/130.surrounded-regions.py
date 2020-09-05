#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start

from typing import List
class Solution:
    def solve(self, board):
        if not any(board): return
        m, n = len(board), len(board[0])
        save = [ij for k in range(max(m,n)) for ij in ((0, k), (m-1, k), (k, 0), (k, n-1))]
        while save:
            i, j = save.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'S'
                save += (i, j-1), (i, j+1), (i-1, j), (i+1, j)
        print("board before last line: ", board)
        #board[:] = [['XO'[c == 'S'] for c in row] for row in board]
        #print("board after last line(slice): ", board)
        board = [['XO'[c == 'S'] for c in row] for row in board]
        print("board after last line(no slice): ", board)

class Solution:     #ping
    def solve(self, grid: List[List[str]]) -> None:
        if not grid: return
        self.rows, self.cols = len(grid), len(grid[0])

        for i in range(self.rows):           #full grid searching for O
            for j in range(self.cols):
                if grid[i][j] == 'O':   #if found in border, set N(onmutable)
                    if i in [0, self.rows-1] or j in [0, self.cols-1]:
                        grid[i][j] = 'N'
                    else:               #if found in non-border, dfs
                        self.dfs(grid,i,j,[])

        grid[:] = ['XO'[c == 'N'] for c in  for row in grid]

    def dfs(self,grid,i,j,rec):
        flipback, grid[i][j] = 0, 'X' #for O at non-border, assume OK to flip to X.
        rec.append((i,j))   #just in case (connect to border O), save its index

        for m,n in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:   # check 4 neighbors
            if (m in [0, self.rows-1] or n in [0, self.cols-1]) and grid[m][n] in ['O', 'N']:
                grid[i][j], flipback = 'N', 1
                break

            if m>0 and m<self.rows-1 and n>0 and n<self.cols-1:
                if grid[m][n] == 'O':       #if found O in non-border, dfs
                    self.dfs(grid,m,n,rec)
                if grid[m][n] == 'N':
                    grid[i][j], flipback = 'N', 1
                    break

        if flipback:
            for i,j in rec:
                grid[i][j] = 'N'

        """
                for i in range(self.rows):
                    for j in range(self.cols):
                        if grid[i][j] != 'N':
                            grid[i][j] = 'X'
                        if grid[i][j] == 'N':
                            grid[i][j] = 'O'
        grid=[["O","O","O"],
            ["O","O","O"],
            ["O","O","O"]]

        grid=[["O","O","O","O","X","X"],
            ["O","O","O","O","O","O"],
            ["O","X","O","X","O","O"],
            ["O","X","O","O","X","O"],
            ["O","X","O","X","O","O"],
            ["O","X","O","O","O","O"]]
        grid=[["X","X","X","X"],
            ["X","O","O","X"],
            ["X","X","O","X"],
            ["X","O","X","X"]]

        S=Solution()
        S.solve(grid)

        [["X","X","X","X"],
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","O","X","X"]]

        [["O","O","O","O","X","X"],
        ["O","O","O","O","O","O"],
        ["O","X","O","X","O","O"],
        ["O","X","O","O","X","O"],
        ["O","X","O","X","O","O"],
        ["O","X","O","O","O","O"]]

        ✘ Testcase:        [["O","O","O","O","X","X"],["O","O","O","O","O","O"],["O","X","O","X","O","O"],["O","X","O","O","X","O"],["O","X","O","X","O","O"],["O","X","O","O","O","O"]]
        ✘ Answer:          [["O","O","O","O","X","X"],["O","O","O","O","O","O"],["O","X","O","X","O","O"],["O","X","O","X","X","O"],["O","X","O","X","O","O"],["O","X","O","O","O","O"]]
        ✘ Expected Answer: [["O","O","O","O","X","X"],["O","O","O","O","O","O"],["O","X","O","X","O","O"],["O","X","O","O","X","O"],["O","X","O","X","O","O"],["O","X","O","O","O","O"]]

        [["X","X","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["X","O","X","X"]]
        [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
        [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]



        """
# @lc code=end
