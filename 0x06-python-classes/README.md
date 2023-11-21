# Python Concepts

This README file provides an overview of various Python concepts related to object-oriented programming (OOP) and attribute handling. It includes definitions, code examples, and explanations where applicable.

## Table of Contents
- [OOP (Object-Oriented Programming)](#OOP)
- ["First-Class Everything"](#first-class-everything)
- [Class](#class)
- [Object and Instance](#object-and-instance)
- [Difference Between Class and Object/Instance](#difference-between-class-and-object-or-instance)
- [Attribute](#attribute)
- [Public, Protected, and Private Attributes](#public-protected-and-private-attributes)
- [Self](#self)
- [Method](#method)
- [Special `__init__` Method](#special-__init__-method)
- [Data Abstraction, Data Encapsulation, and Information Hiding](#data-abstraction-data-encapsulation-and-information-hiding)
- [Property](#property)
- [Difference Between Attribute and Property](#difference-between-attribute-and-property-in-python)
- [Pythonic Getters and Setters](#pythonic-way-to-write-getters-and-setters-in-python)
- [Dynamically Creating Attributes for Existing Instances](#Dynamically-Creating-Attributes-for-Existing-Instances)
- [Binding Attributes to Object and Classes](#Binding-Attributes-to-Object-and-Classes)
- [`__dict__` of a Class/Instance](#__dict__-of-a-class-andor-instance-of-a-class)
- [Attribute Lookup in Python](#attribute-lookup-in-python)
- [Using `getattr()` Function](#using-getattr-function)

## OOP (Object-Oriented Programming)

Object-Oriented Programming (OOP) is a programming paradigm that organizes code around objects, which are instances of classes. It emphasizes the concepts of encapsulation, inheritance, and polymorphism. In Python, OOP allows the creation and manipulation of objects that have both data (attributes) and behavior (methods).

## "First-Class Everything"

In Python, the principle of "first-class everything" means that everything in the language, including functions and classes, is treated as an object. This means you can assign them to variables, pass them as arguments to functions, or return them as values from functions.

Example:
```python
def greet():
    print("Hello, world!")

g = greet  # Assigning function greet to variable g
g()        # Calling function using variable g
```

## Class

A class is a blueprint or template for creating objects. It defines the attributes (data) and methods (functions) that an object will have. The attributes represent the state of the object, while the methods define its behavior.

Example:
```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self):
        print(f"Driving {self.make} {self.model}")

my_car = Car("Tesla", "Model S")
```

## Object and Instance

An object is a specific entity created from a class. It is an instance of that class and possesses the attributes and methods defined in the class.

Example:
```python
my_car = Car("Tesla", "Model S")  # Creating an object (instance) of the Car class
```

## Difference Between Class and Object/Instance

A class is a blueprint or template, while an object/instance is a specific entity created from that blueprint. The class defines the attributes and methods that the object will have, whereas the object/instance represents a specific instance of the class with its own unique attribute values.

## Attribute

An attribute is a piece of data associated with an object or class. It represents the state of the object or class. Attributes can be accessed and modified using dot notation (`object.attribute` or `class.attribute`).

Example:
```python
my_car.make  # Accessing the 'make' attribute of the 'my_car' object
my_car.model = "Model 3"  # Modifying the 'model' attribute of the 'my_car' object
```

## Public, Protected, and Private Attributes
In Python, attribute visibility can be controlled using naming conventions. By convention, attributes that are intended to be public are prefixed with an underscore (`_`), protected attributes are prefixed with double underscores (`__`), and private attributes are prefixed with double underscores and suffixed with single underscores (`__`).

Example:
```python
class MyClass:
    def __init__(self):
        self.public_attr = 123
        self._protected_attr = "456"
        self.__private_attr__ = "789"

obj = MyClass()
obj.public_attr  # Accessing public attribute
obj._protected_attr  # Accessing protected attribute (convention, not enforced)
obj.__private_attr__  # Accessing private attribute (name mangling)
```

## Self

In Python, `self` is a conventionally used parameter name in method definitions within a class. It refers to the instance of the class on which the method is called. It allows access to the object's attributes and methods within the class.

Example:
```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

my_circle = Circle(5)
my_circle.calculate_area()  # Calling the method using the object
```

## Method

A method is a function defined within a class. It defines the behavior of an object or class. Methods can access and manipulate the object's attributes.

Example:
```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height

my_rectangle = Rectangle(10, 5)
my_rectangle.calculate_area()  # Calling the method using the object
```

## Special `__init__` Method

The `__init__` method is a special method in Python classes. It is automatically called when an object is created from a class and allows you to initialize the object's attributes. It is commonly used to set the initial state of the object.

Example:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 25)  # Creating an object and initializing attributes
```

## Data Abstraction, Data Encapsulation, and Information Hiding
- **Data Abstraction:** Data abstraction is the process of hiding the internal implementation details of a class and exposing only the essential information or behavior to the outside world. It allows users to interact with objects using a simplified interface.

- **Data Encapsulation:** Data encapsulation is the bundling of data and the methods that operate on that data within a single unit, such as a class. It ensures that the data is accessed and modified only through the defined methods, providing control over data integrity.

- **Information Hiding:** Information hiding is the principle of hiding the internal details of an object and providing access to only the necessary information. It allows objects to maintain their integrity by preventing direct access to internal data.

## Property

A property is a special attribute that allows customizing the access and modification of an object's attribute. It provides control over attribute assignment, retrieval, and deletion by defining getter, setter, and deleter methods.

Example:
```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

my_circle = Circle(5)
my_circle.diameter  # Accessing the 'diameter' property
my_circle.diameter = 10  # Modifying the 'diameter' property
```

## Difference Between Attribute and Property in Python

An attribute is a data item associated with an object or class, while a property is a special attribute that provides controlled access to another attribute. Properties allow customizing the behavior of attribute access and modification.

## Pythonic Way to Write Getters and Setters in Python

In Python, getters and setters are typically implemented using the `@property` decorator for the getter method and the corresponding setter method with the `@<attribute_name>.setter` decorator.

Example:
```python
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

person = Person("Alice")
person.name  # Accessing the 'name' attribute using the getter method
person.name = "Bob"  # Modifying the 'name' attribute using the setter method
```

## Dynamically Creating Attributes for Existing Instances

In Python, you can dynamically create new attributes for existing instances of a class by directly assigning a value to a previously non-existent attribute. This flexibility allows you to add attributes to objects on-the-fly.

Example:
```python
class Person:
    def __init__(self, name):
        self.name = name

person = Person("Alice")

# Dynamically creating a new attribute for the 'person' instance
person.age = 25

print(person.age)  # Output: 25
```

In the example above, the `age` attribute is dynamically created for the `person` instance by assigning a value to it. This attribute did not exist when the instance was initially created.

## Binding Attributes to Object and Classes

In Python, attributes can be bound to both objects and classes. When an attribute is bound to an object, it is specific to that particular instance of the class. When an attribute is bound to a class, it is shared among all instances of that class.

Example:
```python
class Circle:
    class_attribute = "Shared attribute"  # Bound to the class

    def __init__(self, radius):
        self.radius = radius  # Bound to the object (instance)

circle1 = Circle(5)
circle2 = Circle(10)

print(circle1.radius)  # Output: 5
print(circle2.radius)  # Output: 10
print(circle1.class_attribute)  # Output: Shared attribute
print(circle2.class_attribute)  # Output: Shared attribute
```

In the example above, the `class_attribute` is bound to the `Circle` class, so it is shared among all instances of the class. The `radius` attribute is bound to individual instances (`circle1` and `circle2`), so each instance has its own value for the `radius` attribute.

## `__dict__` of a Class and/or Instance
In Python, the `__dict__` attribute is a dictionary that contains the attributes and their corresponding values of a class or an instance of a class. It provides a way to access and manipulate the attributes dynamically.

Example:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 25)

print(Person.__dict__)  # Output: {'__module__': '__main__', '__init__': <function Person.__init__ at 0x000001>, 'name': <member at 0x000002>, 'age': <member at 0x000003>, ...}
print(person.__dict__)  # Output: {'name': 'Alice', 'age': 25}
```

In the example above, `Person.__dict__` contains the attributes defined in the `Person` class, including the `__init__` method, `name`, and `age`. `person.__dict__` contains the attributes specific to the `person` instance, which are `name` and `age` along with their respective values.

## Attribute Lookup in Python

When accessing an attribute of an object or a class in Python, the interpreter performs attribute lookup to find the attribute. The lookup process starts with the instance's `__dict__` dictionary. If the attribute is not found in the instance's dictionary, the interpreter continues the search in the class's `__dict__` dictionary and its parent classes (following the method resolution order).

Example:
```python
class Vehicle:
    class_attribute = "Shared attribute"

    def __init__(self):
        self.instance_attribute = "Instance attribute"

vehicle = Vehicle()

print(vehicle.instance_attribute)  # Output: Instance attribute
print(vehicle.class_attribute)  # Output: Shared attribute
```

In the example above, when `vehicle.instance_attribute` is accessed, the interpreter first looks for the attribute in the instance's `__dict__`, and since it's present, the value is returned. When `vehicle.class_attribute` is accessed, the interpreter doesn't find it in the instance's `__dict__`, so it looks for it in the class's `__dict__` and returns the value.

## Using `getattr()` Function

The `getattr()` function in Python is used to dynamically retrieve the value of an attribute from an object or a class. It takes the object or class as the first argument and the attribute name as the second argument. Additionally, you can provide a default value as the third argument, which is returned if the attribute doesn't exist.
