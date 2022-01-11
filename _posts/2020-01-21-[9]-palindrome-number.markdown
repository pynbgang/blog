---
layout: post
title: "[9] palindrome-number"
published: true
created:  2020 Jan 21 01:59:22 PM
tags: [easy, python, lintcode, leetcode, recursion, goodone]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[9] Palindrome Number](https://leetcode.com/problems/palindrome-number/description/)

    || * algorithms
    || * Easy (46.45%)
    || * Likes:    1959
    || * Dislikes: 1484
    || * Total Accepted:    820.1K
    || * Total Submissions: 1.8M
    || * Testcase Example:  '121'
    ||
    || Determine whether an integer is a palindrome. An integer is a palindrome
    when it reads the same backward as forward.
    ||
    || Example 1:
    ||
    || Input: 121
    || Output: true
    ||
    || Example 2:
    ||
    || Input: -121
    || Output: false
    || Explanation: From left to right, it reads -121. From right to left, it
    becomes 121-. Therefore it is not a palindrome.
    ||
    || Example 3:
    ||
    || Input: 10
    || Output: false
    || Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
    ||
    ||
    || Follow up:
    ||
    || Coud you solve it without converting the integer to a string?

see also: [palindrome-number](https://www.lintcode.com/problem/palindrome-number/description)

## int/str (best, cheat way)

```python
class Solution:
    def isPalindrome(self, num):
        # write your code here
        return num == int(str(num)[::-1])
```

## wangmazi (good)

```python
class Solution(object):
    '''
    题意：判断数字是否为回文数
    翻转数字比较相等即可
    注意负数不是回文数
    '''
    def isPalindrome(self, x):
        if x < 0 :
            return False
        orig_num, rev_num = x, 0
        while orig_num:
            orig_num, remainder  = orig_num // 10, orig_num % 10
            #or with divmod:
            #orig_num, remainder  = divmod(orig_num, 10)
            rev_num = rev_num * 10 + remainder
        return rev_num == x
```

## ping: with divmod

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        rev, div = 0, x
        while div:
            div, mod = divmod(div, 10)
            rev      = rev * 10 + mod
        return rev == x
```

## ping (harder way: recursion)

```python
class Solution:
    """
    @param num: a positive number
    @return: true if it's a palindrome or false
    """

    def isPalindrome(self, num):
        # write your code here
        return num == self.revnum(num, [])

    def revnum(self, num, tmp):

        div, mod = divmod(num, 10)
        tmp.append(mod)
        sum=0
        if div:
            sum=self.revnum(div, tmp)
            return sum  #<---must have
        else:
            tmp.reverse()
            for i in range(len(tmp)):
                sum+=tmp[i] * pow(10,i)
            return sum
```
