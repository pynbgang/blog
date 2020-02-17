---
layout: post
title: "longest-palindrome"
published: true
created:  2020 Jan 21 01:28:00 PM
tags: [dict, python, module, Counter, easy, lintcode]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [longest-palindrome](https://www.lintcode.com/problem/longest-palindrome/description?_from=ladder&&fromId=99)

## wangmazi

```python
class Solution:
    # @param {string} s a string which consists of lowercase or uppercase letters
    # @return {int} the length of the longest palindromes that can be built

    # the answer is the count of characters that has even number of appereances.
    # for characters that has odd number of appereances,
    # their appereances minus 1 will make their apperances even.
    # And finally we can put an unused character in the middle of the palindrome
    def longestPalindrome(self, s):
        # Write your code here

        ## get those letters appeared odd times
        hash = {}
        for c in s:
            if c in hash:
                del hash[c]
            else:
                hash[c] = True

        ## get its length
        remove = len(hash)

        ## if there is any odd counts, plus 1
        return len(s) - remove +1 if remove else len(s)
```

## jj (best)

```python
def longestPalindrome(self, s):
    # write your code here

    ##count each letters
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1

    ##how many letters that appears odd times?
    ##2 conditions:
    ##  - 1 time (single letter): won't be useful except 1 of them
    ##  - 3,5, times (odd letter)  : can be used only even times (except just one letter)
    n = sum([1 for v in d.values() if v % 2 == 1])

    return len(s) - n + 1 if n else len(s)
```

```python
def longestPalindrome(self, s):
    # write your code here
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    n = sum([1 for v in d.values() if v % 2 == 1])
    return sum(d.values()) - n + 1 if n else sum(d.values())
```

## ping

```python
class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built with these
    letters, case sensitive
    """
    def longestPalindrome(self, s):
        # write your code here

        #count each letter
        d={}
        for l in s:
            d[l]=d[l]+1 if l in d else 1

        #check if there is at least:
        #  - one "extra" single letter, or
        #  - duplicated letter but the number of appearance is odd
        #in either case, just check if there is any letter appears odd times
        #because if yes, then result is sum of their even number (by -1)  plus 1

        extra=False
        for i in d:
            if d[i] % 2:
                d[i] -= 1
                extra=True

        #get sum of count for all duplicated letters
        sum1=sum([d[i] for i in d])
        return sum1+1 if extra else sum1
```

## ping (Counter version+stolen idea)

with Counter: "plus" idea (sum of even plus 1 if there is odd ever)

```python
    def longestPalindrome(self, s):
        # write your code here
        d2=collections.Counter(collections.Counter(s).values())
        sums=0, hasodd=False
        for k,v in d2.items():
            if k % 2: hasodd=True
            sums+=v*(k if not k%2 else k-1)
        return sums+1 if hasodd else sums
```

with Counter: "minus" idea (total_len - sum_of_odd + 1 if there is odd ever)

```python
    def longestPalindrome(self, s):
        # write your code here
        oddsum=sum([1 for v in collections.Counter(s).values() if v % 2])
        return len(s)-oddsum+1 if oddsum else len(s)
```
