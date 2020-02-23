#
# @lc app=leetcode id=599 lang=python3
#
# [599] Minimum Index Sum of Two Lists
#

# @lc code=start

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list1=["Shogun","Tapioca Express","Burger King","KFC"]
        list2=["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
        for res1 in list1:
            if res1 in list2:
                sum1=list1.index(res1)+list2.index(res1)
                break
        for res2 in list2:
            if res2 in list1:
                sum2=list1.index(res2)+list2.index(res2)
                break
        print(res1 if sum1<=sum2 else res2)

S=Solution()
res=S.findRestaurant(list1, list2)
print(res)
# @lc code=end
