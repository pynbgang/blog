#
# @lc app=leetcode id=468 lang=python3
#
# [468] Validate IP Address
#

# @lc code=start
class Solution:
    def validIPAddress(self, IP: str) -> str:
        # ipv4 is dot seperated groups
        if "." in IP:
            list4 = IP.split(".")
            
            # it has to contain exact 4 groups
            # and all of the following has to be true:
            # for each group:
            #    it has to be a digit that is not gt 255
            #    no leading zero, except for 0
            if len(list4) == 4 \
                and all([
                    s.isnumeric() and int(s) <= 255
                    and s[0] is not '0' if s != '0' else True
                    for s in list4
                ]):
                return "IPv4"
        # ipv6 is ':' seperated groups
        if ":" in IP and IP.count("::") < 1:
            list6 = IP.split(":")
            # ipv6 can has digit or a-f chars, so prepare a char set for ipv6
            hexnums = "0123456789abcdefABCDEF"
            
            # ipv6 has to has 8 groups (required by this test)
            # and all of the following has to be true:
            # for each group:
            #   it has to be no more than 4 chars
            #   char has to be in the allowed char set
            if len(list6) == 8 and \
                all([
                    len(s) <= 4
                    and all([c in hexnums for c in s])
                    for s in list6
                ]):
                return "IPv6"
        return "Neither"
        
    """
    def validIPAddress(self, IP):
        # Write your code here
        if IP.count(".") == 3 \
            and all([
                s.isnumeric()
                and int(s) <= 255
                and (len(s) == 1 or s[0] != "0")
                for s in IP.split(".")]):
            return "IPv4"
        hexnums = "0123456789abcdefABCDEF"
        if IP.count(":") == 7 \
            and all([
                all([c in hexnums for c in s])
                and len(s) and len(s) <= 4
                for s in IP.split(":")
            ]):
            return "IPv6"
        return "Neither"
    """
# @lc code=end
