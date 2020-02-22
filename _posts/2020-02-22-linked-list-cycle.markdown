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
To represent a cycle in the given linked list, we use an integer pos which
represents the position (0-indexed) in the linked list where tail connects to.
If pos is -1, then there is no cycle in the linked list.
 
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

# solution

```python
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        set1 = set()
        while head:
            if head not in set1:
                set1.add(head)
                head = head.next
            else:
                return True
        return False
```

||   ✔ Accepted
||   ✔ 17/17 cases passed (48 ms)
||   ✔ Your runtime beats 64.59 % of python3 submissions
||   ✔ Your memory usage beats 100 % of python3 submissions (16.4 MB)

# lmv

Except-ionally fast Python

https://leetcode.com/problems/linked-list-cycle/discuss/44494

* Lang:    python3
* Author:  StefanPochmann
* Votes:   257

Took 88 ms and the "Accepted Solutions Runtime Distribution" doesn't show any faster Python submissions. The "trick" is to not check all the time whether we have reached the end but to handle it via an exception. ["Easier to ask for forgiveness than permission."](https://docs.python.org/3/glossary.html#term-eafp)

The algorithm is of course [Tortoise and hare](https://en.wikipedia.org/wiki/Cycle_detection#Tortoise_and_hare).

```python
class Solution:
    def hasCycle(self, head):
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False
```

||   ✔ Accepted
||   ✔ 17/17 cases passed (40 ms)
||   ✔ Your runtime beats 95.74 % of python3 submissions
||   ✔ Your memory usage beats 100 % of python3 submissions (16.1 MB)
