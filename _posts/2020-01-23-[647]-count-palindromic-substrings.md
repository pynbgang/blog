---
layout: post
title: "[647] Palindromic Substrings"
subtitle: "abc"
date: 2020-01-23
author: "Owen"
tags:
    - lintcode
    - medium
    - python
    - google
    - interview
    - string
    - wangmazi
    - pending
    - goodone
created:  20120 Jan 23 00:14:49 AM
categories: [tech]
published: true

---


TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[647] Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/description/)

    || * algorithms
    || * Medium (59.02%)
    || * Likes:    2903
    || * Dislikes: 120
    || * Total Accepted:    200.1K
    || * Total Submissions: 328.9K
    || * Testcase Example:  '"abc"'
    || * Source Code:       647.palindromic-substrings.py
    ||
    || Given a string, your task is to count how many palindromic substrings in this string.
    ||
    || The substrings with different start indexes or end indexes are counted as
    different substrings even they consist of same characters.
    ||
    || Example 1:
    || Input: "abc"
    || Output: 3
    || Explanation: Three palindromic strings: "a", "b", "c".
    ||
    || Example 2:
    || Input: "aaa"
    || Output: 6
    || Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
    ||
    || Note:
    ||
    || 	The input string length won't exceed 1000.

see also [palindromic-substrings](https://www.lintcode.com/problem/palindromic-substrings/description)

## Owen(within helper function On2)

```python
class Solution:

    def countPalindromicSubstrings(self, str):
        if not str:
            return 0
        if len(str)==1:
            return 1
        lenth=len(str)
        count=0
        for i in range(lenth):
            for j in range(i+1,lenth+1):
                if self.checkPalindromic(str[i:j]):
                    count+=1
        return count
    ###helper function to check if it is Palindromic####
    def checkPalindromic(self,str123):
        if len(str123)==1:
            return True
        i=0
        j=len(str123)-1
        while(i<j):
            if str123[i]!=str123[j]:
                return False
            i+=1
            j-=1
        return True
```

## High voted answer (wangmazi)

考虑如果substring(i,j)是回文串，那么str[i]和str[j]一定相同，并且一定满足以
下两个条件之一:

1. substring(i+1,j-1)也是回文串
2. `j-i<=2`，即substring(i,j)长度 `<=` 2

那么我们就只需要顺着这个思路dp就行了，复杂度On2

```python
class Solution:
    def countPalindromicSubstrings(self, str):
        dp = [[0 for j in range(len(str))] for i in range(len(str))]
        ans = 0
        for i in range(len(str)):
            for j in range(i + 1):
                if(str[j] == str[i] and (i - j <= 2 or dp[j + 1][i - 1] == 1)):
                    #pending: need to understand
                    dp[j][i] = 1
                ans += dp[j][i]
        return ans
```

## lmv

### idea

This problem, like many, is all about optimization. The naive solution would be
to check if each and every substring is a palindrome, but that would easily
achieve a **TLE** result.

Instead, the first realization that we can make is that each larger palindrome
is built upon many layers of smaller p alindromes, going back to its center. So
we could optimize our solution by iterating through **S** and considering the
index **i** to be the center of a series of potential palindromes.

Then, for each **i** we could use two more pointers (**j & k**) which would
spread out in both directions from **i**.  As long as **S[j] == S[k]**, we\'d
know we had found a new palindrome and could continue spreading outward.

We would have to duplicate this process for even-length palindromes, as their
center would be two characters intead of one.

But we can optimize more than that.

If we instead think of the center of the palindrome not as just one or two
characters, but as *any* length of repeated characters, then we can break each
iteration down into two steps.

First, we identify how long the "center" is by moving our right-size pointer
(**k**) forwards while checking for duplicate characters. Now, instead of our
center just being a single palindrome, it will be the **Nth triangular number**
(defined as **N * (N + 1) / 2**) to account for all the smaller palindromes of
which it\'s made.

After that, we can spread out with **j** and **k** just as before. Since we\'ve
dealt with the entire center\'s worth of palindromes, we can move **i** forward
to start up again after the end of the center, regardless of its length.


### code

```python
class Solution:
    def countSubstrings(self, S: str) -> int:
        ans, n, i = 0, len(S), 0
        while (i < n):
            j, k = i - 1, i
            while k < n - 1 and S[k] == S[k+1]: k += 1
            ans += (k - j) * (k - j + 1) // 2
            i, k = k + 1, k + 1
            while ~j and k < n and S[k] == S[j]:
                j, k, ans = j - 1, k + 1, ans + 1
        return ans
```

## ping: brute force :)

```python
class Solution:
    def countPalindromicSubstrings(self, str):
        count=0
        for i in range(len(str)):
            for j in range(i+1, len(str)+1):
                if str[i:j]==str[i:j][::-1]:
                    count+=1
        return count
```

or, oneliner with generator:

use `int` to convert `True/False` to `1/0`

```python
class Solution:
    def countPalindromicSubstrings(self, str):
        return sum((int(str[i:j]==str[i:j][::-1]) for i in range(len(str)) for j in range(i+1, len(str)+1)))
```

lintcode: time limit exceeded

or:

```python
class Solution:
    def countPalindromicSubstrings(self, str):
        return sum(
            ( 1 for i in
                (str[i:j] for i in range(len(str)) for j in range(i+1, len(str)+1)) if i==i[::-1]
            )
        )
```


```python
#revisit: (Sat 29 Aug 2020 07:48:04 PM DST)
class Solution:
    def countSubstrings(self, s: str) -> int:
        return sum(s[i:j] == s[i:j][::-1] for i in range(len(s)) for j in range(i+1, len(s)+1))
```

## others 双指针中心扩展

https://maxming0.github.io/2021/03/27/Palindromic-Substrings/

### 思路

    双指针，l, r, 初始化0， 0，进入主循环,
    主循环中设法在每次循环中， l, r轮番加一:
        这次r加1，  下次l加1
        观察s[l]=s[r]字符是否相同
        如果相同，进入二重循环, 向外扩展:
            计数加一
            l-1
            r+1
            再次观察s[l]=s[r]字符是否相同

### 代码

```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        l = len(s)
        for mid in range(l * 2 - 1):
            left = mid // 2
            right = left + mid % 2
            while left >= 0 and right < l and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        return res
```

### 调试版：
```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        l = len(s)
        for mid in range(l * 2 - 1):
            left = mid // 2
            right = left + mid % 2
            print("try: l,r: ", left, right)
            while left >= 0 and right < l and s[left] == s[right]:
                print("\t got one:", s[left:right+1], "res:", res+1)
                res += 1
                left -= 1
                right += 1
                print("\t try: l,r: ", left, right)
            else:
                print("\t not one:", s[left:right+1], "res:", res)
        return res
S=Solution()
s="abcdc"
S.countSubstrings(s)
```

    try: l,r:  0 0
            got one: a res: 1
            try: l,r:  -1 1
            not one:  res: 1
    try: l,r:  0 1
            not one: ab res: 1
    try: l,r:  1 1
            got one: b res: 2
            try: l,r:  0 2
            not one: abc res: 2
    try: l,r:  1 2
            not one: bc res: 2
    try: l,r:  2 2
            got one: c res: 3
            try: l,r:  1 3
            not one: bcd res: 3
    try: l,r:  2 3
            not one: cd res: 3
    try: l,r:  3 3
            got one: d res: 4
            try: l,r:  2 4
            got one: cdc res: 5
            try: l,r:  1 5
            not one: bcdc res: 5
    try: l,r:  3 4
            not one: dc res: 5
    try: l,r:  4 4
            got one: c res: 6
            try: l,r:  3 5
            not one: dc res: 6
    Out[206]: 6
