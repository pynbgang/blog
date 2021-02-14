---
layout: post
title: "[38] Count and Say"
published: true
created:  2021 Feb 12 12:53:33
tags: [python, leetcode, easy, regex]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[38] Count and Say](https://leetcode.com/problems/count-and-say/description/)

just go to example to understand what it is about...

    || * algorithms
    || * Easy (45.57%)
    || * Likes:    268
    || * Dislikes: 1027
    || * Total Accepted:    477.9K
    || * Total Submissions: 1M
    || * Testcase Example:  '1'
    || * Source Code:       38.count-and-say.py
    ||
    || The count-and-say sequence is a sequence of digit strings defined by the
    recursive formula:
    ||
    || 	countAndSay(1) = "1"
    || 	countAndSay(n) is the way you would "say" the digit string from
    countAndSay(n-1), which is then converted into a different digit string.
    ||
    ||
    || To determine how you "say" a digit string, split it into the minimal
    number of groups so that each group is a contiguous section all of the same
    character. Then for each group, say the number of characters, then say the
    character. To convert the saying into a digit string, replace the counts
    with a number and concatenate every saying.
    ||
    || For example, the saying and conversion for digit string "3322251":
    ||
    || Given a positive integer n, return the n^th term of the count-and-say
    sequence.
    ||
    ||  
    || Example 1:
    ||
    || Input: n = 1
    || Output: "1"
    || Explanation: This is the base case.
    ||
    || Example 2:
    ||
    || Input: n = 4
    || Output: "1211"
    || Explanation:
    || countAndSay(1) = "1"
    || countAndSay(2) = say "1" = one 1 = "11"
    || countAndSay(3) = say "11" = two 1's = "21"
    || countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
    ||
    || Constraints:
    ||
    || 	1 <= n <= 30

# solution

    || https://leetcode.com/problems/count-and-say/discuss/15999
    ||
    || * Lang:    python3
    || * Author:  StefanPochmann
    || * Votes:   178
    ||
    || **Solution 1** ... using a regular expression
    ||
    ||     def countAndSay(self, n):
    ||         s = '1'
    ||         for _ in range(n - 1):
    ||             s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
    ||         return s
    ||
    || ---
    ||
    || **Solution 2** ... using a regular expression
    ||
    ||     def countAndSay(self, n):
    ||         s = '1'
    ||         for _ in range(n - 1):
    ||             s = ''.join(str(len(group)) + digit
    ||                         for group, digit in re.findall(r'((.)\2*)', s))
    ||         return s
    ||
    || ---
    ||
    || **Solution 3** ... using `groupby`
    ||
    ||     def countAndSay(self, n):
    ||         s = '1'
    ||         for _ in range(n - 1):
    ||             s = ''.join(str(len(list(group))) + digit
    ||                         for digit, group in itertools.groupby(s))
    ||         return s


```python
class Solution:     #lmv
    def countAndSay(self, n):
        s = '1'
        for _ in range(n - 1):
            s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
            #          ---------   -------------------------------------------
            #           regex           repl
        return s
```

# tips

1. regarding `r'(.)\1*'`
   match repeating chars

        In [49]: match1 = re.match(r'(.)*', "1112")
        In [50]: match1
        Out[50]: <re.Match object; span=(0, 4), match='1112'>

        In [50]: re.match(r'(.)\1*', "1112")
        Out[50]: <re.Match object; span=(0, 3), match='111'>

2. regarding `re.sub(a, b, s)`
   from s, use regex a to match, then use new string b to replace whatever
   matched

        # Replace pattern abc -> def
        result = re.sub('abc',  'def', input)           

3. regarding `re.sub(a, func, s)`
    when b (new string) is not a static string, but instead a function. then:

    >If repl is a function, it is called for **every non-overlapping occurrence** of
    >pattern. The function takes a single match object argument, and returns the
    >replacement string. For example:

        def dashrepl(matchobj):
            print(matchobj)
            if matchobj.group(0) == '-': 
                return ' '
            else: 
                return '-'

        In [94]: re.sub('-{1,2}', dashrepl, 'pro----gram-files')                        
        <re.Match object; span=(3, 5), match='--'>
        <re.Match object; span=(5, 7), match='--'>
        <re.Match object; span=(11, 12), match='-'>
        Out[94]: 'pro--gram files'

    regex is `-{1,2}`, string is  `pro----gram-files`, 
    there are totally 3 matches `--` `--` and `-`, each passed as a
    match type of object `matchobj`, the matched string is saved as `.group(0)`
    of each match objects.

    This is like an internal "hidden loop".
    when matched string is '-', replace it with a space
    else (when matched string is '--'), replace with a '-'.
    hence the final new string changed from:

        `pro----gram-files`
            ^^^^    ^
            - -    blank

    to

        `pro--gram files`

back to this 3 lines lmv solution:

        s = '1'
        for _ in range(n - 1):
            s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)

the core is this one line:

    s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)

for example let's say s is `1211`: the expected output is `111221`

* regex a is `r'(.)\1*'`, matches any repetitive chars, like in this example `1` or `2`, or `11`
* func is `lambda m: str(len(m.group(0))) + m.group(1)`. 
  * input is `m` - a match object.
  * output is `str(len(m.group(0))) + m.group(1)`, which are two parts:
    * a: string form of `m.group(0)` 's length. `m.group(0)` is the whole matched
      part of the string. for our regex, the matched part will be `1` or `2`,
      or `11`. the string form of their lengths are `1`, `1`, `2` respectively.
    * b: `m.group(1)`, which is the "1st" string captured by `()`, in
      this case the single char. so it's `1`, `2`, `1`, respectively.
    * a+b will be connecting `11` `12` and `11`, that is `111211`. this is
      because the func will be called for each every match.
* repeat `n-1` times. because the init `s='1'` count once.
