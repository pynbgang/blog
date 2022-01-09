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

class Solution:     #lmv
    def addStrings(self, num1, num2):
        #num1="3451"; num2="823"
        #z=[('1', '3'), ('5', '2'), ('4', '8'), ('3', '0')]
        z = itertools.zip_longest(num1[::-1], num2[::-1], fillvalue='0')
        res, carry, zero2 = [], 0, 2*ord('0')
        for i in z:
            #cur_sum = ord(i[0]) - ord('0') + ord(i[1]) - ord('0') + carry
            cur_sum = ord(i[0]) + ord(i[1]) - zero2 + carry
            res.append(str(cur_sum % 10))
            carry = cur_sum // 10
        return ('1' if carry else '') + ''.join(res[::-1])

class Solution:     #lmv
    def addStrings(self, num1, num2):
        return str(
            reduce(lambda a, b: 10*a + b,
                map(lambda x: ord(x[0])+ord(x[1])-2*ord('0'),
                    list(itertools.zip_longest(num1[::-1], num2[::-1], fillvalue='0'))[::-1]
                )
            )
        )


class Solution:  #ping: pratice (Wed 26 Aug 2020 10:43:33 PM DST)
    def addStrings(self, str1: str, str2: str) -> str:
        #' 23': [0, 2, 3]
        #'678': [6, 7, 8]
        list1, list2, len1, len2  = list(str1), list(str2), len(str1), len(str2)
        if len1 > len2:     #string2list, then make sure first one is no longer
            list1, list2 = list2, list1
            len1, len2 = len2, len1
        list1 = ['0'] * (len2 - len1) + list1   #padding '0' in prefix
        for i in range(len2-1, 0, -1):  #calc from low power(higher index)
            sum1 = int(list1[i]) + int(list2[i]) #keep reminder and move carry
            list1[i], list1[i-1] = str(sum1 % 10), str(int(list1[i-1]) + sum1 // 10)
        list1[0] = str(int(list1[0]) + int(list2[0])) #the last digit
        return "0" if str1==str2=='0' else "".join(list1).lstrip('0')

# @lc code=end
