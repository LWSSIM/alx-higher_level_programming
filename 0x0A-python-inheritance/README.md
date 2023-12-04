# Python OOP Basics

## Table of Contents

1. [Superclass, Baseclass, or Parentclass](#Superclass-Baseclass-or-Parentclass)
2. [Subclass](#Subclass)
3. [Listing Attributes and Methods](#listing-attributes-and-methods)
4. [Adding New Attributes to Instances](#adding-new-attributes-to-instances)
5. [Inheriting from Another Class](#inheriting-from-another-class)
6. [Defining a Class with Multiple Base Classes](#defining-a-class-with-multiple-base-classes)
7. [Default Class Every Class Inherits From](#default-class-every-class-inherits-from)
8. [Method or Attribute Override](#method-or-attribute-override)
9. [Attributes or Methods Available to Subclasses](#attributes-or-methods-available-to-subclasses)
10. [Purpose of Inheritance](#purpose-of-inheritance)
11. [Built-in Functions: isinstance, issubclass, type, and super](#built-in-functions-isinstance-issubclass-type-and-super)

---

### 1. Superclass, Baseclass, or Parentclass

In Python, a superclass, baseclass, or parentclass is a class from which another class, called a subclass, inherits attributes and methods. It serves as the foundation for the subclass.

```python
class Superclass:
    pass

class Subclass(Superclass):
    pass
```

### 2. Subclass

A subclass is a class that inherits from another class, known as its superclass. It can extend or override the functionality of the superclass.

```python
class Superclass:
    pass

class Subclass(Superclass):
    pass
```

### 3. Listing Attributes and Methods

To list all attributes and methods of a class or instance, you can use the `dir()` function.

```python
class MyClass:
    def __init__(self):
        self.my_attribute = 42

    def my_method(self):
        pass

# Listing attributes and methods
print(dir(MyClass))
```

### 4. Adding New Attributes to Instances

Instances can have new attributes dynamically added.

```python
class MyClass:
    pass

obj = MyClass()
obj.new_attribute = "Hello, World!"
```

### 5. Inheriting from Another Class

To inherit from another class, include the superclass in parentheses after the subclass name.

```python
class Superclass:
    pass

class Subclass(Superclass):
    pass
```

### 6. Defining a Class with Multiple Base Classes

A class can inherit from multiple base classes by separating them with commas.

```python
class BaseClass1:
    pass

class BaseClass2:
    pass

class DerivedClass(BaseClass1, BaseClass2):
    pass
```

### 7. Default Class Every Class Inherits From

The default class every class inherits from is `object`.

```python
class MyClass:
    pass
```

### 8. Method or Attribute Override

To override a method or attribute inherited from the base class, redeclare it in the subclass.

```python
class Superclass:
    def my_method(self):
        print("Superclass method")

class Subclass(Superclass):
    def my_method(self):
        print("Subclass method")

obj = Subclass()
obj.my_method()  # Output: Subclass method
```

### 9. Attributes or Methods Available to Subclasses

All public attributes and methods of the superclass are available to subclasses.

```python
class Superclass:
    def public_method(self):
        pass

class Subclass(Superclass):
    pass

obj = Subclass()
obj.public_method()
```

### 10. Purpose of Inheritance

The purpose of inheritance is to promote code reuse and establish a hierarchy of classes, allowing subclasses to inherit and extend the functionality of superclasses.

### 11. Built-in Functions: isinstance, issubclass, type, and super

- `isinstance`: Checks if an object is an instance of a specified class or a tuple of classes.

```python
obj = MyClass()
print(isinstance(obj, MyClass))  # True
```

- `issubclass`: Checks if a class is a subclass of another class.

```python
print(issubclass(Subclass, Superclass))  # True
```

- `type`: Returns the type of an object.

```python
obj = MyClass()
print(type(obj))  # <class '__main__.MyClass'>
```

- `super`: Returns a temporary object of the superclass, allowing access to its methods.

```python
class Superclass:
    def my_method(self):
        pass

class Subclass(Superclass):
    def my_method(self):
        super().my_method()  # Calls the superclass method
```

