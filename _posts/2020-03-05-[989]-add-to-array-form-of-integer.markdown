---
layout: post
title: "[989] Add to Array-Form of Integer"
published: true
created:  2020 Mar 05 10:08:19 PM
tags: [python, leetcode, easy, string, str, int]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[989] Add to Array-Form of Integer](https://leetcode.com/problems/add-to-array-form-of-integer/description/)

    || * algorithms
    || * Easy (44.09%)
    || * Likes:    251
    || * Dislikes: 50
    || * Total Accepted:    32.1K
    || * Total Submissions: 72.8K
    || * Testcase Example:  '[1,2,0,0]\n34'
    || * Source Code:       989.add-to-array-form-of-integer.py
    || 
    || For a non-negative integer X, the array-form of X is an array of its
    digits in left to right order.  For example, if X = 1231, then the array
    form is [1,2,3,1].
    || 
    || Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.
    || 
    || Example 1:
    || Input: A = [1,2,0,0], K = 34
    || Output: [1,2,3,4]
    || Explanation: 1200 + 34 = 1234
    || 
    || Example 2:
    || Input: A = [2,7,4], K = 181
    || Output: [4,5,5]
    || Explanation: 274 + 181 = 455
    || 
    || Example 3:
    || Input: A = [2,1,5], K = 806
    || Output: [1,0,2,1]
    || Explanation: 215 + 806 = 1021
    || 
    || Example 4:
    || Input: A = [9,9,9,9,9,9,9,9,9,9], K = 1
    || Output: [1,0,0,0,0,0,0,0,0,0,0]
    || Explanation: 9999999999 + 1 = 10000000000
    || 
    || Note：
    || 	1 <= A.length <= 10000
    || 	0 <= A[i] <= 9
    || 	0 <= K <= 10000
    || 	If A.length > 1, then A[0] != 0

## ping: str, int

```python
class Solution:  #ping
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        return str(int(''.join(str(i) for i in A))+K)
        """
        ||   ✔ Accepted
        ||   ✔ 156/156 cases passed (316 ms)
        ||   ✔ Your runtime beats 66.76 % of python3 submissions
        ||   ✔ Your memory usage beats 55 % of python3 submissions (13.6 MB)
        """
```

## lmv

    || [Python3] Improving the Leetcode Solution and Avoiding the Use of 'str', 'int' and 'map'
    || 
    || https://leetcode.com/problems/add-to-array-form-of-integer/discuss/437674
    || 
    || * Lang:    python3
    || * Author:  Dr_Sean
    || * Votes:   6
    || 
    || # Notes:
    || - Leetcode provided a simple [solution](https://leetcode.com/problems/add-to-array-form-of-integer/solution/), but it is not efficient. K has 5 digits at most, but A can have 10000 elements. This means that the summation might finish after 5 iterations, but the loop will continue for 10000 times! I added a condition to avoid this.
    || - I think the purpose of this question is to provide a summation based on elementary school math, and avoid other functions such as \'str\', \'int\' and \'map\'. 
    || - The Leetcode solution does not work for Python3, but slight changes would make it compatible for both Python/ Python3.
    || 
    || 
    || # Python/ Python3 code:
    || ```
    ||         for i in range(len(A) - 1, -1, -1):
    ||             if not K: break
    ||             K, A[i] = divmod(A[i] + K, 10)
    ||         while K:
    ||             K, a = divmod(K, 10)
    ||             A = [a] + A
    ||         return A
    || ```

