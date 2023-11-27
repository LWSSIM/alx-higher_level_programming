# 0x08 Python More Classes

This README.md file provides an overview of fundamental concepts related to object-oriented programming (OOP) in Python.

## Table of Contents
- [Class](#class)
- [Object and Instance](#object-and-instance)
- [Class vs. Object/Instance](#class-vs-objectinstance)
- [Attribute](#attribute)
- [Access Modifiers](#access-modifiers)
- [self](#self)
- [Method](#method)
- [`__init__` Method](#__init__-method)
- [Data Abstraction, Encapsulation, and Information Hiding](#data-abstraction-encapsulation-and-information-hiding)
- [Property](#property)
- [Attribute vs. Property](#attribute-vs-property)
- [Getters and Setters](#getters-and-setters)
- [`__str__` and `__repr__` Methods](#__str__-and-__repr__-methods)
- [Class Attribute](#class-attribute)
- [Object Attribute vs. Class Attribute](#object-attribute-vs-class-attribute)
- [Class Method](#class-method)
- [Static Method](#static-method)
- [Dynamically Creating Attributes](#dynamically-creating-attributes)
- [Binding Attributes](#binding-attributes)
- [`__dict__`](#__dict__)
- [Finding Attributes](#finding-attributes)
- [Using getattr Function](#using-getattr-function)
- [Referals](#referals)

## Class
A class is a blueprint for creating objects. It defines attributes and methods that will be common to all instances of the class.

```python
class MyClass:
    pass
```

## Object and Instance
An object is an instance of a class. Instance and object are often used interchangeably.

```python
obj = MyClass()  # Creating an instance of MyClass
```

## Class vs. Object/Instance
A class is a template, while an object/instance is a concrete realization of that template.

## Attribute
An attribute is a characteristic or property of an object.

```python
class Dog:
    def __init__(self, name):
        self.name = name  # 'name' is an attribute
```

## Access Modifiers
Attributes can be public, protected, or private. In Python, this is achieved through naming conventions.

- Public: No prefix
- Protected: Prefix with a single underscore
- Private: Prefix with double underscore

```python
class MyClass:
    def __init__(self):
        self.public_attr = 1        # Public attribute
        self._protected_attr = 2     # Protected attribute
        self.__private_attr = 3      # Private attribute
```

## self
`self` is a reference to the instance of the class and is passed as the first parameter to all instance methods.

```python
class MyClass:
    def my_method(self):
        print("Hello from", self)
```

## Method
A method is a function defined within a class.

```python
class MyClass:
    def my_method(self):
        print("Hello from my_method")
```

## `__init__` Method
The `__init__` method initializes the attributes of an object when it is created.

```python
class Dog:
    def __init__(self, name):
        self.name = name
```

## Data Abstraction, Encapsulation, and Information Hiding
- Data Abstraction: Representing essential features without including implementation details.
- Data Encapsulation: Bundling of data and methods that operate on the data.
- Information Hiding: Restricting access to certain details of an object.

## Property
A property is a special kind of attribute that allows controlled access.

```python
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height
```

## Attribute vs. Property
Attributes are data members, while properties are attributes with getter, setter, and deleter methods.

## Getters and Setters
Use properties to create Pythonic getters and setters.

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
```

## `__str__` and `__repr__` Methods
`__str__` returns a user-friendly string representation, while `__repr__` returns an unambiguous string for developers.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"
```

## Class Attribute
A class attribute is shared among all instances of a class.

```python
class Car:
    wheels = 4  # Class attribute shared by all instances

    def __init__(self, make):
        self.make = make
```

## Object Attribute vs. Class Attribute
Object attributes are specific to each instance, while class attributes are shared among all instances.

## Class Method
A class method is a method bound to the class and not the instance.

```python
class MyClass:
    count = 0  # Class attribute

    def __init__(self):
        MyClass.count += 1

    @classmethod
    def get_count(cls):
        return cls.count
```

## Static Method
A static method is a method that is not bound to the instance or class.

```python
class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y
```

## Dynamically Creating Attributes
You can dynamically create attributes for existing instances of a class.

```python
class MyClass:
    pass

obj = MyClass()
obj.new_attribute = 42
```

## Binding Attributes
Attributes can be bound to both objects and classes.

```python
class MyClass:
    class_attr = 10

obj = MyClass()
obj.obj_attr = 20
```

## `__dict__`
`__dict__` contains the namespace of a class or an instance.

```python
class MyClass:
    class_attr = 10

obj = MyClass()
print(obj.__dict__)  # {'obj_attr': 20}
```

## Finding Attributes
--Attribute Lookup in Python--

When accessing an attribute of an object or class, Python follows a specific order called attribute lookup. It first checks the object's instance attributes, then the class attributes, and finally the attributes inherited from parent classes. 

Python looks for attributes in the instance namespace first and then in the class namespace.

## Using getattr Function
`getattr` retrieves the value of an attribute if it exists.

```python
class MyClass:
    my_attr = 42

obj = MyClass()
value = getattr(obj, 'my_attr', None)  # Retrieves the value of 'my_attr' or None if not found
```

## Referals
- A good article about [OOP](https://python.swaroopch.com/oop.html)
- [`# OOP concepts in Python`](https://www.geeksforgeeks.org/python-oops-concepts/?ref=lbp)
