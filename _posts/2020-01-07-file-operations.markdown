---
layout: post
title: "file operations"
published: true
created:  2020 Jan 07 09:13:34 PM
tags: [file, python, py2]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

## file operations

### file/folder operations

    if os.path.exists(fname):

    >>> import os
    >>> os.path.isdir('/tmp')
    True
    >>> os.chdir('/tmp')
    >>>
    >>> cwd=os.getcwd()
    >>> cwd
    '/tmp'
    >>> os.mkdir('example')
    >>> os.chdir('example')
    >>> cwd=os.getcwd()
    >>> cwd
    '/tmp/example'
    >>> os.listdir(cwd)

### file read/write w/o 'with'

more examples P349

* open
* read():       read all file
* read(size):   read "size" file
* readline():   read one line at a time
* readlines():  read all lines and return list
* f.close

test:

    for line in f.readlines():
      print(line.strip()) # 把末尾的'\n'删掉

    In [6]: myfile=open('temp.p')

    In [7]: filecontent=myfile.read()

    In [8]: filecontent
    Out[8]: 'first line\nsecond line'

    In [9]: myfile.read()
    Out[9]: ''

    In [12]: myfile.seek(0)
    Out[12]: 0

    In [13]: line1=myfile.readline()

    In [14]: line1
    Out[14]: 'first line\n'

    In [15]: line2=myfile.readline()

    In [16]: line2
    Out[16]: 'second line'

    In [17]: line3=myfile.readline()

    In [18]: line3
    Out[18]: ''

    for line in open('test.txt'):
        print line

* write('abc')/writelines

### about `with..as..`

use "context manager" with 'with .. as'

    with open('/path/to/file', 'r') as f:
        print f.read()

or

    with open('/path/to/file', 'w') as f:
        f.write('Hello, world!')

python keyword, using "context manager": internally encapsulated exception
handling when "__enter__" the class, and when "__exit__" it. this will ensure
some resources will always be releases when exiting.

equivalent to:

    try:
        f = open('/path/to/file', 'r')
        print(f.read())
    finally:
        if f:
            f.close()

to test 'with' internals:

    class Sample:
        def __enter__(self):
            print("in __enter__")
            return "Foo"
        def __exit__(self, exc_type, exc_val, exc_tb):
            print("in __exit__")

    def get_sample():
        return Sample()

    with get_sample() as sample:
        print("Sample: ", sample)

output:

    in __enter__
    Sample:  Foo
    in __exit__

so 整个运行过程如下：

* enter()方法被执行；
* enter()方法的返回值，在这个例子中是”Foo”，赋值给变量sample；
* 执行代码块，打印sample变量的值为”Foo”；
* exit()方法被调用；

with后面的代码块抛出异常时，exit()方法被执行。开发库时，清理资源，关闭文件等操
作，都可以放在exit()方法中。
总之，with-as表达式极大的简化了每次写finally的工作，这对代码的优雅性是有极大帮
助的。


other usages:

    With open('1.txt') as f1, open('2.txt') as  f2:
        do something

or:

    try:
	with open( "a.txt" ) as f :
	    do something
    except xxxError:
	do something about exception

read further:

* http://zhoutall.com/archives/325
* https://blog.csdn.net/u012609509/article/details/72911564

### with `with..as..` (liaoxuefeng)

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

with open('test.txt', 'w') as f:
    f.write('今天是 ')
    f.write(datetime.now().strftime('%Y-%m-%d'))

with open('test.txt', 'r') as f:
    s = f.read()
    print('open for read...')
    print(s)

with open('test.txt', 'rb') as f:
    s = f.read()
    print('open as binary for read...')
    print(s)
```

### quick test

```python
[ins] In [1]: f=open('2020-01-07-file.markdown')

[ins] In [2]: s=[]
        ...: with open('2020-01-07-file.markdown') as f:
        ...:     for i in range(10):
        ...:         s.append(f.readline())
        ...:

[ins] In [3]: s
Out[3]:
['---\n',
'layout: post\n',
'title: "file"\n',
'published: true\n',
'created:  2020 Jan 07 09:13:34 PM\n',
'tags: [file, python]\n',
'categories: [tech]\n',
'\n',
'---\n',
'\n']
```
