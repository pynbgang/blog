---
layout: post
title: "lower case to upper case"
published: true
created:  2020 Feb 07 01:57:42 PM
tags: [python, naive, ord, chr]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# lowercase-to-uppercase

https://www.lintcode.com/problem/lowercase-to-uppercase/description

```python
class Solution:
    """
    @param character: a character
    @return: a character
    """
    def lowercaseToUppercase(self, character):
        # write your code here
        # return character.upper()
        return chr(ord(character) + ord('A') - ord('a'))
```
