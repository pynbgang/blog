#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#


# @lc code=start
class Solution:  #ping
    def addStrings(self, str1: str, str2: str) -> str:
        str2num, num2str = dict((zip('0123456789', range(10)))), dict((zip(range(10), '0123456789')))
        l1, l2 = list(str1)[::-1], list(str2)[::-1]
        if len(l1) >= len(l2): l1, l2 = l2, l1
        for i in range(len(l2)):
            l2[i] = str2num[l1[i]] + str2num[l2[i]] if i < len(l1) else str2num[l2[i]]
        l2.append(0)
        for i in range(len(l2) - 1):
            l2[i], l2[i + 1] = l2[i] % 10, l2[i + 1] + l2[i] // 10
        return "0" if str1 == str2 == '0' else ''.join(num2str[i] for i in l2)[::-1].lstrip('0')


class Solution:  #owen on field
    def addStrings(self, str1, str2):
        if not str1 or not str2:                #special cases: one str is null
            return str2 if not str1 else str2
        if len(str2) > len(str1):               #make sure str1 is longer
            return self.addStrings(str2, str1)  #str to list, & prepare a n+1
        l1, carry = list(str1), [0]*(len(str1)+1)     #list to save carry
        l2 = ["0"] * (len(str1) - len(str2)) + list(str2) #make l2 same length
        sumstr = ""                             #init result string
        for i in range(len(l1) - 1, -1, -1):    #calculate reversely (from ones)
            temp = int(l1[i]) + int(l2[i]) + carry[i + 1]
            if temp < 10:
                sumstr += str(temp)
            else:
                sumstr += str(temp)[-1]
                carry[i] = 1
        return "1" + sumstr[::-1] if carry[0] else sumstr[::-1]

#                i     |len(l1)-1
#                v     v
#l1:      [1, 2, 3, 4, 5]
#l2:      [0, 0, 6, 7, 8]
#carry:[0, 0, 0, 0, 0, 0]
#                ^     ^
#                i+1   |len(l1)

# @lc code=end
