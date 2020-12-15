#
# @lc app=leetcode id=56 lang=python
#
# [56] Merge Intervals
#

# @lc code=start


class Solution(object):     #ping
    # [[1,3],[2,6],[8,10],[15,18]]
    def merge(self, intervals):
        #:type intervals: List[List[int]]
        #:rtype: List[List[int]]
        res = []

        # corner cases: none or 1 internval only
        if not intervals:
            return res
        if len(intervals) == 1:
            return intervals

        # if there are at least 2 intervals, use first as "previous"
        int_p = intervals[0]
        # then get one from the rest as "current", and then compare
        for int_c in intervals[1:]:
            # find the the max/min of all 4 elements
            max1, min1 = max(int_p+int_c), min(int_p+int_c)

            if [min1, max1] == int_p:
                res.append(int_p)
            elif [min1, max1] == int_c:
                res.append(int_c)
            elif min1 in int_c and max1 in int_p:
                int_c, int_p = int_p, int_c
            else:
                if int_c[0] <= int_p[1]:
                    res.append([int_p[0], int_c[1]])
                else:
                    res.append(int_p)
                    int_p = int_c

        res.append(int_p)
        return res

class Solution(object):     #wangmazi
    def merge(self, intervals):
        # @param intervals, a list of Interval
        # @return a list of Interval
        result = []
        for interval in sorted(intervals, key=lambda x: x[0]):
            if len(result) == 0 or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
        return result

class Solution(object):     #revisit:  (Thu 10 Sep 2020 07:32:14 PM DST)
    def merge(self, intervals):
        if len(intervals) <= 1:
            return intervals
        i, res = 1, []
        intervals.sort(key=lambda x: x[0])
        while i < len(intervals):
            start, stop = intervals[i-1][0], intervals[i-1][1]
            while i < len(intervals) and intervals[i-1][1] >= intervals[i][0]:
                stop = max(intervals[i-1][1], intervals[i][1])
                i += 1
            res.append([start, stop])
            if i == len(intervals)-1 and intervals[i-1][1] < intervals[i][0]:
                res.append(intervals[-1])
            i += 1
        return res
"""
[[1,3],[2,6],[8,10],[15,18]]
    s
          s
                 s

"""


# @lc code=end
