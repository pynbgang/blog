#
# @lc app=leetcode id=1010 lang=python3
#
# [1010] Pairs of Songs With Total Durations Divisible by 60
#

# @lc code=start
class Solution:             #web
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        l, res = [0] * 60, 0
        for t in time:
            l[t % 60] += 1
        for i in range(1, 30):
            res += (l[i] * l[60 - i])
        res += l[0] * (l[0] - 1) / 2
        res += l[30] * (l[30] - 1) / 2
        return int(res)

class Solution(object):     #owen
    def numPairsDivisibleBy60(self, time):
        d, count ={}, 0
        for i in time:                      #use a dict to count and save
            d[i%60]=d.get(i%60,0)+1         #mod of each num
        if 0 in d:count+=d[0]*(d[0]-1)/2    #special case mod being 0 or 30:
        if 30 in d:count+=d[30]*(d[30]-1)/2 #from n 0 take 2, total:nx(n-1)/2
        for i in range(1,30):               #from n x m take 1 each, total:nxm
            if i in d and 60-i in d: count += d[i] * d[60-i]
        return int(count)


class Solution(object):     #owen
    def numPairsDivisibleBy60(self, time):
        d, count ={}, 0
        for i in time:
            d[i%60]=d.get(i%60,0)+1
        count += d.get(0,0) * (d.get(0,0) - 1) / 2
        count += d.get(30,0) * (d.get(30,0) - 1) / 2
        count += sum(d[i] * d[60-i] for i in range(1,30) if i in d and 60-i in d)
        return int(count)

class Solution(object):     #ping, 2 pointer, not done
    def numPairsDivisibleBy60(self, time):
        #time = [30,20,150,100,40]
        count, i, j, time = 0, 0, len(time), sorted(i % 60 for i in time)
        dup_030 = dup_smaller = dup_bigger = 1
        while i <= j:
            while i<=j and time[i] == time[i+1] and time[i] in [0, 30]:
                dup_030 += 1
                i += 1
            count += dup_030 * (dup_030-1)/2

            sum1 = time[i] + time[j]
            while i<=j and 0 < time[i] == time[i+1] < 30:
                dup_smaller += 1
                i += 1
            while i<=j and 0 < time[j] == time[j-1] == (60 - time[i]) > 30:
                dup_bigger += 1
                j -= 1
            if not (sum1 % 60):
                count += dup_smaller * dup_bigger

            elif sum1 > 60: j -= 1
            else: i += 1
        return count




# @lc code=end
