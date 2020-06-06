---
layout: post
title: "[797] All Paths From Source to Target"
published: true
created:  2020 Jun 05 07:23:48 PM
tags: [python, leetcode, medium, queue, bfs, dfs]
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
        queue, ans = [[0]], []
        while len(queue):
            top = queue.pop(0)
            if top[-1] == len(graph):
                ans.append(top)
                continue
            for nei in graph[top[-1]]:
                queue.append(top + [nei])
        return ans
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
        end, cur, res = len(graph) - 1, [[0]], []
        while cur:
            path = cur.pop()
            for p in graph[path[-1]]:
                if p == end:
                    res.append(path + [p])
                else:
                    cur.append(path + [p])
        return res
```

### dfs

```python
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def helper(end, cur):
            if cur == end:
                return [[cur]]
            res = []
            for p in graph[cur]:
                res += [[cur] + l for l in helper(end, p)]
            return res
        return helper(len(graph) - 1, 0)
```

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

* https://www.youtube.com/watch?v=L38V_q3lrvM
