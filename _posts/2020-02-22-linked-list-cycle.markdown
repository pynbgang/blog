---
layout: post
title: "linked list cycle"
published: true
created:  2020 Feb 22 12:08:05 PM
tags: [linkedlist, python, easy, leetcode]
categories: [tech]
---
TABLE OF CONTENT
* auto-gen TOC:
{:toc}
- - -

# [[141] Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/description/)

* algorithms
* Easy (39.40%)
* Likes:    2287
* Dislikes: 346
* Total Accepted:    539.7K
* Total Submissions: 1.4M
* Testcase Example:  '[3,2,0,-4]\n1'

Given a linked list, determine if it has a cycle in it.
To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
 
Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.
Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.
Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 
Follow up:
Can you solve it using O(1) (i.e. constant) memory?

