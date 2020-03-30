---
layout: post
title: "[22] Generate Parentheses"
published: true
created:  2020 Mar 23 03:32:50 PM
tags: [python, leetcode, dfs, dp, medium, recursion]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[22] Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)

    || * algorithms
    || * Medium (59.38%)
    || * Likes:    4333
    || * Dislikes: 234
    || * Total Accepted:    487.2K
    || * Total Submissions: 808.1K
    || * Testcase Example:  '3'
    || * Source Code:       22.generate-parentheses.py
    || 
    || Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
    || 
    || For example, given n = 3, a solution set is:
    || 
    || [
    || ⁠ "((()))",
    || ⁠ "(()())",
    || ⁠ "(())()",
    || ⁠ "()(())",
    || ⁠ "()()()"
    || ]

## owen fake DP
DP is not best way in this case...since using to many for,if i can optimize to 2 for ,it must beat DFS

```python
class Solution(object):
    def generateParenthesis(self, n):
        if n==0:return []
        if n==1:return ["()"]
        if n==2:return ["()()","(())"]
        temp=["()()","(())"]
        temp1=set()
        for i in range(3,n+1):
            for j in temp:
                temp1.add("()"+j)
                temp1.add(j+"()")
                temp1.add("("+j+")")
                m=self.helper(j)
                for x in range(1,len(m)-1):
                    for y in range(x+1,len(m)):
                        if m[y][1]-m[x][1]==m[y][0]-m[x][0]+1:
                            temp1.add(j[0:x]+"("+j[x:y+1]+")"+j[y+1:]) 
            temp=list(temp1)
            temp1=set()
        return temp   
    def helper(self,str1):
        l=[]
        count0,count1=0,0
        for i in str1:
            if i=="(":count0+=1
            if i==")":count1+=1
            l.append((count0,count1))
        return l
```

## lmv: solution1

```python
class Solution:     #lmv
    def generateParenthesis(self, n):
        def generate(p, left, right, parens=[]):
            if left:         generate(p + '(', left-1, right)
            if right > left: generate(p + ')', left, right-1)
            if not right:    parens += p,
            return parens
        return generate('', n, n)
```

4-7 lines Python
https://leetcode.com/problems/generate-parentheses/discuss/10096

* Lang:    python3
* Author:  StefanPochmann
* Votes:   200

`p` is the parenthesis-string built so far, `left` and `right` tell the number
of left and right parentheses still to add, and `parens` collects the
parentheses.

### debug code with print

```python
class Solution:     #lmv debug
    def generateParenthesis(self, n):
        self.spaces=0
        def generate(p, left, right, parens=[]):
            if left:
                print(' '*self.spaces, 'left not 0, use left...', sep='')
                print(' '*self.spaces+'L:generate(', '"', p, '+(', '",', left-1, ',', right, ')', sep='')
                self.spaces+=4
                generate(p + '(', left-1, right)
            if right > left:
                print(' '*self.spaces, 'right bigger, use right...', sep='')
                print(' '*self.spaces+'R:generate(', '"', p, '+)', '",', left, ',', right-1, ')', sep='')
                self.spaces+=4
                generate(p + ')', left, right-1)
            if not right:
                parens += p,
                print(' '*self.spaces, 'right 0...', sep='')
                print(' '*self.spaces+'get', '"', p, '"', sep='')
            print(' '*self.spaces+'return', sep='')
            self.spaces-=4
            return parens
        print("start...")
        print('generate(', '"",', n, ',', n, ')', sep='')
        return generate('', n, n)

S=Solution()
S.generateParenthesis(2)
```

output:

    start...
    generate("",2,2)
    left not 0, use left...
    L:generate("+(",1,2)
        left not 0, use left...
        L:generate("(+(",0,2)
            right bigger, use right...
            R:generate("((+)",0,1)
                right bigger, use right...
                R:generate("(()+)",0,0)
                    right 0...
                    get"(())"
                    return
                return
            return
        right bigger, use right...
        R:generate("(+)",1,1)
            left not 0, use left...
            L:generate("()+(",0,1)
                right bigger, use right...
                R:generate("()(+)",0,0)
                    right 0...
                    get"()()"
                    return
                return
            return
        return
    return
    Out[92]: ['(())', '()()']

## lmv: solution2

```python
class Solution:     #lmv
    """
    **Solution 2**

    Here I wrote an actual Python generator. I allow myself to put the `yield q` at
    the end of the line because it's not that bad and because in "real life" I use
    Python 3 where I just say `yield from generate(...)`.
    """

    def generateParenthesis(self, n):
        def generate(p, left, right):
            if right >= left >= 0:
                if not right:
                    yield p
                for q in generate(p + '(', left-1, right): yield q
                for q in generate(p + ')', left, right-1): yield q
        return list(generate('', n, n))
```

## lmv
```python
class Solution:     #lmv
    """
    **Solution 3**

    Improved version of
    [this](https://leetcode.com/discuss/25725/7-lines-in-python-44-ms). Parameter
    `open` tells the number of "already opened" parentheses, and I continue the
    recursion as long as I still have to open parentheses (`n > 0`) and I haven't
    made a mistake yet (`open >= 0`).
    """

    def generateParenthesis(self, n, open=0):
        if n > 0 <= open:
            return ['(' + p for p in self.generateParenthesis(n-1, open+1)] + \\
                   [')' + p for p in self.generateParenthesis(n, open-1)]
        return [')' * open] * (not n)
```

