#
# @lc app=leetcode id=670 lang=python3
#
# [670] Maximum Swap
#

# @lc code=start
if 0:
    class Solution:
        def maximumSwap(self, num: int) -> int:
            #print("get num: ", num)
            str1 = str(num)
            list1=list(str1)
            len1 = len(list1)
            for i in range(len1-1):
                maxj = max(s for s in list1[i+1:])
                slipped = False
                for j in range(i+1, len1):
                    if list1[j] == maxj:
                        while j<len1 and list1[j] == maxj:
                            j += 1
                            slipped = True
                        if slipped:
                            j -= 1
                            break
                #print("found the swap j: ", j)
                if  list1[i] < list1[j] and i is not j:
                    list1[i], list1[j] = list1[j], list1[i]
                    break
            return int(''.join(list1))

if 0:
    class Solution:
        def maximumSwap(self, num: int) -> int:
            #print("get num: ", num)
            str1 = str(num)
            list1=list(str1)
            len1 = len(list1)
            for i in range(len1-1):
                maxj = max(s for s in list1[i+1:])
                slipped = False
                for j in range(len1-1, i, -1):
                    if list1[j] == maxj:
                        break
                #print("found the swap j: ", j)
                if  list1[i] < list1[j] and i is not j:
                    list1[i], list1[j] = list1[j], list1[i]
                    break
            return int(''.join(list1))

if 1:
    class Solution:
        def maximumSwap(self, num: int) -> int:
            if num < 11:
                return num
            if num > 10 ** 8:
                return 0

            original_num = list(str(num))
            new_num = original_num[:]

            for i in range(len(original_num)):
                for j in range(i + 1, len(original_num)):
                    # Swap
                    original_num[i], original_num[j] = original_num[j], original_num[i]
                    if new_num < original_num:
                        new_num = original_num[:]
                    # Swap back
                    original_num[i], original_num[j] = original_num[j], original_num[i]

            return int("".join(new_num))

S=Solution()
num=2736
S.maximumSwap(num)
num=9973
S.maximumSwap(num)
num=1993
S.maximumSwap(num)
num=10909091
S.maximumSwap(num)

# @lc code=end
