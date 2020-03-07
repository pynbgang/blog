---
layout: post
title: "binary-watch"
published: true
created:  2020 Mar 07 11:47:32 AM
tags: [python, leetcode, easy]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[401] Binary Watch](https://leetcode.com/problems/binary-watch/description/)

    || * algorithms
    || * Easy (46.33%)
    || * Likes:    485
    || * Dislikes: 831
    || * Total Accepted:    76.2K
    || * Total Submissions: 164K
    || * Testcase Example:  '0'
    || * Source Code:       401.binary-watch.py
    || 
    || A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).
    || Each LED represents a zero or one, with the least significant bit on the right.
    || 
    || For example, the above binary watch reads "3:25".
    || 
    || Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.
    || 
    || Example:
    || Input: n = 1Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
    || 
    || 
    || Note:
    || 
    || The order of output does not matter.
    || The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
    || The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".

