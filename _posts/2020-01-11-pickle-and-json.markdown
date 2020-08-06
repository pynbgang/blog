---
layout: post
title: "pickle and json"
published: true
created:  2020 Jan 11 02:44:01 PM
tags: [pickle, json, module, liaoxuefeng, python, notes]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# pickling/serialization/flattening

## pickle.dumps/loads

```python
import pickle

d = dict(name='Bob', age=20, score=88)
data = pickle.dumps(d)
print(data)

reborn = pickle.loads(data)
print(reborn)
```

## json.dumps/loads

    JSON 类型   Python 类型
    =============================
    {}          dict
    []          list
    "string"    'str'或 u'unicode'
    1234.56     int 或 float
    true/false  True/False
    null        None


### dict

```python
import json

d = dict(name='Bob', age=20, score=88)
data = json.dumps(d)
print('JSON Data is a str:', data)
reborn = json.loads(data)
print(reborn)
```

### class

```python

# define a class and generate an instance
class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return 'Student object (%s, %s, %s)' % (self.name, self.age, self.score)
s = Student('Bob', 20, 88)

# to dump:
# use `default` param to pass a func which tells to what we want to convert the
# object. `__dict__` is the built-in dict attr that includes all member info
std_data = json.dumps(s, default=lambda obj: obj.__dict__)
print('Dump Student:', std_data)

# to rebuild:
# use `object_hook` param to pass a func which tells how to use the saved data
# to initialize and generate an object.
rebuild = json.loads(
            std_data,
            object_hook=lambda d: Student(d['name'], d['age'], d['score'])
        )
print(rebuild)
```

### about the built-in `__dict__` attributes

```python
[ins] In [29]: class Student(object):
          ...:     def __init__(self, name, age, score):
          ...:         self.name = name
          ...:         self.age = age
          ...:         self.score = score
          ...:     def __str__(self):
          ...:         return 'Student object (%s, %s, %s)' % (self.name, self.age
          ...: , self.score)
          ...:

[ins] In [30]: s = Student('Bob', 20, 88)

[ins] In [31]: s.__dict__
Out[31]: {'name': 'Bob', 'age': 20, 'score': 88}
```

### exercise

```python
[ins] In [1]: obj = dict(name='小明', age=20)
[ins] In [4]: import json
[ins] In [5]: s = json.dumps(obj, ensure_ascii=True)
[ins] In [6]: s
Out[6]: '{"name": "\\u5c0f\\u660e", "age": 20}'

[ins] In [7]: s2 = json.dumps(obj, ensure_ascii=False)
[ins] In [8]: s2
Out[8]: '{"name": "小明", "age": 20}'
```


