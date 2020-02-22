---
layout: post
title: "maximum-swap"
published: true
created:  2020 Feb 21 11:55:40 AM
tags: [leetcode, number, medium, int, list]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[670] Maximum Swap](https://leetcode.com/problems/maximum-swap/description/)

|| [leetcode show 670]
|| 
|| * algorithms
|| * Medium (41.51%)
|| * Likes:    744
|| * Dislikes: 54
|| * Total Accepted:    50.9K
|| * Total Submissions: 122.3K
|| * Testcase Example:  '2736'
|| 
|| Given a non-negative integer, you could swap two digits at most once to get
|| the maximum valued number. Return the maximum valued number you could get.
|| 
|| Example 1:
|| 
|| Input: 2736
|| Output: 7236
|| Explanation: Swap the number 2 and the number 7.
|| 
|| Example 2:
|| 
|| Input: 9973
|| Output: 9973
|| Explanation: No swap.
|| 
|| Note:
|| 
|| The given number is in the range [0, 10^8]

# ping

## failed

```python
class Solution:
    def maximumSwap(self, num: int) -> int:
        #print("get num: ", num)
        str1 = str(num)
        list1=list(str1)
        len1 = len(list1)
        for i in range(len1-1):
            maxj = max(s for s in list1[i+1:])
            slipped = False
            for j in range(i+1, len1):
                if list1[j] == maxj:
                    while j<len1 and list1[j] == maxj:
                        j += 1
                        slipped = True
                    if slipped:
                        j -= 1
                        break
            #print("found the swap j: ", j)
            if  list1[i] < list1[j] and i is not j:
                list1[i], list1[j] = list1[j], list1[i]
                break
        return int(''.join(list1))
```

## passed

```python
class Solution:
    def maximumSwap(self, num: int) -> int:
        list1=list(str(num))            #convert to list, for max, swapping, etc
        len1 = len(list1)
        for i in range(len1-1):                         #for each digit
            maxj = max(s for s in list1[i+1:])          #find max from the rest
            for j in range(len1-1, i, -1):              #locate it from the end
                if list1[j] == maxj: break              #  backward
            if  list1[i] < list1[j] and i is not j:     #if worth to swap
                list1[i], list1[j] = list1[j], list1[i] #  swap it
                break
        return int(''.join(list1))
```

    ||   ✔ Accepted
    ||   ✔ 111/111 cases passed (32 ms)
    ||   ✔ Your runtime beats 20.67 % of python3 submissions
    ||   ✔ Your memory usage beats 100 % of python3 submissions (12.6 MB)

```python
S=Solution()
num=2736
S.maximumSwap(num)
num=9973
S.maximumSwap(num)
num=1993
S.maximumSwap(num)
num=10909091
S.maximumSwap(num)
```

# lmv

```python
class Solution:
    def maximumSwap(self, num: int) -> int:
        if num < 11:
            return num
        if num > 10 ** 8:
            return 0

        original_num = list(str(num))
        new_num = original_num[:]

        for i in range(len(original_num)):
            for j in range(i + 1, len(original_num)):
                # Swap
                original_num[i], original_num[j] = original_num[j], original_num[i]
                if new_num < original_num:
                    new_num = original_num[:]
                # Swap back
                original_num[i], original_num[j] = original_num[j], original_num[i]

        return int("".join(new_num))
```



