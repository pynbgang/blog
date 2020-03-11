#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#

# @lc code=start
class Solution:     #ping
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        return (sum(sum(l) for l in grid) * 4   #sum(all 1 x 4)
            -                 #minus sum(borders of 1) x 2
            sum([1 for l in grid for i in range(1, len(l)) if l[i] == l[i-1] == 1]) * 2
            -                 #minus sum(borders of 1 after matrix flip) x 2
            sum([1 for l in zip(*grid) for i in range(1, len(l)) if l[i] == l[i-1] == 1]) * 2
            )
        """
        ||   ✔ Accepted
        ||   ✔ 5833/5833 cases passed (500 ms)
        ||   ✔ Your runtime beats 90.89 % of python3 submissions
        ||   ✔ Your memory usage beats 100 % of python3 submissions (12.9 MB)
        """

class Solution:     #lmv
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                    if grid[row][column]:
                        res+=4
                        if row and grid[row-1][column]:
                            res-=2
                        if column and grid[row][column-1]:
                            res-=2
        return res
        """
        ||   ✔ Accepted
        ||   ✔ 5833/5833 cases passed (468 ms)
        ||   ✔ Your runtime beats 99.75 % of python3 submissions
        ||   ✔ Your memory usage beats 100 % of python3 submissions (12.8 MB)
        """

def islandPerimeter(self, grid):    #lmv
    return sum(sum(map(operator.ne, [0] + row, row + [0]))
               for row in grid + map(list, zip(*grid)))

    """
    ||   ✔ Accepted
    ||   ✔ 5833/5833 cases passed (500 ms)
    ||   ✔ Your runtime beats 90.6 % of python3 submissions
    ||   ✔ Your memory usage beats 100 % of python3 submissions (12.9 MB)
    """

# @lc code=end
