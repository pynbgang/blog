---
layout: post
title: "[468] Validate IP Address"
published: true
created:  2020 Jan 02 03:30:01 PM
tags: [leetcode, python, lintcode, networking, all, split, count, wangmazi, medium]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -


# [[468] Validate IP Address](https://leetcode.com/problems/validate-ip-address/description/)

[validate-ip-address](https://www.lintcode.com/problem/validate-ip-address/description)

    || [468] Validate IP Address
    ||
    || https://leetcode.com/problems/validate-ip-address/description/
    ||
    || * algorithms
    || * Medium (24.64%)
    || * Likes:    443
    || * Dislikes: 1934
    || * Total Accepted:    94K
    || * Total Submissions: 377.5K
    || * Testcase Example:  '"172.16.254.1"'
    ||
    || Given a string IP, return "IPv4" if IP is a valid IPv4 address, "IPv6"
    if IP is a valid IPv6 address or "Neither" if IP is not a correct IP of any
    type.
    || A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <=
    255 and xi cannot contain leading zeros. For example, "192.168.1.1"
    and "192.168.1.0" are valid IPv4 addresses but "192.168.01.1", while
    "192.168.1.00" and "192.168@1.1" are invalid IPv4 addresses.
    || A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:
    ||
    || 	1 <= xi.length <= 4
    || 	xi is a hexadecimal string which may contain digits, lower-case English letter ('a' to 'f') and upper-case English letters ('A' to 'F').
    || 	Leading zeros are allowed in xi.

    For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and
    "2001:db8:85a3:0:0:8A2E:0370:7334" are valid IPv6 addresses, while
    "2001:0db8:85a3::8A2E:037j:7334" and
    "02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses.
    ||
    ||  
    || Example 1:
    ||
    ||
    || Input: IP = "172.16.254.1"
    || Output: "IPv4"
    || Explanation: This is a valid IPv4 address, return "IPv4".
    ||
    ||
    || Example 2:
    ||
    ||
    Input: IP = "2001:0db8:85a3|| 8A2E:0370:7334"
    || Output: "IPv6"
    || Explanation: This is a valid IPv6 address, return "IPv6".
    ||
    ||
    || Example 3:
    ||
    ||
    || Input: IP = "256.256.256.256"
    || Output: "Neither"
    || Explanation: This is neither a IPv4 address nor a IPv6 address.
    ||
    ||
    || Example 4:
    ||
    ||
    Input: IP = "2001:0db8:85a3|| 8A2E:0370:7334:"
    || Output: "Neither"
    ||
    ||
    || Example 5:
    ||
    ||
    || Input: IP = "1e1.4.5.6"
    || Output: "Neither"
    ||
    ||
    ||  
    || Constraints:
    ||
    ||
    || 	IP consists only of English letters, digits and the characters '.' and ':'.

## notes 问题归纳

v4:

* 4 groups, separated by ".", e.g.,172.16.254.1
* each part is a decimal num,
* each number ranges from 0-255,
* each number has no leading zero. For example, 172.16.254.01 is invalid.

v6:

* 8 groups separated by ":".
* each group is 4 hexadecimal digits, representing 16 bits.
    * e.g.: 2001:0db8:85a3:0000:0000:8a2e:0370:7334.
    * don't use :: , e.g.: 2001:0db8:85a3::8A2E:0370:7334 is invalid
* (optionally) omit some leading zeros among four hexadecimal digits
* some low-case characters in the address to upper-case ones: e.g:
  * 2001:db8:85a3:0:0:8A2E:0370:7334 is valid
* "extra" leading zeros is invalid. e.g. 02001:0db8:85a3:0000:0000:8a2e:0370:7334

## jj2 (best)

```python
class Solution:
    def validIPAddress(self, IP: str) -> str:
        if (IP.count(".") == 3 and          #v4 must be 3 parts seperated by .
            all(                                 #and each part has to be:
                s.isnumeric()
                and int(s) <= 255                #number, < 255,
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
```

* no temp var, use oneliner list comprehension `for s in IP.split`
* `x or y` instead of `expr if else`
* avoid `all('') = true` trick
* use `all(list expression)`, instead of `all([list])`
* use () to break long expression

long line version:

```python
class Solution:
    def validIPAddress(self, IP: str) -> str:
        if (IP.count(".") == 3 and all( s.isnumeric() and int(s) <= 255 and (len(s) == 1 or s[0] != "0") for s in IP.split("."))): return "IPv4"
        if IP.count("::") == 1: IP = IP.replace('::', ':', 1)
        if (1<= IP.count(":") <= 7 and all( all(c in "0123456789abcdefABCDEF" for c in s) and 0 < len(s) <= 4 for s in IP.split(":"))): return "IPv6"
        return "Neither"
```

(Sun Feb 14 00:03:15 2021) 
if including `::` case for IPv6:

```python
class Solution:
    def validIPAddress(self, IP: str) -> str:
        if (IP.count(".") == 3 and          #v4 must be 3 parts seperated by .
            all(                                 #and each part has to be:
                s.isnumeric() and int(s) <= 255  #number, < 255,
                and (len(s) == 1 or s[0] != "0") #first digit can't be "0"
                for s in IP.split(".")           #unless it is just 0.
               )
           ): return "IPv4"
        if IP.count("::") == 1: IP = IP.replace('::', ':", 1)
        if (IP.count(":") == 7 and          #v6 must be 7 parts seprated by :
            all(                                #and each part has to be:
                all(c in "0123456789abcdefABCDEF" for c in s) #from this chars
                and 0 < len(s) <= 4             #less or equal to 4 digits
                for s in IP.split(":")          #but not null (1111::1111)
               )
            ): return "IPv6"
        return "Neither"
S=Solution()
IP="2003::1"
S.validIPAddress(IP)

```



### jj1 v1

```python
def validIPAddress(self, IP):
    # Write your code here
    if "." in IP:
        list4 = IP.split(".")
        if len(list4) == 4 and all([s.isnumeric() and int(s) >= 0 and int(s) <= 255 for s in list4]):
            return "IPv4"
    if ":" in IP and IP.count("::") < 2:
        list6 = IP.split(":")
        hexnums = "0123456789abcdefABCDEF"
        if len(list6) == 8 \
            and all([
                all([c in hexnums for c in s]) for s in list6
            ]):
            return "IPv6"
    return "Neither"
```

### jj1 v2
```python
class Solution:
    def validIPAddress(self, IP: str) -> str:
        # ipv4 is dot seperated groups
        if IP.count(".") == 3:
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
        if IP.count(":") == 7:
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
```

## wangmazi

```python
class Solution(object):
    def validIPAddress(self, IP):
        ip = IP.split('.')
        if len(ip) == 4:
            # ipv4 candidate, validate it
            for octet_s in ip:
                try:
                    octet = int(octet_s)
                except ValueError:
                    return 'Neither'
                if octet < 0 or octet > 255 or (octet_s != '0' and (octet // 10**(len(octet_s) - 1) == 0)):
                    return 'Neither'
            return 'IPv4'
        else:
            ip = IP.split(':')
            if len(ip) == 8:
                # ipv6 candidate, validate it
                for hexa_s in ip:
                    if not hexa_s or len(hexa_s) > 4 or not hexa_s[0].isalnum():
                        return 'Neither'
                    try:
                        hexa = int(hexa_s, base=16)
                    except ValueError:
                        return 'Neither'
                    hexa_redo = '{:x}'.format(hexa)
                    if hexa < 0 or hexa > 65535:
                        return 'Neither'
                return 'IPv6'
        return 'Neither'
```

* make use of exception

## other zb solutions

### socket module

```python
import socket

def is_ipv4(ip):
    try:
        socket.inet_pton(socket.AF_INET, ip)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(ip)
        except socket.error:
            return False
        return ip.count('.') == 3
    except socket.error:  # not a valid ip
        return False
    return True

def is_ipv6(ip):
    try:
        socket.inet_pton(socket.AF_INET6, ip)
    except socket.error:  # not a valid ip
        return False
    return True

def check_ip(ip):
    return is_ipv4(ip)  or is_ipv6(ip)
```

### netaddr module (need to install)

    from netaddr.ip import IPAddress

