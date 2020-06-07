#
# @lc app=leetcode id=797 lang=python3
#
# [797] All Paths From Source to Target
#

# @lc code=start

class Solution:     #lmv(bfs) debugging

    """
    Python Short BFS

    https://leetcode.com/problems/all-paths-from-source-to-target/discuss/416451

    * Lang:    python3
    * Author:  ElectricAvenue
    * Votes:   2

    Abuse the fact that the graph has no cycles. We can just do the naive BFS
    here to enumerate all the answers.
    """

    """
                0     1    2    3
    || Input: [[1,2], [3], [3], []]
    || Output: [[0,1,3],[0,2,3]]
    || Explanation: The graph looks like this:
    || 0--->1
    || |    |
    || v    v
    || 2--->3
    || There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
    """

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        queue, ans = [[0]], []
        print("init q is %s, ans is %s" % (queue, ans))
        while len(queue):
            top = queue.pop(0)
            print("top is %s, queue is %s" % (top, queue))
            if top[-1] == len(graph) - 1:
                ans.append(top)
                print("reach the end, append top %s into ans %s" % (top, ans))
                continue
            for nei in graph[top[-1]]:
                print("from graph[top[-1]] that is graph[%s]=%s, get nei %s" % (top[-1], graph[top[-1]], nei))
                print("use this nei to extend top, and append new top into queue")
                queue.append(top + [nei])
                print("queue is now", queue)
        return ans

class Solution:     #lmv(bfs)

    """
    Python Short BFS

    https://leetcode.com/problems/all-paths-from-source-to-target/discuss/416451

    * Lang:    python3
    * Author:  ElectricAvenue
    * Votes:   2

    Abuse the fact that the graph has no cycles. We can just do the naive BFS
    here to enumerate all the answers.
    """

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        pathq, res = [[0]], []        #queue to save all paths, init with node 0
        while len(pathq):
            firstpath = pathq.pop(0)  #dequeue first path
            if firstpath[-1] == len(graph) - 1: #check if last node reaches end
                res.append(firstpath) #if yes, save this full path to result
                continue              #and check next path
            for nei in graph[firstpath[-1]]:    #otherwise, get all it's neighbors
                pathq.append(firstpath + [nei]) #connect it's nei into the path
        return res                    #and append back into paths queue


class Solution:     #jj: dfs
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def helper(endnode, node):
            if node == endnode:
                return [[node]]
            res = []
            for nei in graph[node]:
                res += [[node] + l for l in helper(endnode, nei)]
            return res
        return helper(len(graph) - 1, 0)

class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(graph, 0, len(graph) - 1, res, [0])
        return res

    def dfs(self, graph, start, end, res, path):
        if start == end:
            res.append(path)
        for node in graph[start]:
            self.dfs(graph, node, end, res, path + [node])

# @lc code=end
