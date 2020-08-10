#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:     #ping
    def exist(self, grid: List[List[str]], word: str) -> bool:

        if not grid: return False           #特判：空矩阵
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):               #全矩阵扫描，要找的是：
            for j in range(cols):           #"从给定某一点开始，能够向四周扩展
                if self.dfs(grid,i,j,word): #成功匹配”的情形
                    return True             #那么就返回成功， 不再继续寻找了
        return False                        #如果搜完矩阵没有这种情形，返回失败

    def dfs(self,grid,i,j,word):            #因此递归函数的设计，也是要：
        print("dfs: get %s, %s" % (i, j))
        if grid[i][j] == word[0]:           #从给定一点开始，如向周围扩展能匹配
            grid[i][j] = 0                  #则返回true，其他返回false
        else:                               #先看首字母，如匹配就置0，这样后面
            return False                    #向周围查找时候这个点不再能重复匹配
        if len(word) == 1:                  #如首字母不匹配则失败。如果已经匹配
            return True                     #并到最后字母，则成功
        for m,n in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]: #四邻查找
            if m>=0 and m<len(grid) and n>=0 and n<len(grid[0]) and grid[m][n]==word[1]:
                if self.dfs(grid,m,n,word[1:]):     #检查边界，如果找到，则不断
                    return True             #递归看是否成功
        grid[i][j] = word[0]                #若四邻搜完都不见，则恢复置位的字母
        return False                        #否则会影响caller从其他位置开始的查找

class Solution:     #jj, no need setting matching char
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board                      #global var in recursion
        self.word = word    #debugging
        return any(self.helper(i, j, [], word)    #scan grid, if starting from
                   for i in range(len(board))     #any position match can succeed
                   for j in range(len(board[0]))) #then return True

    def helper(self, i, j, path, word):
        # if word == self.word: print(i, j)     #debugging code
        if not word:        #if word is empty then match succeed
            return True     #if first ch matchs at a new pos, check 4 neighbors
        if self.board[i][j] == word[0] and (i, j) not in path:
            for r, c in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if (not word[1:] or                     #if reach end of word, or
                   (r in range(len(self.board)) and     #within proper position
                    c in range(len(self.board[0])) and  #all rest chs of word
                    self.helper(r, c, path + [(i, j)], word[1:]) #can be found
                   )):      #also adding searched pos in searched-list
                    return True                         #then return true
        return False #otherwise (if no searches ever return True), return False

#Testcase:
[["A","B","C","E"],
 ["S","F","C","S"],
 ["A","D","E","E"]]
"ABCCED"

[["A","B","C","E"],
 ["S","F","C","S"],
 ["A","D","E","E"]]
"ABCB"

grid=[["C","A","A"], ["A","A","A"], ["B","C","D"]]
word="AAB"

S=Solution()
S.exist(grid, word)
# @lc code=end
