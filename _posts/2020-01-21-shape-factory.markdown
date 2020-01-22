---
layout: post
title: "shape-factory"
published: true
created:  2020 Jan 21 10:54:51 PM
tags: [oo, python, exception, easy, lintcode]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -


# [shape-factory](https://www.lintcode.com/problem/shape-factory/description?_from=ladder&&fromId=99)


## code

```python
"""
Your object will be instantiated and called as such:
sf = ShapeFactory()
shape = sf.getShape(shapeType)
shape.draw()
"""
class Shape:
    def draw(self):
        raise NotImplementedError('This method should have implemented.')

class Triangle(Shape):
    # Write your code here
    def draw(self):
        print("  /\\")
        print(" /  \\")
        print("/____\\")

class Rectangle(Shape):
    # Write your code here
    def draw(self):
        print(" ----")
        print("|    |")
        print(" ----")

class Square(Shape):
    # Write your code here
    def draw(self):
        print(" ----")
        print("|    |")
        print("|    |")
        print(" ----")

class Diamond(Shape):
    # Write your code here
    pass

class ShapeFactory:
    # @param {string} shapeType a string
    # @return {Shape} Get object of type Shape
    def getShape(self, shapeType):
        # Write your code here
        if shapeType == "Triangle":
            return Triangle()
        if shapeType == "Rectangle":
            return Rectangle()
        if shapeType == "Square":
            return Square()
        if shapeType == "Diamond":
            return Diamond()
```

## test1

```python
sf = ShapeFactory()
shape = sf.getShape('Triangle')
shape.draw()
```

    [ins] In [60]: sf = ShapeFactory()
    [ins] In [61]: shape = sf.getShape('Triangle')
    [ins] In [62]: shape.draw()
    /\
    /  \
    /____\


## test2

```python
sf = ShapeFactory()
shape = sf.getShape('Diamond')
shape.draw()
```

    [ins] In [57]: sf = ShapeFactory()
    [ins] In [58]: shape = sf.getShape('Diamond')
    [ins] In [59]: shape.draw()
    ---------------------------------------------------------------------------
    NotImplementedError                       Traceback (most recent call last)
    <ipython-input-59-739b968dc53b> in <module>
    ----> 1 shape.draw()
    <ipython-input-46-ccc901d2ff83> in draw(self)
        1 class Shape:
        2     def draw(self):
    ----> 3         raise NotImplementedError('This method should have implemented.')
        4
    NotImplementedError: This method should have implemented.


## tips

* from a method of an object to return another object


