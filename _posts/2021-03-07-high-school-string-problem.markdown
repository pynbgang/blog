---
layout: post
title: "high school string problem"
published: true
created:  2021 Mar 07 17:32:29
tags: [python, recursion]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# problem

![image](https://user-images.githubusercontent.com/2038044/110257601-951f8b00-7f6c-11eb-93fb-594edf1e1cf4.png)

# solutions

## jj

```python
def str_processing(s):
    d, maxrepeat, res = dict(), 0, [] #dict: counting each letter; res: result
    for c in s:                 #maxrepeat: record max repeat of any letter
        if c.isalpha():         #scan string, for any letter, convert to lower
            k = c.lower()       #and count each letter
            d[k] = d.get(k, 0) + 1
            maxrepeat = max(maxrepeat, d[k]) #record max repeat, as num of pass
    #prepare a list, has "passes" num of empty lists, each as placeholder for
    mat = [[] for i in range(maxrepeat)]  #that pass
    for k in sorted(d.keys()):  #for each (sorted) letter that is in the string
        for i in range(d[k]):   #dispatch it to each placeholder based on its
            mat[i].append(k)    #count. after this, all placeholders are filled
    for r in mat:               #?
        for c in r:             #?
            if not res or res[-1] != c:  #?
                res.append(c)   #?
    return "".join(res)

s = 'A good sorting algorithm.'
s = "OOOOO"
rearrangedString(s)
```

## ping

```python
def rearrangedString(s):        #first prepare valid chars from the string
    s = "".join([c.lower() for c in s if c.isalpha()])
    return worker(s)               #then pass to the worker func

def worker(s):                  #just follow the steps. result, "rest" left
    res, rest, set1 = "", "", set() #in each pass, a set to record occurrence
    for c in s:                 #scan the string
        if c not in set1:       #for each char, if did not occurre yet
            set1.add(c)         #put it in set to record it (- just occurred)
            res += c            #place this char in result
        else:                   #if it occurred, it will be left in "rest" part
            rest += c
    res = "".join(sorted(res))  #sort the current result
    if rest:                    #if rest is not empty, 
        res1 = worker(rest)     #repeat the pass with recursion. assuming result
        if res1 and res[-1] == res1[0]: #of next pass is not empty, and tail of
            return res + res1[1:] #curr res is dup with head of next res, then
        else:                   #skip the dup char, otherwise no skip
            return res + res1
    else:                       #if rest is empty, it indicates the end
        return res

s = 'A good sorting algorithm.'
s = "OOOOO"
rearrangedString(s)
```

## owen

```python
import collections
def tolist(s):
    res=[i.lower() for i in s if i.isalpha()]
    return sorted("".join(res))

def newstring(list1):
    counter=collections.Counter(list1)
    res="".join(sorted(list(set(list1))))
    temp=0
    for i in counter:
        if counter[i]==0:continue
        counter[i]-=1
        temp+=counter[i]
    if temp==0:return res
    nextstr=""
    for i in counter:
        nextstr+=i*counter[i]
    return res+newstring(sorted(nextstr))

def rdstr(s):
    if not s :return ""
    if len(s)==1:return s
    s=s+"."
    res,i,j="",0,1
    while(j<len(s)):
        if s[i]!=s[j]:
            res+=s[i]
            j+=1
            i=j-1
        else:j+=1
    return res

def rearrangedString(s):
    return rdstr(newstring(tolist(s)))

s = 'A good sorting algorithm.'
s = "OOOOO"
rearrangedString(s)
```
