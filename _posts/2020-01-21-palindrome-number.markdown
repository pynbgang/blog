---
layout: post
title: "palindrome-number"
published: true
created:  2020 Jan 21 01:59:22 PM
tags: [easy, python, lintcode]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [palindrome-number](https://www.lintcode.com/problem/palindrome-number/description)

## ping

```python
class Solution:
    """
    @param num: a positive number
    @return: true if it's a palindrome or false
    """

    def isPalindrome(self, num):
        # write your code here
        tmp=[]
        revnum=self.revnum(num, tmp)
        return num == revnum

    def revnum(self, num, tmp):

        remainder = num % 10
        leftover = num // 10
        tmp.append(remainder)
        sum=0
        if leftover > 0:
            sum=self.revnum(leftover, tmp)
            return sum  #<---must have
        else:
            tmp.reverse()
            for i in range(len(tmp)):
                sum+=tmp[i] * pow(10,i)
            return sum
```

## wangmazi

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
        tmp = x
        rev = 0
        while tmp :
            rev = rev * 10 + tmp % 10
            tmp /= 10
        return rev == x
```

## cheat (best)

```python
class Solution:
    def isPalindrome(self, num):
        # write your code here
        return num == int(str(num)[::-1])
```

