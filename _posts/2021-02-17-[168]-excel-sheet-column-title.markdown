---
layout: post
title: "[168] Excel Sheet Column Title"
published: true
created:  2021 Feb 17 23:02:12
tags: [python, leetcode, easy]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -


# [[168] Excel Sheet Column Title](https://leetcode.com/problems/excel-sheet-column-title/description/)

    || * algorithms
    || * Easy (31.51%)
    || * Likes:    1569
    || * Dislikes: 286
    || * Total Accepted:    244.8K
    || * Total Submissions: 772.2K
    || * Testcase Example:  '1'
    || * Source Code:       168.excel-sheet-column-title.py
    || 
    || Given a positive integer, return its corresponding column title as
    appear in an Excel sheet.
    || 
    || For example:
    || 
    || ⁠   1 -> A
    || ⁠   2 -> B
    || ⁠   3 -> C
    || ⁠   ...
    || ⁠   26 -> Z
    || ⁠   27 -> AA
    || ⁠   28 -> AB 
    || ⁠   ...
    || 
    || Example 1:
    || 
    || Input: 1
    || Output: "A"
    || 
    || Example 2:
    || 
    || Input: 28
    || Output: "AB"
    || 
    || Example 3:
    || 
    || Input: 701
    || Output: "ZY"

# solution

```python
class Solution:     #ping
    def convertToTitle(self, n: int) -> str:
        res = ""
        while n:
            res, n = chr(ord('A') + (n-1)%26) + res, (n-1)//26
        return res
        """
        ||   ✔ Accepted
        ||   ✔ 18/18 cases passed (32 ms)
        ||   ✔ Your runtime beats 52.05 % of python3 submissions
        ||   ✔ Your memory usage beats 11.03 % of python3 submissions (14.4 MB)
        """

class Solution:     #lmv
    # @return a string
    def convertToTitle(self, num):
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        result = []
        while num > 0:
            result.append(capitals[(num-1)%26])
            num = (num-1) // 26
        result.reverse()
        return ''.join(result)
```

    || https://leetcode.com/problems/excel-sheet-column-title/discuss/51404
    || 
    || * Lang:    python3
    || * Author:  yuzhiqiang
    || * Votes:   240
    || 
    || Let's see the relationship between the Excel sheet column title and the number:
    || 
        A   1     AA    26+ 1     BA  2×26+ 1     ...     ZA  26×26+ 1     AAA  1×26²+1×26+ 1
        B   2     AB    26+ 2     BB  2×26+ 2     ...     ZB  26×26+ 2     AAB  1×26²+1×26+ 2
        .   .     ..    .....     ..  .......     ...     ..  ........     ...  .............   
        .   .     ..    .....     ..  .......     ...     ..  ........     ...  .............
        .   .     ..    .....     ..  .......     ...     ..  ........     ...  .............
        Z  26     AZ    26+26     BZ  2×26+26     ...     ZZ  26×26+26     AAZ  1×26²+1×26+26
    || 
    || Now we can see that ABCD＝A×26³＋B×26²＋C×26¹＋D＝1×26³＋2×26²＋3×26¹＋4
    || 
    || But how to get the column title from the number? We can't simply use the n%26 method because:
    || 
    || ZZZZ＝Z×26³＋Z×26²＋Z×26¹＋Z＝26×26³＋26×26²＋26×26¹＋26
    || 
    || We can use (n-1)%26 instead, then we get a number range from 0 to 25.
    || 
    ||     class Solution:
    ||         # @return a string
    ||         def convertToTitle(self, num):
    ||             capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
    ||             result = []
    ||             while num > 0:
    ||                 result.append(capitals[(num-1)%26])
    ||                 num = (num-1) // 26
    ||             result.reverse()
    ||             return ''.join(result)

# tips

1. main headache is, this is like base 26 except:
* there is no 0, base26 will start with 0
* there is 26, base26 will stop at 25

so there is this `-1` mapping between excel and base26.

2. this is good:

        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]

    comparing with `[ABCDEFGHIJKLMNOPQRSTUVWXYZ]

