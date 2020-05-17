---
layout: post
title: "[744] find smallest letter greater Than target"
published: true
created:  2020 May 17 06:30:23 PM
tags: [python, leetcode, easy, sort, list]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -


# [[744] Find Smallest Letter Greater Than Target](https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/)

    || * algorithms
    || * Easy (44.86%)
    || * Likes:    348
    || * Dislikes: 470
    || * Total Accepted:    67.5K
    || * Total Submissions: 149.4K
    || * Testcase Example:  '["c","f","j"]\n"a"'
    || * Source Code:       744.find-smallest-letter-greater-than-target.py
    ||
    || Given a list of sorted characters letters containing only lowercase
    letters, and given a target letter target, find the smallest element in the
    list that is larger than the given target.
    ||
    || Letters also wrap around.  For example, if the target is target = 'z' and
    letters = ['a', 'b'], the answer is 'a'.
    ||
    || Examples:
    ||
    || Input:
    || letters = ["c", "f", "j"]
    || target = "a"
    || Output: "c"
    ||
    || Input:
    || letters = ["c", "f", "j"]
    || target = "c"
    || Output: "f"
    ||
    || Input:
    || letters = ["c", "f", "j"]
    || target = "d"
    || Output: "f"
    ||
    || Input:
    || letters = ["c", "f", "j"]
    || target = "g"
    || Output: "j"
    ||
    || Input:
    || letters = ["c", "f", "j"]
    || target = "j"
    || Output: "c"
    ||
    || Input:
    || letters = ["c", "f", "j"]
    || target = "k"
    || Output: "c"
    ||
    || Note:
    ||
    || letters has a length in range [2, 10000].
    || letters consists of lowercase letters, and contains at least 2 unique letters.
    || target is a lowercase letter.

# ping: merge, sort and index

```python
class Solution:  #ping
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters.append(target); letters.sort(reverse=True) #merge and reversely sort
        return letters[(letters.index(target) - 1)] #find the one ahead of target
```

# lmv: what the hack

Straightforward Solution from Scratch

https://leetcode.com/problems/find-smallest-letter-greater-than-target/discuss/577769

* Lang:    python3
* Author:  ragothaman
* Votes:   1

```python
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # Getting rid of duplicates - set()
                letters = sorted(set(letters))
        #-----------------------------------------------
        # where target character is in \'letters\'
        if target in letters:
            tindex = letters.index(target)
            if tindex + 1 < len(letters):
                return letters[tindex+1]
            elif tindex+1 == len(letters):
                return letters[0]

        # Where target character is not in \'letters\'
        else:
            begin = letters[0]
            end  = letters[-1]

            # Boundary conditions
            if target < begin or target >=end:
                return begin
            # If we reach here - it means, it\'s between one of the characters in \'letters\'
            else:
                for i, data in enumerate(letters):
                    if data > target:
                        return letters[i]
```

