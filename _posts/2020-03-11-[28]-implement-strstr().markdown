---
layout: post
title: "[28] Implement strStr()"
published: true
created:  2020 Mar 11 10:28:08 AM
tags: [python, leetcode, easy]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[28] Implement strStr()](https://leetcode.com/problems/implement-strstr/description/)

    || * algorithms
    || * Easy (33.63%)
    || * Likes:    1312
    || * Dislikes: 1710
    || * Total Accepted:    587.8K
    || * Total Submissions: 1.7M
    || * Testcase Example:  '"hello"\n"ll"'
    || * Source Code:       28.implement-strstr.py
    || 
    || Implement strStr().
    || 
    || Return the index of the first occurrence of needle in haystack, or -1 if
    needle is not part of haystack.
    || 
    || Example 1:
    || 
    || 
    || Input: haystack = "hello", needle = "ll"
    || Output: 2
    || 
    || 
    || Example 2:
    || 
    || 
    || Input: haystack = "aaaaa", needle = "bba"
    || Output: -1
    || 
    || 
    || Clarification:
    || 
    || What should we return when needle is an empty string? This is a great
    question to ask during an interview.
    || For the purpose of this problem, we will return 0 when needle is an
    empty string. This is consistent to C's strstr() and Java's indexOf().
