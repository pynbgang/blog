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
        return "0" if str1 == str2 == '0' else ''.join(
            num2str[i] for i in l2)[::-1].lstrip('0')


class Solution:  #owen on field
    def addStrings(self, str1, str2):
        if not str1 and str2:
            return str2
        if not str2 and str1:
            return str1
        if len(str2) > len(str1):
            return self.addStrings(str2, str1)
        l1 = list(str1)
        l2 = ["0"] * (len(str1) - len(str2)) + list(str2)
        listcarry = [0] + [0] * len(str1)
        sumstr = ""
        for i in range(len(l1) - 1, -1, -1):
            temp = int(l1[i]) + int(l2[i]) + listcarry[i + 1]
            if temp < 10:
                sumstr += str(temp)
            else:
                sumstr += str(temp)[-1]
                listcarry[i] = 1
        if listcarry[0] == 1:
            return "1" + sumstr[::-1]
        return sumstr[::-1]


# @lc code=end
