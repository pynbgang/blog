#
# @lc app=leetcode id=468 lang=python3
#
# [468] Validate IP Address
#

# @lc code=start
class Solution:
    def validIPAddress(self, IP: str) -> str:
        if (IP.count(".") == 3 and          #v4 must be 3 parts seperated by .
            all(                                 #and each part has to be:
                s.isnumeric() and int(s) <= 255  #number, < 255,
                and (len(s) == 1 or s[0] != "0") #first digit can't be "0"
                for s in IP.split(".")           #unless it is just 0.
               )
           ): return "IPv4"
        if (IP.count(":") == 7 and          #v6 must be 7 parts seprated by :
            all(                                #and each part has to be:
                all(c in "0123456789abcdefABCDEF" for c in s) #from this chars
                and 0 < len(s) <= 4             #less or equal to 4 digits
                for s in IP.split(":")          #but not null (1111::1111)
               )
            ): return "IPv6"
        return "Neither"

class Solution:     #(Sun Feb 14 00:01:58 2021)
    def validIPAddress(self, IP: str) -> str:
        if (IP.count('.') == 3 and
            all(
                s.isnumeric() and
                0<= int(s) <= 255 and
                (s[0] !='0' if len(s) > 1 else True)
                for s in IP.split('.')
            )
           ): return "IPv4"
        if (IP.count(':') == 7 and
            all(1 <= len(s) <= 4 and
                all(
                    c in '0123456789abcdefABCDEF'
                    for c in s
                )
                for s in IP.split(':')
            )
           ): return "IPv6"
        return "Neither"

S=Solution()
IP="1.0.1."
IP="2001:db8:85a3|| :8a2E:0370:7334"
S.validIPAddress(IP)

# @lc code=end
