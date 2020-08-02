#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, G: List[List[int]]) -> int:
        M, N, m = len(G), len(G[0]), 0
        def area(x,y):
            p, t, a, G[x][y] = [[x,y]], [], 1, 0
            while p:
                for i,j in p:
                    for k,l in [[i-1,j],[i,j+1],[i+1,j],[i,j-1]]:
                        if k in [-1,M] or l in [-1,N] or G[k][l] == 0: continue
                        a, G[k][l], _ = a + 1, 0, t.append([k,l])
                p, t = t, []
            return a
        for i,j in itertools.product(range(M),range(N)):
            if G[i][j]: m = max(m,area(i,j))
        return m

class Solution:
    def maxAreaOfIsland(self, G: List[List[int]]) -> int:
        M, N, m = len(G), len(G[0]), 0
        def dfs_area(x,y):
            if (x,y) in V: return
            G[x][y], _ = 0, V.add((x,y))
            for i,j in [[x-1,y],[x,y+1],[x+1,y],[x,y-1]]:
                if not (i in [-1,M] or j in [-1,N] or G[i][j] == 0): dfs_area(i,j)
        for i,j in itertools.product(range(M),range(N)):
            if G[i][j]: V = set(); dfs_area(i,j); m = max(m,len(V))
        return m

class Solution(object):

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        ## 空输入就啥别说了
        if not grid: return

        ## 整个排列坐标系
        rows, cols, max_ones = len(grid), len(grid[0]), 0

        ## 全坐标暴力搜索1，找到后对它求个值（它所在连续1区间的数量）
        ## 具体求法另议
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    max_ones = max(max_ones,self.dfs(grid,i,j,1))

        return max_ones

    def dfs(self,grid,i,j,count):
        ## 针对某一个1，求”岛面积“，即所在周边所有连续1的数量。dfs递归思路

        ## 已知为1，置零
        grid[i][j] = 0

        ## 一一查看当前点的“周边”四个点
        for m,n in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
            ## 如果这四个边界点在有效范围内并且也为1， 则
            if m>=0 and m<len(grid) and n>=0 and n<len(grid[0]) and grid[m][n]:
                ## 对这边界为1的点再次dfs递归，并扩展总数量
                count = 1 + self.dfs(grid,m,n,count)
        ## 最后返回总的连续1的数量
        return count

# @lc code=end
