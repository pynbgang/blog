---
layout: post
title: "word count map reduce"
published: true
created:  2020 Feb 08 04:14:15 PM
tags: [python, yield, split]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -


# [word count: map and reduce](https://www.lintcode.com/problem/word-count-map-reduce/description)

## wangmazi

```python
def mapper(self, _, line):
        # Write your code here
        # Please use 'yield key, value'
        for word in line.split():
            yield word, 1


    # @param key is from mapper
    # @param values is a set of value with the same key
    def reducer(self, key, values):
        # Write your code here
        # Please use 'yield key, value'
        yield key, sum(values)
```

![image](https://user-images.githubusercontent.com/2038044/74092149-39937d00-4a8e-11ea-809d-ad89045fa316.png)

## resources

* https://www.youtube.com/watch?v=3LQAaAh4wM8
* https://zhengyang2015.gitbooks.io/lintcode/word_count_map_reduce_499.html
* http://blog.bizcloudsoft.com/wp-content/uploads/Google-MapReduce%E4%B8%AD%E6%96%87%E7%89%88_1.0.pdf

