---
layout: post
title: "validate-ip-address"
published: true
created:  2020 Jan 02 03:30:01 PM
tags: [leetcode, python, lintcode, networking, all, split, count]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -


# [validate-ip-address](https://www.lintcode.com/problem/validate-ip-address/description)

IPv4 addresses are canonically represented in dot-decimal
notation, which consists of four decimal numbers, each ranging
from 0 to 255, separated by dots ("."), e.g.,172.16.254.1;

Besides, leading zeros in the IPv4 is invalid. For example, the
address 172.16.254.01 is invalid.

IPv6 addresses are represented as eight groups of four
hexadecimal digits, each group representing 16 bits. The groups
are separated by colons (":"). For example, the address
2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid one. Also, we
could omit some leading zeros among four hexadecimal digits and
some low-case characters in the address to upper-case ones, so
2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6
address(Omit leading zeros and using upper cases).

However, we don't replace a consecutive group of zero value with
a single empty group using two consecutive colons ("::") to
pursue simplicity. For example, 2001:0db8:85a3::8A2E:0370:7334
is an invalid IPv6 address.

Besides, extra leading zeros in the IPv6 is also invalid. For
example, the address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is
invalid.

## notes

v4:

* 4 decimal nums, each ranging from 0-255, separated by ".", e.g.,172.16.254.1
* leading zeros is invalid. For example, 172.16.254.01 is invalid.

v6:

* 8 groups of 4 hexadecimal digits, each group representing 16 bits. 
* groups are separated by ":". e.g.: 2001:0db8:85a3:0000:0000:8a2e:0370:7334.
* omit some leading zeros among four hexadecimal digits
* some low-case characters in the address to upper-case ones: e.g: 
  - 2001:db8:85a3:0:0:8A2E:0370:7334 is valid
* extra leading zeros is invalid. e.g. 02001:0db8:85a3:0000:0000:8a2e:0370:7334

## jj1 original

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

## jj1 update
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

## jj2 (best)

```python
def validIPAddress(self, IP):
    # Write your code here
    if IP.count(".") == 3 \
        and all([
            s.isnumeric() and int(s) <= 255
            and (len(s) == 1 or s[0] != "0")
            for s in IP.split(".")
        ]):
        return "IPv4"
    hexnums = "0123456789abcdefABCDEF"
    if IP.count(":") == 7 \
        and all([
            all([c in hexnums for c in s])
            and len(s) <= 4
            for s in IP.split(":")
        ]):
        return "IPv6"
    return "Neither"
```

* save temp var: `for s in IP.split`
* `x or y` instead of `expr if else`
* ...

## zhangba

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

