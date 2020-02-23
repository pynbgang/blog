---
layout: post
title: "nested list weight sum"
published: true
created:  2020 Feb 22 02:21:06 PM
tags: [python, lintcode, leetcode, easy, list, recursive, queue]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [leetcode show 339](https://leetcode.com/problems/nested-list-weight-sum/description/)

see also [lintcode](https://www.lintcode.com/problem/nested-list-weight-sum/description)

|| * algorithms
|| * Easy (71.38%)
|| * Likes:    437
|| * Dislikes: 96
|| * Total Accepted:    76.2K
|| * Total Submissions: 106.5K
|| * Testcase Example:  '[[1,1],2,[1,1]]'
||
|| Given a nested list of integers, return the sum of all integers in the list weighted by their depth.
||
|| Each element is either an integer, or a list -- whose elements may also be integers or other lists.
||
||
|| Example 1:
||
||
|| Input: [[1,1],2,[1,1]]
|| Output: 10
|| Explanation: Four 1's at depth 2, one 2 at depth 1.
||
||
|| Example 2:
||
||
|| Input: [1,[4,[6]]]
|| Output: 27
|| Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27.

## tips

* the input is NOT an ordinary nestedlist of integers, like [1,[4,[6]]].
  instead, each raw element is a class, which, via it's method, returns the
  integer or list

```python
def depthSum(self, nestedList: List[NestedInteger]) -> int:
    for i in nestedList:
        if i.isInteger():
            print("print i: ", i)

 Stdout: print i:  NestedInteger{_integer: 2, _list: []}
```
* the methods to return integer or list, and how to identify the two, are given
  - getInteger()
  - getList()
  - isInteger()


## owen: DFS/recursive (most readable)

```python
 class Solution(object):
    # @param {NestedInteger[]} nestedList a list of NestedInteger Object
    # @return {int} an integer
    def depthSum(self, nestedList):
        self.sum = 0

        def dfs(nestedList, depth):
            for i in nestedList:
                if i.isInteger():
                    self.sum += i.getInteger()*depth
                else:
                    dfs(i.getList(),depth+1)

        dfs(nestedList,1)
        return self.sum
```

tips:

* use recursion
* use member var - essentially a global var, to accumulate the result in the
  recursion. non-member var won't work.


## lmv: exactly the same

```python
def DFS(nestedList, depth):
    temp_sum = 0
    for member in nestedList:
        if member.isInteger():
            temp_sum += member.getInteger() * depth
        else:
            temp_sum += DFS(member.getList(),depth+1)
    return temp_sum
return DFS(nestedList,1)
```

## xiaofo: recursive: (shortest)

```python
class Solution(object):
    # @param {NestedInteger[]} nestedList a list of NestedInteger Object
    # @return {int} an integer
    def depthSum(self, nestedList):
        # result is sum of all weighted elements, 
        # how to calc each weighted element, leave to helper
        return sum(self.helper(1, i) for i in nestedList)

    def helper(self, depth, i):
        return (
            i.getInteger() * depth #weighed value for integer
            if i.isInteger() else  #weighed value for list, is sum of all 
            sum(self.helper(depth + 1, n) for n in i.getList()) #weighted items
        )
```

## xiaofo: queue (w/o recursive)

```python
class Solution(object):
    # @param {NestedInteger[]} nestedList a list of NestedInteger Object
    # @return {int} an integer
    def depthSum(self, nestedList):
        # Write your code here
        rtn, q = 0, [(i, 1) for i in nestedList]
        while q:
            item = q.pop(0)
            if item[0].isInteger():
                rtn += item[0].getInteger() * item[1]
            else:
                q += [(i, item[1] + 1) for i in item[0].getList()]
        return rtn
```


