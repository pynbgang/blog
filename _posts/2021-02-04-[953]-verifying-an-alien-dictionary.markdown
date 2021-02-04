---
layout: post
title: "[953] Verifying an Alien Dictionary"
published: true
created:  2021 Feb 04 11:07:36
tags: [python, leetcode]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[953] Verifying an Alien Dictionary](https://leetcode.com/problems/verifying-an-alien-dictionary/description/)

    || * algorithms
    || * Easy (52.77%)
    || * Likes:    1340
    || * Dislikes: 562
    || * Total Accepted:    186.5K
    || * Total Submissions: 356K
    || * Testcase Example:  '["hello","leetcode"]\n"hlabcdefgijkmnopqrstuvwxyz"'
    || 
    || In an alien language, surprisingly they also use english lowercase
    letters, but possibly in a different order. The order of the alphabet is
    some permutation of lowercase letters.
    || 
    || Given a sequence of words written in the alien language, and the order
    of the alphabet, return true if and only if the given words are sorted
    lexicographicaly in this alien language.
    ||  
    || Example 1:
    || 
    || Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
    || Output: true
    || Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
    || 
    || Example 2:
    || 
    || Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
    || Output: false
    || Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
    || 
    || Example 3:
    || 
    || Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
    || Output: false
    || Explanation: The first three characters "app" match, and the second
    string is shorter (in size.) According to lexicographical rules "apple" >
    "app", because 'l' > '∅', where '∅' is defined as the blank character which
    is less than any other character (More info).
    ||  
    || Constraints:
    || 
    || 
    || 	1 <= words.length <= 100
    || 	1 <= words[i].length <= 20
    || 	order.length == 26
    || 	All characters in words[i] and order are English lowercase letters.

# solution

```python
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        return sorted(words, key=lambda x: "".join(chr(97+order.index(c)) for c in x)) == words
```

# tips

https://leetcode.com/problems/verifying-an-alien-dictionary/discuss/1049961/one-line-solution-with-sort

* use sort with `key`. 
* the idea is, to convert each letter in original string, to a new letter,
  based on the given "order". 
* for example, in "word", 'w' is the 1st letter in the new "order", so it is in
  the same position like 'a' in original english. same for other letters.
  using this type of one to one mapping, we can convert "word" to 'ykus', and
  sort based on that. if sorting this way does not change anything, that means
  the orignal sequence was sorted already.
* english letters starts from 'a', and ord('a') is 97. any letters after 'a'
  has an offset from 97. 
* same thing applies the new language. first letter is 'w', following letters has their offset from 'w'.
* so if we map 'w' to 'a', any letters can be translated to original english
  letter using it's current offset.

        || Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"

        In [17]: "".join(chr(97+order.index(c)) for c in "word")              
        Out[17]: 'ykus'

