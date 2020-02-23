#
# @lc app=leetcode id=599 lang=python3
#
# [599] Minimum Index Sum of Two Lists
#

# @lc code=start

if 0:  #ping: failed
    class Solution:
        def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
            #list1=["Shogun","Tapioca Express","Burger King","KFC"]
            #list2=["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
            res=[]
            for res1 in list1:
                if res1 in list2:
                    sum1=list1.index(res1)+list2.index(res1)
                    break
            for res2 in list2:
                if res2 in list1:
                    sum2=list1.index(res2)+list2.index(res2)
                    break
            if sum1<=sum2:
                res.append(res1)
            if sum2<=sum1 and res1 != res2:
                res.append(res2)
            return res
if 1:  #ping
    class Solution:
        def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
            common, d = set(list1) & set(list2), {}
            for one in common:
                d[one]= list1.index(one) + list2.index(one)
            return [k for k in d if d[k] == min(d.values())]

if 0:  #lmv
    class Solution:
        def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
            d = {x: list1.index(x) + list2.index(x) for x in set(list1) & set(list2)}
            return [x for x in d if d[x] == min(d.values())]

"""
S=Solution()
res=S.findRestaurant(list1, list2)
print(res)
"""
# @lc code=end
