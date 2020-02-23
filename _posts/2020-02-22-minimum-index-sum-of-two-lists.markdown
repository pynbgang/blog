---
layout: post
title: "minimum index sum of two lists"
published: true
created:  2020 Feb 22 09:06:40 PM
tags: [python, leetcode, easy, list, dict]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[599] Minimum Index Sum of Two Lists](https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/)

|| * algorithms
|| * Easy (49.59%)
|| * Likes:    479
|| * Dislikes: 177
|| * Total Accepted:    77.5K
|| * Total Submissions: 155.9K
|| * Testcase Example:  '["Shogun","Tapioca Express","Burger King","KFC"]\n["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]'
|| * Source Code:       599.minimum-index-sum-of-two-lists.py
|| 
|| 
|| Suppose Andy and Doris want to choose a restaurant for dinner, and they both
|| have a list of favorite restaurants represented by strings. 
|| 
|| You need to help them find out their common interest with the least list
|| index sum. If there is a choice tie between answers, output all of them with no
|| order requirement. You could assume there always exists an answer.
|| 
|| 
|| Example 1:
|| 
|| Input:
|| ["Shogun", "Tapioca Express", "Burger King", "KFC"]
|| ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
|| Output: ["Shogun"]
|| Explanation: The only restaurant they both like is "Shogun".
|| 
|| Example 2:
|| 
|| Input:
|| ["Shogun", "Tapioca Express", "Burger King", "KFC"]
|| ["KFC", "Shogun", "Burger King"]
|| Output: ["Shogun"]
|| Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
|| 
|| 
|| Note:
|| 
|| The length of both lists will be in the range of [1, 1000].
|| The length of strings in both lists will be in the range of [1, 30].
|| The index is starting from 0 to the list length minus 1.
|| No duplicates in both lists.

## ping
```python
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common, d = set(list1) & set(list2), {}
        for one in common:
            d[one] = list1.index(one) + list2.index(one)
        return [k for k in d if d[k] == min(d.values())]
```

## lmv

```python
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = {x: list1.index(x) + list2.index(x) for x in set(list1) & set(list2)}
        return [x for x in d if d[x] == min(d.values())]
```

tips:
* dict comprehension!


