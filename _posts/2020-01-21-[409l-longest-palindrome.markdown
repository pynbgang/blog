---
layout: post
title: "[409] longest-palindrome"
published: true
created:  2020 Jan 21 01:28:00 PM
tags: [dict, python, module, Counter, easy, lintcode, collections]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[409] Longest Palindrome](https://leetcode.com/problems/longest-palindrome/)

    ||Given a string which consists of lowercase or uppercase letters, find the
    length of the longest palindromes that can be built with those letters.
    ||
    ||This is case sensitive, for example "Aa" is not considered a palindrome here.
    ||
    ||Note:
    ||Assume the length of given string will not exceed 1,010.
    ||
    ||Example:
    ||
    ||Input:
      "abccccdd"

    ||Output:
    ||7
    ||Explaination: One longest palindrome that can be built is "dccaccd", whose length is 7.


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

## jj ("minus" idea: smart)


```python
def longestPalindrome(self, s):
    # write your code here

    ##count each letters
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1

    n = sum(1 for v in d.values() if v % 2)

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

## ping: 

### solution1

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

### solution2

```python
#(2020-08-28) 
class Solution:
    def longestPalindrome(self, s: str) -> int:
        d, count, isthereodd = {}, 0, 0
        for i in s:
            d[i] = d.get(i, 0) + 1
        for i in d.values():
            if not i % 2:
                count += i
            if i % 2:
                count += i-1
                if not isthereodd:
                    count += 1
                    isthereodd = 1
        return count
```


### Counter version

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
        oddsum=sum(1 for v in collections.Counter(s).values() if v % 2)
        return len(s)-oddsum+1 if oddsum else len(s)
```

## Owen

```python
class Solution(object):
    def longestPalindrome(self, s):
        if len(s)==1:return 1
        dict1={}
        for i in s:dict1[i]=dict1.get(i,0)+1
        even=0
        flag=False
        for i in dict1.keys():
            if dict1[i]%2==0:
                even+=dict1[i]
            else:
                flag=True
                even+=dict1[i]-1
        if flag:return even+1
        return even
```

## tips

### "plus" idea:

just add up even and odd nums seperately and carefully.

### "minus" idea:

if a letter appear even times, then just add the count of it into result.
if a letter appear odd time(s), it's kind of tricky:

2 conditions:

- a letter appears just 1 time: won't be useful except only 1 of them
- a letter appears n(>1) times : the extra 1 time for each letter can't be
  used, except only 1 of them

so overall, need to minus 1 from each every letter which appears odd times, and
plus 1 -- that is if there is any "odd time" letter.

