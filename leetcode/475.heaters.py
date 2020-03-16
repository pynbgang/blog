#
# @lc app=leetcode id=475 lang=python3
#
# [475] Heaters
#

# @lc code=start
def findRadius(houses, heaters):    #lmv
    """
    Python short and easy - explained - One pointer - O(NlogN), O(1)

    https://leetcode.com/problems/heaters/discuss/274555

    * Lang:    python3
    * Author:  axelramar9
    * Votes:   7

    **Algorithm**
    After sorting the inputs, we loop through the houses and find the minimum
    distance to the left and right closests heaters.
    We mantain a pointer to lookup at the closests heaters, while looping through
    the houses:
    * `i` represents the index of the closest left heater
    * `i+1` represents the index of the closest left heater

    **Analysis**
    There is no extra space used.
    Given the two sort methods used, the runtime complexity is min(NlogN, MlogM)
    where N and M are the sizes of the two inputs.
    If the array were initially sorted, this algorithm would have linear runtime.
    """

    houses.sort()
    heaters.sort()
    n, i, maxRadius = len(heaters), 0, 0

    for house in houses:
        while i+1 < n and heaters[i+1] < house:
            i += 1
        maxRadius = max(maxRadius, min([abs(h-house) for h in heaters[i:i+2]]))

    return maxRadius

from typing import List
class Solution:     #ping: brute force: time limit exceeded
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        res = 0
        for house in houses:
            min_radius = 10 ** 9
            for heaters in heaters:
                min_radius = min(min_radius, abs(house - heater))
                if min_radius is 0:
                    break
            res = max(min_radius, res)
        return res

class Solution:     #jj: same, one liner
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        return max(min(abs(heater - house) for heater in heaters) for house in houses)

class Solution:     #jj: pass
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses, heaters = sorted(houses), sorted(heaters)   #sorted both
        stk, res = [heater.pop(0)], 0       #use a stack, pop 1st heater into it
        for h in houses:                    #loop each house
            while h > stk[-1] and heaters:  #find the closest heaters
                stk.append(heaters.pop(0))
            stk = stk[-2:] if len(stk) > 2 else stk
            res = max(res, min(abs(s - h) for s in stk))
        return res

        """
        ||   ✔ Accepted
        ||   ✔ 30/30 cases passed (412 ms)
        ||   ✔ Your runtime beats 29.13 % of python3 submissions
        ||   ✔ Your memory usage beats 8.33 % of python3 submissions (16.4 MB)
        """

class Solution:     #wangmazi
    """
    先对于加热器数组排序。
    对于每个房屋i，在加热器数组里使用二分查找找到距离房屋i最近的加热器的位置，
    最后的答案为所有房屋答案的最大值。
    """
    def findRadius(self, houses, heaters):
        # Write your code here
        heaters.sort()
        ans = 0
        for house in houses:
            ans=max(ans,self.closestHeater(house,heaters))
        return ans

    def closestHeater(self,house,heaters):
        start = 0
        end = len(heaters) - 1
        while start + 1 < end:
            m = start + (end - start) // 2
            if heaters[m] == house:
                return 0
            elif heaters[m] < house:
                start = m
            else:
                end = m
        return min(abs(house - heaters[start]), abs(heaters[end] - house))

S = Solution()
houses = [1, 2, 3, 4]
heaters = [1, 4]
S.findRadius(houses, heaters)
#1， 20, (H500)， 4444， （H8888），20000

# @lc code=end
