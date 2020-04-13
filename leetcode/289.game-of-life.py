#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#

# @lc code=start
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        pass

class Solution(object):     # own
    def gameOfLife(self, board):
        # create a new matrix with 2 additional all-0 rows and columns
        row, col=len(board), len(board[0])
        l1=[[0 for x in range(col+2)] for y in range(row+2)]
        for i in range(row):
            for j in range(col):
                if board[i][j]==1: l1[i+1][j+1]=1

        for i in range(1,row+1):
            for j in range(1,col+1):
                sum1=self.helper(l1,i,j)
                if l1[i][j]:
                    if 2<=sum1<=3:  board[i-1][j-1]=1
                    else:           board[i-1][j-1]=0
                else:
                    if sum1==3:     board[i-1][j-1]=1
        return board

    def helper(self,l1,i,j):
        return l1[i-1][j-1]+l1[i+1][j+1]+l1[i-1][j+1]+l1[i+1][j-1]+l1[i][j-1]+l1[i-1][j]+l1[i][j+1]+l1[i+1][j]

        """
        ||   ✔ Accepted
        ||   ✔ 23/23 cases passed (28 ms)
        ||   ✔ Your runtime beats 85.73 % of python3 submissions
        ||   ✔ Your memory usage beats 10 % of python3 submissions (13.8 MB)
        """

class Solution(object):     # ping: optimized based on own
    def gameOfLife(self, board):
        # create a new extended grid with 2 additional all-0 rows and columns
        row, col=len(board), len(board[0])
        l1=[[0 for x in range(col+2)] for y in range(row+2)]

        # copy the orig grid into the new extended grid
        for i in range(row):
            for j in range(col):
                if board[i][j]:
                    l1[i+1][j+1]=1

        # from the new grid, calc new value based on game rules,
        # and update the old grid
        for i in range(1,row+1):
            for j in range(1,col+1):
                sum1 = (l1[i-1][j-1] + l1[i+1][j+1] +
                        l1[i-1][j+1] + l1[i+1][j-1] +
                        l1[i][j-1]   + l1[i-1][j]   +
                        l1[i][j+1]   + l1[i+1][j]
                        )
                if l1[i][j] and not 2<=sum1<=3 :
                    board[i-1][j-1]=0
                if not l1[i][j] and sum1==3:
                    board[i-1][j-1]=1
        return board

        """
        ||   ✔ Accepted
        ||   ✔ 23/23 cases passed (28 ms)
        ||   ✔ Your runtime beats 85.73 % of python3 submissions
        ||   ✔ Your memory usage beats 10 % of python3 submissions (13.8 MB)
        """

class Solution(object):     # ping: owen compact more
    def gameOfLife(self, board):
        # create a new extended grid with 2 additional all-0 rows and columns
        row, col=len(board), len(board[0])
        l1=[[1 if x and y and x<=col and y<=row and board[y-1][x-1] else 0 \
             for x in range(col+2)] \
             for y in range(row+2)]

        # from the new grid, calc new value based on game rules,
        # and update the old grid
        for i in range(1,row+1):
            for j in range(1,col+1):
                sum1 = (l1[i-1][j-1] + l1[i+1][j+1] +
                        l1[i-1][j+1] + l1[i+1][j-1] +
                        l1[i][j-1]   + l1[i-1][j]   +
                        l1[i][j+1]   + l1[i+1][j]
                        )
                if l1[i][j] and not 2<=sum1<=3 :
                    board[i-1][j-1]=0
                if not l1[i][j] and sum1==3:
                    board[i-1][j-1]=1
        return board

class Solution(object):     # lmv
     def gameOfLifeInfinite(self, live):
         ctr = collections.Counter((I, J)
                                   for i, j in live
                                   for I in range(i-1, i+2)
                                   for J in range(j-1, j+2)
                                   if I != i or J != j)
         return {ij for ij in ctr
                 if ctr[ij] == 3 or ctr[ij] == 2 and ij in live}
     def gameOfLife(self, board):
         live = {(i, j) for i, row in enumerate(board) for j, live in enumerate(row) if live}
         live = self.gameOfLifeInfinite(live)
         for i, row in enumerate(board):
             for j in range(len(row)):
                 row[j] = int((i, j) in live)

class Solution(object):     # ping: use dict + complex
    def gameOfLife(self, grid):
        # use a dict to record board info
        d = {i + j*1j: val for i, row in enumerate(grid) for j, val in enumerate(row)}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                sum1 = (sum(d.get(i+j*1j+1j**k, 0) for k in range(4)) +
                        d.get(i+1+j*1j+1j, 0) + d.get(i-1+j*1j-1j, 0) +
                        d.get(i+1+j*1j-1j, 0) + d.get(i-1+j*1j+1j, 0))
                if d.get(i+j*1j,0) and not 2<=sum1<=3 :
                    grid[i][j]=0
                if not d.get(i+j*1j,0) and sum1==3:
                    grid[i][j]=1
        return grid

class Solution(object):     # ping: compact the above
    def gameOfLife(self, grid):
        # use a dict to record board info
        d = {i + j*1j: val for i, row in enumerate(grid) for j, val in enumerate(row)}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                sum1 = (sum(d.get(i+j*1j+1j**k, 0) for k in range(4)) +
                        d.get(i+1+j*1j+1j, 0) + d.get(i-1+j*1j-1j, 0) +
                        d.get(i+1+j*1j-1j, 0) + d.get(i-1+j*1j+1j, 0))
                if (d.get(i+j*1j,0) and not 2<=sum1<=3) or (not d.get(i+j*1j,0) and sum1==3): grid[i][j] = int(not(grid[i][j]))
        return grid

# @lc code=end
