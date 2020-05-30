---
layout: post
title: "[1341] The K Weakest Rows in a Matrix"
published: true
created:  2020 May 30 12:22:28 PM
tags: [python, leetcode, easy, sum, sort, list]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[1341] The K Weakest Rows in a Matrix](https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/description/)

    || * algorithms
    || * Easy (68.58%)
    || * Likes:    210
    || * Dislikes: 14
    || * Total Accepted:    21.4K
    || * Total Submissions: 31.3K
    || * Testcase Example:  '[[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]\n3'
    || * Source Code:       1341.the-k-weakest-rows-in-a-matrix.py
    || 
    || Given a m * n matrix mat of ones (representing soldiers) and
    zeros (representing civilians), return the indexes of the k weakest rows in
    the matrix ordered from the weakest to the strongest.
    || 
    || A row i is weaker than row j, if the number of soldiers in row i is less
    than the number of soldiers in row j, or they have the same number of
    soldiers but i is less than j. Soldiers are always stand in the frontier of
    a row, that is, always ones may appear first and then zeros.
    || 
    ||  
    || Example 1:
    || 
    || 
    || Input: mat = 
    || [[1,1,0,0,0],
    || ⁠[1,1,1,1,0],
    || ⁠[1,0,0,0,0],
    || ⁠[1,1,0,0,0],
    || ⁠[1,1,1,1,1]], 
    || k = 3
    || Output: [2,0,3]
    || Explanation: 
    || The number of soldiers for each row is: 
    || row 0 -> 2 
    || row 1 -> 4 
    || row 2 -> 1 
    || row 3 -> 2 
    || row 4 -> 5 
    || Rows ordered from the weakest to the strongest are [2,0,3,1,4]
    || 
    || 
    || Example 2:
    || 
    || 
    || Input: mat = 
    || [[1,0,0,0],
    ||  [1,1,1,1],
    ||  [1,0,0,0],
    ||  [1,0,0,0]], 
    || k = 2
    || Output: [0,2]
    || Explanation: 
    || The number of soldiers for each row is: 
    || row 0 -> 1 
    || row 1 -> 4 
    || row 2 -> 1 
    || row 3 -> 1 
    || Rows ordered from the weakest to the strongest are [0,2,3,1]
    ||  
    || Constraints:
    || 
    || 	m == mat.length
    || 	n == mat[i].length
    || 	2 <= n, m <= 100
    || 	1 <= k <= m
    || 	matrix[i][j] is either 0 or 1.

## ping

* use tuple to record: (index of each row, sum of each row)
* use sort with key to sort per sum

```python
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        t=sorted([(i, (sum(mat[i]))) for i in range(len(mat))], key=lambda x: x[1])
        return [t[i][0] for i in range(k)]
```

## lmv

    || [Python] One-Liner using Sorting
    || 
    || https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/discuss/496713
    || 
    || * Lang:    python3
    || * Author:  C0R3
    || * Votes:   30
    || 
    || We can sort the indexes of the weakest rows by using their sums as the key in sorting. Then we return the k first values.
    || ```python
    || class Solution:
    ||     def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
    ||         return sorted(range(len(mat)), key=lambda x: sum(mat[x]))[:k]
    || ```
    || Calculating the sum of a row has a time complexity of ```O(n)``` and is done ```m``` times. Python\'s key function will do a [Schwartzian transform](https://en.wikipedia.org/wiki/Schwartzian_transform) and cache the sums. Sorting has a complexity of ```O(m log m)```.
    || 
    || Time complexity: ```O(n * m + m log m)```
    || Space complexity: ```O(m)```
    || 
    || **Long and optimized algorithm**
    || 
    || If we want to improve on this we have to use more lines of code. We have to return the sorted indexes of the k weakest rows. Heaps allow us to sort an input while keeping only the desired k items in memory.
    || Heaps in Python will pop the smallest values first. Therefore we need to push tuples with inverted values onto our heap.
    || We still have to iterate over all rows in ```O(m)```. But now we only need ```O(log k)``` to add a value to the heap. We also need only ```O(k)``` space.
    || We can further improve our algorithm by using binary search to find the number of soldiers. That reduces the complexity per row to ```O(log n)```.
    || In the end our heap contains the desired row indexes. But they are not yet sorted. Therefore we need to push them onto a list until the heap is exhausted. We also discard the numbers of rows and invert the indexes back.
    || Since the heap returns the maximum items first we need to return the list in reversed order.
    || 
    || Time complexity: ```O(m * (log n + log k) + k log k)```
    || Space complexity: ```O(k)```
    || ```python
    || from heapq import heappushpop, heappush, heappop
    || 
    || class Solution:
    ||     def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
    ||         heap = [] # Size: O(k)
    ||         
    ||         # Iterate over the rows in O(m).
    ||         for index, row in enumerate(mat):
    ||             soldier_count = self.soldier_count(row)
    ||             
    ||             # Push values to the heap in O(log k)
    ||             if len(heap) == k:
    ||                 heappushpop(heap, (-soldier_count, -index))
    ||             else:
    ||                 heappush(heap, (-soldier_count, -index))
    ||         
    ||         weakest_rows = [] # Size: O(k)
    ||         
    ||         # Push the heap values into our result list in O(k log k).
    ||         while heap:
    ||             weakest_rows.append(-heappop(heap)[1])
    ||         
    ||         # Return the result in reversed order.
    ||         return weakest_rows[::-1]
    ||     
    ||     # Find the number of soldiers in a row using Binary Search in O(log n).
    ||     def soldier_count(self, row: List[int]) -> int:
    ||         low, high = 0, len(row) - 1
    || 
    ||         while low < high:
    ||             mid = (low + high + 1) // 2
    || 
    ||             if not row[mid]:
    ||                 high = mid - 1
    ||             else:
    ||                 low = mid
    || 
    ||         # We need to return a count and not an index.
    ||         # Therefore we need to increase the result by one if soldiers have been found.
    ||         if row[0]:
    ||             low += 1
    ||         
    ||         return low
    || ```
    || 
    || **Optimized One-Liner**
    || 
    || This algorithm caches the row sums and uses heapq to keep the complexity down. The heap is filled using a generator expression with enumerate to keep the space complexity low. Sadly the built-in bisect can\'t be used because the rows would have to be reversed and that would take as long as taking the sum directly.
    || 
    || Time complexity: ```O(m * n + k log k)```
    || Space complexity: ```O(k)```
    || ```python
    || class Solution:
    ||     def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
    ||         return [x[1] for x in heapq.nsmallest(k, ((sum(s), i) for i, s in enumerate(mat)))]
    || ```
    || [Finished in 3 seconds]

