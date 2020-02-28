---
layout: post
title: "reorder-data-in-log-files"
published: true
created:  2020 Feb 25 11:51:59 AM
tags: [easy, lintcode, list, string, python, sorted]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[937] Reorder Data in Log Files](https://leetcode.com/problems/reorder-data-in-log-files/description/)

    || * algorithms
    || * Easy (53.65%)
    || * Likes:    431
    || * Dislikes: 1339
    || * Total Accepted:    83.5K
    || * Total Submissions: 155.6K
    || * Testcase Example:  '["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]'
    || 
    || You have an array of logs.  Each log is a space delimited string of words.
    || 
    || For each log, the first word in each log is an alphanumeric identifier.  Then, either:
    || 
    || 	Each word after the identifier will consist only of lowercase letters, or;
    || 	Each word after the identifier will consist only of digits.
    || 
    || We will call these two varieties of logs letter-logs and digit-logs.  It is
    guaranteed that each log has at least one word after its identifier.
    || 
    || Reorder the logs so that all of the letter-logs come before any digit-log. 
    The letter-logs are ordered lexicographically ignoring identifier, with the
    identifier used in case of ties.  The digit-logs should be put in their
    original order.
    || 
    || Return the final order of the logs.
    || 
    || Example 1:
    || Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    || Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
    || 
    || Constraints:
    || 

    || 	0 <= logs.length <= 100
    || 	3 <= logs[i].length <= 100
    || 	logs[i] is guaranteed to have an identifier, and a word after the identifier.

"dig1 8 1 5 1",
"let1 art can",
"dig2 3 6",
"let2 own kit dig",
"let3 art zero"

## rules

* letter log first
* letter log sort ignoring id, then use id as tie
* digit log no sort

## solutions


```python
class Solution: # ping: make use of sorted 'key'
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        """
        "let1 0art can",
        "let3 0art zero"
        "let2 0own kit dig",
        "dig2 a3 6",
        "dig1 a8 1 5 1",
        """

        def helper(s):
            l = s.split()
            if l[1].isalpha():  l = ['0']+l[1:]+l[0:1]
            else:               l = ['a']
            return ' '.join(l)

        return sorted(logs, key=helper)

class Solution: # ping: compacted
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def helper(s):
            l = s.split()
            return ' '.join(['0']+l[1:]+l[0:1] if l[1].isalpha() else ['a'])

        return sorted(logs, key=helper)

    """
    ||   ✔ Accepted
    ||   ✔ 63/63 cases passed (24 ms)
    ||   ✔ Your runtime beats 99.38 % of python3 submissions
    ||   ✔ Your memory usage beats 100 % of python3 submissions (12.8 MB)
    """

class Solution: # ping: oneliner, without list
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        return sorted(logs, key=lambda s: '0'+s[s.index(' ')+1:]+' '+s[0:s.index(' ')] if s[s.index(' ')+1].isalpha() else 'a')

    """
    ||   ✔ Accepted
    ||   ✔ 63/63 cases passed (36 ms)
    ||   ✔ Your runtime beats 56.1 % of python3 submissions
    ||   ✔ Your memory usage beats 100 % of python3 submissions (12.7 MB)
    """

class Solution: # lmv
    """
    Reorder Data in Log Files

    Solution in Python 3 (beats ~100%) (five lines)

    https://leetcode.com/problems/reorder-data-in-log-files/discuss/382667

    * Lang:    python3
    * Author:  junaidmansuri
    * Votes:   5
    """

    def reorderLogFiles(self, G: List[str]) -> List[str]:
        A, B, G = [], [], [i.split() for i in G]
        for g in G:
            if g[1].isnumeric(): B.append(g)
            else: A.append(g)
        return [" ".join(i) for i in sorted(A, key = lambda x: x[1:]+[x[0]]) + B]

    """
    ||   ✔ Accepted
    ||   ✔ 63/63 cases passed (32 ms)
    ||   ✔ Your runtime beats 83.02 % of python3 submissions
    ||   ✔ Your memory usage beats 100 % of python3 submissions (12.8 MB)
    """
```


## tips

* python string manipulation:
  - very limited tools to change "in-place"
      * s.replace?
      * `+`: s=s[1:3]+s[2:5]+
  - split to list, convert to list operation
  - regex?

