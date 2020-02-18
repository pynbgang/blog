---
layout: post
title: "Implement Power Function"
published: true
created:  2020 Feb 17 11:04:01 PM
tags: [python, binary, Google, Lin kedin]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

## Implement Power Function
find (xn % d)

Note that remainders on division cannot be negative.
In other words, make sure the answer you return is non negative.

### (https://www.interviewbit.com/problems/implement-power-function/)

   
### ideas


1. Mn=Mn/2*Mn/2



```python
class Solution:

    def pow(self, x, n, d):
        if n==0:
            return 1%d
        if n==1:return x%d
        elif n%2==0:return (pow(x, n/2, d)*pow(x, n/2, d))%d
        else :return (pow(x, n/2, d)*pow(x, n/2, d)*pow(x,1,d))%d

```

