# Python Basics README

## Introduction

This README provides an overview of fundamental concepts in Python programming, focusing on objects, classes, mutability, references, and variable handling.

### What is an Object?

In Python, everything is an object. An object is an instance of a particular data type or class. Objects can represent data or functionality and are the building blocks of a Python program.

### Class vs. Object or Instance

- **Class**: A class is a blueprint or template for creating objects. It defines attributes and methods that the objects instantiated from the class will have.
  
  ```python
  class Dog:
      def __init__(self, name):
          self.name = name
  
      def bark(self):
          print(f"{self.name} says woof!")
  ```

- **Object or Instance**: An object is a specific instance of a class. It has attributes and methods as defined by the class.

  ```python
  my_dog = Dog("Buddy")
  my_dog.bark()  # Output: Buddy says woof!
  ```

### Mutable vs. Immutable Objects

- **Mutable Object**: Objects whose value or state can be modified after creation are mutable. Lists are an example of mutable objects.

  ```python
  mutable_list = [1, 2, 3]
  mutable_list.append(4)
  print(mutable_list)  # Output: [1, 2, 3, 4]
  ```

- **Immutable Object**: Objects whose value or state cannot be modified after creation are immutable. Tuples are an example of immutable objects.

  ```python
  immutable_tuple = (1, 2, 3)
  # Attempting to modify will raise an error: 'tuple' object has no attribute 'append'
  ```

### Reference, Assignment, Alias

- **Reference**: A reference is a way to access the memory location of an object. Variables in Python are references to objects.

- **Assignment**: Assignment binds a variable name to an object. It does not create a new object; it associates the variable with the existing object.

  ```python
  x = [1, 2, 3]
  y = x  # Both x and y reference the same list object
  ```

- **Alias**: An alias occurs when two or more variables refer to the same object.

### Identical Variables and Object Linkage

- **Identical Variables**: Variables are identical if they reference the same object.

  ```python
  a = [1, 2, 3]
  b = a
  print(a is b)  # Output: True
  ```

- **Linked to the Same Object**: Two variables are linked to the same object if they share the same reference.

  ```python
  c = [1, 2, 3]
  d = c
  ```

### Displaying Variable Identifier

To display the variable identifier (memory address), you can use the `id()` function.

```python
e = 42
print(id(e))  # Output: Memory address of the object
```

### Mutable and Immutable

- **Mutable**: Objects whose state or value can be changed after creation are mutable.

- **Immutable**: Objects whose state or value cannot be changed after creation are immutable.

### Built-in Mutable Types

- **List**: An ordered, mutable collection.

  ```python
  my_list = [1, 2, 3]
  ```

- **Dictionary**: An unordered, mutable collection of key-value pairs.

  ```python
  my_dict = {'a': 1, 'b': 2}
  ```

### Built-in Immutable Types

- **Tuple**: An ordered, immutable collection.

  ```python
  my_tuple = (1, 2, 3)
  ```

- **String**: An immutable sequence of characters.

  ```python
  my_string = "Hello, Python!"
  ```

### Python Variable Passing to Functions

In Python, variables are passed to functions by object reference. Changes made to mutable objects within a function persist outside the function, while changes to immutable objects do not.

```python
def modify_list(lst):
    lst.append(4)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # Output: [1, 2, 3, 4]
```

This README covers fundamental Python concepts, providing examples and explanations for objects, classes, mutability, references, and variable handling. For a deeper understanding, refer to the official Python documentation and additional learning resources.
