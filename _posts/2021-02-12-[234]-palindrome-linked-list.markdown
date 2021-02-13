---
layout: post
title: "[234] Palindrome Linked List"
published: true
created:  2021 Feb 12 11:15:35
tags: [python, leetcode, easy, linkedlist]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[234] Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/description/)

    || * algorithms
    || * Easy (40.01%)
    || * Likes:    4625
    || * Dislikes: 423
    || * Total Accepted:    555.4K
    || * Total Submissions: 1.4M
    || * Testcase Example:  '[1,2]'
    || * Source Code:       234.palindrome-linked-list.py
    || 
    || Given a singly linked list, determine if it is a palindrome.
    || 
    || Example 1:
    || 
    || 
    || Input: 1->2
    || Output: false
    || 
    || Example 2:
    || 
    || 
    || Input: 1->2->2->1
    || Output: true
    || 
    || Follow up:
    || Could you do it in O(n) time and O(1) space?

# solution: lmv

    || Palindrome Linked List
    || 
    || 11 lines, 12 with restore, O(n) time, O(1) space
    || 
    || https://leetcode.com/problems/palindrome-linked-list/discuss/64500
    || 
    || * Lang:    python3
    || * Author:  StefanPochmann
    || * Votes:   423
    || 
    || O(n) time, O(1) space. The second solution restores the list after changing it.
    || 
    || ---
    || 
    || **Solution 1: *Reversed first half == Second half?***
    || 
    || Phase 1: Reverse the first half while finding the middle.  
    || Phase 2: Compare the reversed first half with the second half.
    || 
    ||     def isPalindrome(self, head):
    ||         rev = None
    ||         slow = fast = head
    ||         while fast and fast.next:
    ||             fast = fast.next.next
    ||             rev, rev.next, slow = slow, rev, slow.next
    ||         if fast:
    ||             slow = slow.next
    ||         while rev and rev.val == slow.val:
    ||             slow = slow.next
    ||             rev = rev.next
    ||         return not rev
    || 
    || ---
    || 
    || **Solution 2: *Play Nice***
    || 
    || Same as the above, but while comparing the two halves, restore the list to its original state by reversing the first half back. Not that the OJ or anyone else cares.
    || 
    ||     def isPalindrome(self, head):
    ||         rev = None
    ||         fast = head
    ||         while fast and fast.next:
    ||             fast = fast.next.next
    ||             rev, rev.next, head = head, rev, head.next
    ||         tail = head.next if fast else head
    ||         isPali = True
    ||         while rev:
    ||             isPali = isPali and rev.val == tail.val
    ||             head, head.next, rev = rev, head, rev.next
    ||             tail = tail.next
    ||         return isPali
    || [Finished in 5 seconds]


# tips

* one line `a, b = c, d` is the key. different than a=c; b=d

```python
def isPalindrome(self, head):
    rev, slow, fast = None, head, head
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next      #<---
    if fast:
        slow = slow.next
    while rev and rev.val == slow.val:
        slow = slow.next
        rev = rev.next
    return not rev

"""
   None     head    ->  node1  ->  node2   ->   node3   ->  node4   ->  None

phaseI: create a reverse linke list for 1st half

   rev      fast/slow
                                   fast
     <----- rev         slow

                                                             fast

              <-------- rev        slow

                                                 slow
phaseII: compare 1st half(reversed linked list) and 2nd half(original linked l)

                          ^------------------------^
              rev                                            slow

   rev                                                                  rev

"""

```

