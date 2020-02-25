---
layout: post
title: "sort-colors"
published: true
created:  2020 Feb 25 12:29:47 PM
tags: [lintcode, easy, list, python, brute force, wangmazi]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# sort-colors

https://www.lintcode.com/problem/sort-colors/description?_from=ladder&&fromId=99

## mine

```python
class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    def sortColors(self,nums):
        # write your code here
        #this is not allowed:
        #return nums.sort()

        #this should be allowed?
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] < nums[i]:
                    nums[i],nums[j]=nums[j],nums[i]
        return nums
```


## wangmazi

使用一次扫描的办法。
设立三根指针，left, index, right。定义如下规则：

left 的左侧都是 0（不含 left）
right 的右侧都是 2（不含 right）
index 从左到右扫描每个数，如果碰到 0 就丢给 left，碰到 2 就丢给 right。碰到 1 就跳过不管。

```python
class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    def sortColors(self, A):
        left, index, right = 0, 0, len(A) - 1
        # be careful, index < right is not correct
        while index <= right:
            if A[index] == 0:
                A[left], A[index] = A[index], A[left]
                left += 1
                index += 1 # move to next number
            elif A[index] == 2:
                A[right], A[index] = A[index], A[right]
                right -= 1
            else:  # == 1, skip
                index += 1
```

## wangmazi illustration

![image](https://user-images.githubusercontent.com/2038044/70585018-db7f1200-1b90-11ea-8437-aa0b4372b91a.png)

