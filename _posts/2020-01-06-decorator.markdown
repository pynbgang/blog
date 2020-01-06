---
layout: post
title: "decorator"
published: true
created:  2020 Jan 06 03:51:29 PM
tags: [python, decorator]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# decorator

## example1: w/o decorator

没有decorator概念之前，在不更改原有函数自身代码的前提下，如何实现对它功能的修改:

```python
def dec(a_func):

    def wrap():
        print("before executing a_func()")
        a_func()
        print("after executing a_func()")

    return wrap

def f():
    print("function being decorated")


f()             # run the original func

f = dec(f)      # modify (decorate) the func

f()             # run the decorated func
```

## example2: with decorator

with python '@', 

    @dec                def f():
    f():        <==>        xxx
        xxx             f=dec(f)

so same thing will look:


```python
def dec(a_func):

    def wrap():
        print("before executing a_func()")
        a_func()
        print("after executing a_func()")

    return wrap

@dec                    # decorate the below func
def f():
    print("function being decorated")

f()                     # run the decorated func
print(f.__name__)       # print the original func name
```

    In [44]: f()
    before executing a_func()
    function being decorated
    after executing a_func()

    In [45]: print(f.__name__)
    wrap        #<--- problem.

* **problem**: the orignal functions name is also changed.
* **solution**: use `functools.wraps` to recover it back

## example3: functools.wraps

```python
from functools import wraps

def dec(a_func):
    @wraps(a_func)
    def wrap():
        print("before executing a_func()")
        a_func()
        print("after executing a_func()")

    return wrap

@dec                    # decorate the below func
def f():
    print("function being decorated")

f()                     # run the decorated func
print(f.__name__)       # print the original func name
```

`@wraps`: 接受一个函数来进行装饰，并加入了复制函数名称、注释文档、
参数列表等等的功能。这可以让我们在装饰器里面访问在装饰之前的函数的
属性。

## example4: 更通用的格式

```python
from functools import wraps

def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)
    return decorated

@decorator_name
def func():
    return("Function is running")

can_run = True
print(func())
# Output: Function is running

can_run = False
print(func())
# Output: Function will not run
```


## example5: usage case: Authorization

```python
from functools import wraps
 
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            authenticate()
        return f(*args, **kwargs)
    return decorated
```


## example6: usage case2: logging

```python
from functools import wraps

def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

@logit
def addition_func(x):
   """Do some math."""
   return x + x

result = addition_func(4)
# Output: addition_func was called
```


## example7: decorator with params

```python
from functools import wraps

def logit(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile，并写入内容
            with open(logfile, 'a') as opened_file:
                # 现在将日志打到指定的logfile
                opened_file.write(log_string + '\n')
            return func(*args, **kwargs)
        return wrapped_function
    return logging_decorator

@logit()
def myfunc1():
    pass

myfunc1()
# Output: myfunc1 was called
# 现在一个叫做 out.log 的文件出现了，里面的内容就是上面的字符串

@logit(logfile='func2.log')
def myfunc2():
    pass

myfunc2()
# Output: myfunc2 was called
# 现在一个叫做 func2.log 的文件出现了，里面的内容就是上面的字符串
```


## example8: decorator in class

TO DO
