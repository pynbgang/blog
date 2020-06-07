---
layout: post
title: "[797] All Paths From Source to Target"
published: true
created:  2020 Jun 05 07:23:48 PM
tags: [python, leetcode, medium, queue, bfs, dfs, debug, recursion]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[797] All Paths From Source to Target](https://leetcode.com/problems/all-paths-from-source-to-target/description/)

    || * algorithms
    || * Medium (73.07%)
    || * Likes:    685
    || * Dislikes: 58
    || * Total Accepted:    52.6K
    || * Total Submissions: 70.7K
    || * Testcase Example:  '[[1,2],[3],[3],[]]'
    || * Source Code:       797.all-paths-from-source-to-target.py
    || 
    || Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.
    || 
    || The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.
    || 
    || 
    || Example:
    || Input: [[1,2], [3], [3], []] 
    || Output: [[0,1,3],[0,2,3]] 
    || Explanation: The graph looks like this:
    || 0--->1
    || |    |
    || v    v
    || 2--->3
    || There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
    || 
    || 
    || Note:
    || 
    || 
    || 	The number of nodes in the graph will be in the range [2, 15].
    || 	You can print different paths in any order, but you should keep the order of nodes inside one path.

## lmv

```python
class Solution:     #lmv

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
```

## lmv debugging
```python
class Solution:     #lmv debugging

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
            if top[-1] == len(graph):
                ans.append(top)
                print("reach the end, append top %s into ans %s" % (top, ans))
                continue
            for nei in graph[top[-1]]:
                print("from graph[top[-1]] that is graph[%s]=%s, get nei %s" % (top[-1], graph[top[-1]], nei))
                print("use this nei to extend top, and append new top into queue")
                queue.append(top + [nei])
                print("queue is now", queue)
        return ans
```

running flows:

    [ins] In [77]: graph                                                                 
    Out[77]: [[1, 2], [3], [3], []]

    top is [0], queue is []
    from graph[top[-1]] that is graph[0]=[1, 2], get nei 1
    use this nei to extend top, and append new top into queue
    queue is now [[0, 1]]
    from graph[top[-1]] that is graph[0]=[1, 2], get nei 2
    use this nei to extend top, and append new top into queue
    queue is now [[0, 1], [0, 2]]
    top is [0, 1], queue is [[0, 2]]
    from graph[top[-1]] that is graph[1]=[3], get nei 3
    use this nei to extend top, and append new top into queue
    queue is now [[0, 2], [0, 1, 3]]
    top is [0, 2], queue is [[0, 1, 3]]
    from graph[top[-1]] that is graph[2]=[3], get nei 3
    use this nei to extend top, and append new top into queue
    queue is now [[0, 1, 3], [0, 2, 3]]
    top is [0, 1, 3], queue is [[0, 2, 3]]
    reach the end, append top [0, 1, 3] into ans [[0, 1, 3]]
    top is [0, 2, 3], queue is []
    reach the end, append top [0, 2, 3] into ans [[0, 1, 3], [0, 2, 3]]


## lmv illustration

    queue:                              use a queue, to hold all path 
    queue: [[0]]                        init the queue with ONE path that has only node 0 in it
             -                              dequeue (from top) FIRST path, check it's LAST node, 
             graph[0] > [1,2]               get it's neighbors (given in graph)

    queue: [[0,1], [0,2]]                   attach each neighbor into this (FIRST) path, and enqueue (at tail => append)
               -                        repeat this process
               graph[1] > [3]               ......

    queue: [[0,2],[0,1,3]]                  ......
               -                            ......
               graph[2] > [3]               ......

    queue: [[0,1,3],[0,2,3]]                ......
                 -                      whenever a path reaches the end node, 

    ans: [[0,1,3]]                          copy this path into result

    queue: [[0,2,3]]                        repeat this for all paths
                 -
    ans: [[0,1,3], [0,2,3]]                 get final result

## jj

### bfs

```python
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        endnode, pathq, res = len(graph) - 1, [[0]], []
        while pathq:                            #repeat below until pathq is empty
            path = pathq.pop()                  #keep dequeuing first path
            for node in graph[path[-1]]:        #check all it's neighbors
                if node == endnode:             #if a nei is end node
                    res.append(path + [node])   #this is a full path, save in result
                else:                           #otherwise, not a full path yet
                    pathq.append(path + [node]) #connect path with this new node, and enqueue
        return res
```

### dfs

```python
class Solution:     #jj: dfs
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def helper(endnode, node):
            if node == endnode:         #if reaches end
                return [[node]]         #just return end node as current path
            res = []                    #if not reaches end, check each neighbors
            for nei in graph[node]:     #conn curr node and each nei to update path
                res += [[node] + l for l in helper(endnode, nei)] #and save in res
            return res
        return helper(len(graph) - 1, 0)
```

### dfs debug

```python
from typing import List
class Solution:     #jj: dfs
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.spaces=0
        def helper(endnode, node):
            print(">>>>entering helper") 
            print(' '*self.spaces, "get a node: ", node)
            if node == endnode:
                print(' '*self.spaces, "<<<<reaches end, return this node", [[node]])
                return [[node]]
            res = []
            print(' '*self.spaces, "not reaches end yet, it's neighbors: ", graph[node])
            for nei in graph[node]:
                print("get one neighbor ", nei)
                self.spaces += 4
                path = [[node] + l for l in helper(endnode, nei)]
                res += path
                print("path is to connect current node %s and each neighbors %s: %s" % (node, nei, path))
                print("add it into res: ", res)
                self.spaces -= 4
            print(' '*self.spaces, "<<<<return result", res)
            return res
        return helper(len(graph) - 1, 0)

S=Solution()
graph=[[1,2], [3], [3], []]
S.allPathsSourceTarget(graph)
```

    >>>>entering helper
        get a node:  0
        not reaches end yet, get it's neighbors:  [1, 2]

        get one neighbor  1
        >>>>entering helper
            get a node:  1
            not reaches end yet, get neighbors of this node:  [3]
            get one neighbor  3
            >>>>entering helper
                get a node:  3
            <<<<reaches end, return this node [[3]]
            path is to connect current node 1 and each neighbors 3: [[1, 3]]
            add it into res:  [[1, 3]]
        <<<<return result [[1, 3]]

        path is to connect current node 0 and each neighbors 1: [[0, 1, 3]]
        add it into res:  [[0, 1, 3]]

        get one neighbor  2
        >>>>entering helper
            get a node:  2
            not reaches end yet, it's neighbors:  [3]
            get one neighbor  3
            >>>>entering helper
                get a node:  3
            <<<<reaches end, return this node [[3]]
            path is to connect current node 2 and each neighbors 3: [[2, 3]]
            add it into res:  [[2, 3]]
        <<<<return result [[2, 3]]

        path is to connect current node 0 and each neighbors 2: [[0, 2, 3]]
        add it into res:  [[0, 1, 3], [0, 2, 3]]

    <<<<return result [[0, 1, 3], [0, 2, 3]]


## others

```python
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
```

## good resources

* https://www.youtube.com/watch?v=L38V_q3lrvM good explain of the problem
