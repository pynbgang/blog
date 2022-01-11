---
layout: post
title: "global nonlocal"
published: true
date: 2020-01-09
created:  2020 Jan 10 07:38:47 PM
tags: [python, global, nonlocal, notes]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -


# examples

## refer is fine

```python
x = 5

def myfnc():
  print("inside myfnc", x)
  def myfnc2():
    print("inside myfnc2", x)

  myfnc2()

myfnc()
```

## change triggers errors

```python
x = 5

def myfnc():
    print("inside myfnc", x)
    def myfnc2():
        print("inside myfnc2", x)
        x = 10 #在嵌套的方程中对x重新赋值
        print("x = ", x)
    myfnc2()

myfnc()
```

          2     print("inside myfnc", x)
          3     def myfnc2():
    ----> 4         print("inside myfnc2", x)
          5         x = 10
          6         print("x = ", x)

    UnboundLocalError: local variable 'x' referenced before assignment

## solution: use global: now change is ok

```python
x = 5

def myfnc():
    print("inside myfnc", x)
    def myfnc2():
        global x
        print("inside myfnc2", x)
        x = 10 #在嵌套的方程中对x重新赋值
        print("x = ", x)
    myfnc2()

myfnc()
```


## global can't solve one scenario

```python
x = 5

def myfnc():
    print("inside myfnc", x)
    y=10
    def myfnc2():
        global x
        global y
        print("inside myfnc2", x, ' ', y)
        x = 10 #在嵌套的方程中对x重新赋值
        print("x = ", x)
        y = 10 #在嵌套的方程中对y重新赋值
        print("y = ", y)
    myfnc2()

myfnc()
```

          5         global x
          6         global y
    ----> 7         print("inside myfnc2", x, ' ', y)
          8         x = 10
          9         print("x = ", x)

    NameError: name 'y' is not defined

因为使用了global后，系统到最外层去找，但是此处最外层没有定义y

## example: use nonlocal

nonlocal关键字用来在函数或其他作用域中使用外层（非全局）变量

```python
x = 5

def myfnc():
    print("inside myfnc", x)
    y=10
    def myfnc2():
        global x
        nonlocal y
        print("inside myfnc2", x, ' ', y)
        x = 10 #在嵌套的方程中对x重新赋值
        print("x = ", x)
        y = 10 #在嵌套的方程中对x重新赋值
        print("y = ", y)
    myfnc2()

myfnc()
```

## conclusion

* global:   仅仅到"最"外层去找。  
* nonlocal: 字面意思就是除了local之外的任何层，包含，但不限于最外层（global）


