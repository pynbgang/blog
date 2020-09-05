---
layout: post
title: "[84]-largest-rectangle-in-histogram"
published: true
created:  2020 Jan 31 10:29:15 AM
tags: [wangmazi, python, leetcode, lintcode, stack, hard]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[84] Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/description/)

    || * algorithms
    || * Hard (33.27%)
    || * Likes:    2767
    || * Dislikes: 66
    || * Total Accepted:    219.9K
    || * Total Submissions: 660.9K
    || * Testcase Example:  '[2,1,5,6,2,3]'
    || * Source Code:       84.largest-rectangle-in-histogram.py
    || 
    || Given n non-negative integers representing the histogram's bar height
    where the width of each bar is 1, find the area of largest rectangle in the
    histogram.
    || 
    || Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
    || 
    || The largest rectangle is shown in the shaded area, which has area = 10 unit.
    || 
    || Example:
    || 
    || Input: [2,1,5,6,2,3]
    || Output: 10

see also [largest-rectangle-in-histogram](http://www.lintcode.com/problem/largest-rectangle-in-histogram/description)

## ping: brute force

timeout

```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea=[]
        for i in range(len(heights)):
            area=height=heights[i]
            for j in range(i, len(heights)):
                width=j-i+1
                height=min(height, heights[j])
                area=max(area, width*height)
            maxarea.append(area)
        return max(maxarea or [0])
```

## wangmazi

```python
class Solution:
    def largestRectangleArea(self, heights):
        ids, area = [], 0
        for id, height in enumerate(heights + [0]):
            while ids and height < heights[ids[-1]]:
                popped_id = ids.pop()
                left_id = ids[-1] if ids else -1
                width = id - left_id - 1
                area = max(area, width * heights[popped_id])
            ids.append(id)
        return area
```

with comments:

```python
class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, heights):
        ids, area = [], 0

        #1. 增加末尾高度0，统一算法最后一步的操作
        #2. 依次取每个高度的编号和值
        for id, height in enumerate(heights + [0]):
            #如果ids堆栈未取空，且突然遇到一个变小的高度：
            while ids and height < heights[ids[-1]]:
                # 弹出距离当前高度最近的编号
                popped_id = ids.pop()
                # 计算它的“左边界“编号：
                # 如果堆栈里还有，那么就是那个下一个（距离当前编号更远的）编号
                # 否则，用-1.这样抵消掉下面的减一算法，使得数字0代表宽度1
                left_id = ids[-1] if ids else -1
                #如果列表为空，则宽度为id，否则为id-ids[-1]-1
                # 计算从弹出编号，向左能拉长到的最远（直到左边界）宽度
                width = id - left_id - 1
                area = max(area, width * heights[popped_id])
            #否则，如果是递增或等高，或者堆栈取空（比较完了），依次压入堆栈中
            ids.append(id)
        return area
```

## tips

https://chuansongme.com/n/390896436960

<!--
![image](https://user-images.githubusercontent.com/2038044/73324248-5b803a80-4218-11ea-9d9a-35fa33e2237c.png)
![image](https://user-images.githubusercontent.com/2038044/73324229-4c998800-4218-11ea-809b-84e37937ac1c.png)
![image](https://user-images.githubusercontent.com/2038044/73370602-79828500-4282-11ea-9eca-6df64d5a5aab.png)
-->

### running process

example: 213423

              4        
             +--+      
           3 |  |   3  
     2    +--+  |2 +--+
    +--+  |  |  +--+  |
    |  |1 |  |  |  |  |
    |  +--+  |  |  |  |
    +--------+--+--+--+
     0  1  2  3  4  5  

running process:

    first, push id0 => 0
    id1 is lower, pop stack:
        pop0, area: 2x1=2
        stack is empty
        push id1 => 0 1
    id2 is higher, push id2 (1,2)
    id3 is higher, push id3 (1,2,3)
    id4 is lower, pop those taller items in stack:
        pop3 and calc its max extended area:
            because its left neighbor 2 is lower, so 2 is its max-left boundary
            current id4 is lower, so id4 is its max-right boundary
                leftid=2
                width=4-2-1=1
                so id3 area: 3x1=3
                stack: 1, 2
        pop2 and calc its max extended area:
            because its left neighbor 1 is lower, so 1 is its max-left boundary
            current id4 is lower so id4 is its max-right boundary
                leftid=1
                width=4-1-1=2
                id2's max area=2x2=4
                stack 1,
        1 is not taller, so not pop it yet
        (otherwise can't find 1's right boundary - it can extend beyond 4)
        push id4 in stack: 1, 4
    id5 is higher, push id5 (1,4,5)
    id6 is what we've made up (height0):
        it will be the max-right boundary for all id in stack 
        pop all id in stack and calc its max extended area:
        pop5 and calc its max extended area: 
            left neighbor in stack is 4, so 4 is its max-left boundary
                leftid=4
                width=6-4-1=1
                id5 area: 3x1
                stack: 1, 4
        pop4 and calc its max extended area:
            left neighbor in stack is 1, so 1 is its max-left boundary
                leftid=1
                width=6-1-1=4
                id4 area: 4x2=8         #<---found it
        pop1 and calc its max extended area:
            no left neighbor in stack, so use -1
                leftid=-1
                width=6-(-1)-1=6
                id1 area: 1x6=6
        push id6
    done

### running process (detail)

example: 213423

              4        
             +--+      
           3 |  |   3  
     2    +--+  |2 +--+
    +--+  |  |  +--+  |
    |  |1 |  |  |  |  |
    |  +--+  |  |  |  |
    +--------+--+--+--+
     0  1  2  3  4  5  

* for id, height in enumerate(heights+[0]):

    * id, height = 0, 2
        * while ids(empty) and height2 `<` heights[ids[-1]]: skip
        * ids.append(id0). ids=[0]

    * id, height=1,1
        * while ids([0]) not empty and 
                current height1 `<` height(2) of last element in ids(0):
            * popped_id = 0
            * left_id = -1 :last id in ids(empty now) if ids not empty, else -1
            * width = id(1) - left_id(-1) - 1 = 1
            * current area = width * height2 of popped_id0 = 2
            * maxarea=max(previous maxarea0, current area2)=2
        * while ids(empty) and ...:
            * done
        * ids.append(1). ids=[1]

    * id, height=2,3
        * while ids [1] and current height3 `<` height(1) of last id1: skip
        * ids.append(2). ids=[1,2]

    * id, height=3,4
        * while ids [1,2] and current height4 `<` height(3) of last id2: skip
        * ids.append(3). ids=[1,2,3]

    * id, height=4,2
        * while ids [1,2,3] and current height2 `<` height(4) of last id3:
            * popped_id = 3
            * left_id = 2 :last id in ids(2) if ids not empty, else -1
            * width = id(4) - left_id(2) - 1 = 1
            * current area = width1 * height4 of popped_id3 = 4
            * maxarea=max(previous maxarea2, current area4) = 4
        * while ids [1,2] and current height2 `<` height(3) of last id2:
            * popped_id = 2
            * left_id = 1 :last id in ids(1) if ids not empty, else -1
            * width = id(4) - left_id(1) - 1 = 2
            * current area = width2 * height3 of popped_id2 = 6
            * maxarea=max(previous maxarea4, current area6) = 6
        * while ids [1] and current height2 `<` height(1) of last id1: skip
        * ids.append(4). ids=[1,4]

    * id, height=5,3
        * while ids [1,4] and current height3 `<` height(2) of last id4: skip
        * ids.append(5). ids=[1,4,5]

    * id, height=6,0
        * while ids [1,4,5] and current height0 `<` height(3) of last id5:
            * popped_id = 5
            * left_id = 4 :last id in ids(4) if ids not empty, else -1
            * width = id(6) - left_id(4) - 1 = 1
            * current area = width1 * height3 of popped_id2 = 3
            * maxarea=max(previous maxarea3, current area6) = 6
        * while ids [1,4] and current height0 `<` height(2) of last id4:
            * popped_id = 4
            * left_id = 1 :last id in ids(1) if ids not empty, else -1
            * width = id(6) - left_id(1) - 1 = 4
            * current area = width4 * height2 of popped_id4 = 6
            * maxarea=max(previous maxarea6, current area6) = 6
        * while ids [1] and current height0 `<` height(2) of last id1:
            * popped_id = 1
            * left_id = -1 :last id in ids(empty) if ids not empty, else -1
            * width = id(6) - left_id(-1) - 1 = 6
            * current area = width6 * height1 of popped_id1 = 6
            * maxarea=max(previous maxarea6, current area5) = 6
        * ids.append(6). ids=[6]

    * return maxarea6

### illustration

example: 213423

    I         4                II         4 
             +--+                        +--+
           3 |  |   3                  3 |  |   3
     2    +--+  |2 +--+          2    +--+  |2 +--+
    +--+  |  |  +--+  |         +--+  |  |  +--+  |
    |  |1 |  |  |  |  |  ==>    |  |1 |  |  |  |  |
    |  +--+  |  |  |  |         |  +--+  |  |  |  | 0  #<---append 0
    +--------+--+--+--+         +--------+--+--+--+--
     0  1  2  3  4  5            0  1  2  3  4  5  6
                                        ||
                                        vv
    IV        4                 III       4
             +--+                        +--+
           3 |  |   3                  3 |  |   3
     2    +--+  |2 +--+          2    +--+  |2 +--+
    +--+  |  |  +--+  |         +--+  |  |  +--+  |
    |  |1 |  |  |  |  |  <==    |  |1 |  |  |  |  |
    |  +--+  |  |  |  |0        |  +--+  |  |  |  | 0
    +--------+--+--+--+--       +--------+--+--+--+--
     0 (1  2  3) 4  5  6        (0) 1  2   3  4  5  6
                 ^              --- ^
                                2x1
            ||                  
            vv
     V        4                 VI        4
             +--+                        +--+
           3 |  |   3                  3 |  |   3
     2    +--+  |2 +--+          2    +--+  |2 +--+
    +--+  |  |  +--+  |         +--+  |  |  +--+  |
    |  |1 |  |  |  |  |  ==>    |  |1 |  |  |  |  |
    |  +--+  |  |  |  |0        |  +--+  |  |  |  | 0
    +--------+--+--+--+--       +--------+--+--+--+--
     0 (1  2) 3  4  5  6         0 (1) 2   3  4  5  6
             --- ^                     -----  ^
             4x1                       3x2
                                        ||
                                        vv
    VIII      4                  VII      4
             +--+                        +--+
           3 |  |   3                  3 |  |   3
     2    +--+  |2 +--+          2    +--+  |2 +--+
    +--+  |  |  +--+  |         +--+  |  |  +--+  |
    |  |1 |  |  |  |  |  <==    |  |1 |  |  |  |  |
    |  +--+  |  |  |  |0        |  +--+  |  |  |  | 0
    +--------+--+--+--+--       +--------+--+--+--+--
     0 (1) 2  3 (4) 5  6         0 (1) 2   3 (4  5) 6
                   --- ^                            ^
                   5x1
            ||                  
            vv
    IX        4                 X         4
             +--+                        +--+
           3 |  |   3                  3 |  |   3
     2    +--+  |2 +--+          2    +--+  |2 +--+
    +--+  |  |  +--+  |         +--+  |  |  +--+  |
    |  |1 |  |  |  |  |  ==>    |  |1 |  |  |  |  |
    |  +--+  |  |  |  |0        |  +--+  |  |  |  | 0
    +--------+--+--+--+--       +--------+--+--+--+--
     0 (1) 2  3  4  5  6         0  1  2   3  4  5  6
           --------    ^         -----------------  ^
            2x3                         1x6
                                        ||                  
                                        vv
    XII                         XI        4
                                         +--+
                                       3 |  |   3
                                 2    +--+  |2 +--+
         return max=6   <==     +--+  |  |  +--+  |
                                |  |1 |  |  |  |  |
                                |  +--+  |  |  |  | 0
                                +--------+--+--+--+--
                                 0  1  2   3  4  5 (6)

### how/why it works

1. brute force: "find all substrings" and compare
2. use some "rules"

looking at this figure:

    I         4                II         4 
             +--+                        +--+
           3 |  |   3                  3 |  |   3
     2    +--+  |2 +--+          2    +--+  |2 +--+
    +--+  |  |  +--+  |         +--+  |  |  +--+  |
    |  |1 |  |  |  |  |  ==>    |  |1 |  |  |  |  |
    |  +--+  |  |  |  |         |  +--+  |  |  |  | 0  #<---append 0
    +--------+--+--+--+         +--------+--+--+--+--
     0 (1  2  3) 4  5            0 (1) 2  3 (4  5) 6
       --------  |                                 ^
       IS: incremental sequence                    |
        ^        |                                 |
        |        |                                 |
        |        |FLI:First lower ID for IS 123    |FLI for IS 145
        |        |RB: right border for IS 123      |RB: right border for IS 145
        |LIS: last id in IS
        |LNIS: left neighboring ID in IS for 2

the rules:

* scan each id and check their height, try to search for some incremental
  sequences (IS)
* some IS must can be found. save in a list or stack e.g. [1, 2, 3]
* in any IS, say 1,2,3, for each individual id, there are some "rules" to
  compose the max rectangle it may span. the key is to find the left and right
  borders of the max rectangle.
  * the *"right border(RB)"* of the max area must be the first lower id(FLI)
    found during the process 4. because the FLI is "lower" by definition.
    * for 2, 3, which are "taller" then the FLI4, the RB rule is true.
      there is no chance any of them could extend further beyand FLI4.
      * now determine the *"left border(LB)"*. for each of 2,3 which are both
        taller than FLI4, their LB is simply their "left neighboring id in IS
        (LNIS)". e.g. id3, the LNIS2 is lower, making 3 not possible to
        extend left-ward further.
    * however, for 1, which is lower than FLI4, the RB rule does *NOT* apply.
      apparently it can extend right-ward further beyond FLI4. there is no way
      to know where it will stop at the moment, so we have to leave the RB
      determinition later.
      * But what about the 1's *LB*? 1 is already the last id in the sequence
        (LIS), so there is no LNIS to use. in this case the LB is actually 0,
        that is the very beginning of the whole list. because it must be the
        lowest ID we've ever seen *so far*, reasons are: 
          * LIS (last id in IS) was also FLI(first lower id for IS) for its
            previous IS, so LIS `<` anything in previous IS.
          * LIS is smallest in an IS, so LIS `<=` anything in current IS.
  * based above observation, we can conclude: in any IS, if we iterate from
    right to left, we can find the LB and RB of each id's corresponding max
    width:
    * LB: this can be determined anytime
        * if the id is not the LIS, it's LB is the LNIS
        * if the id is LIS, it's LB is beginning of the list (0)
    * RB: some can be determined, some can't
        * if the id is taller than FLI, then it's RB is the FLI
        * if the id is lower or same as FLI, it's RB can't be determined so far
    * use a stack to maintain IS, then pop those IDs for which we can determine
      the max width(and rectangle), leave those IDs for which we can't determine
      yet.

* repeat this process, found a new IS: 4, 5
* now, *merge* whatever left over in previous sequence(1) and get a new merged
  IS [1,4,5]
* in order to repeat this algorithm, we have to find a FLI for this new
  sequence, but we can't. so just making up one with height 0 (which is
  guaranteed to be lower than any existing one)
* now we can repeat the method inside of the IS.
  * for 5, RB is 6, LB is its LNIS 4
  * for 4, RB is 6, LB is its LNIS 1.
  * for 1, RB is 6, LB is 0 since 1 is LIS
* compare all the areas between LB to RB and get the max.

