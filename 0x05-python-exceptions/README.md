# 0x05-python-exceptions

## Difference between errors and exceptions

In Python, "errors" typically refer to syntax errors or problems that prevent the interpreter from running the code. On the other hand, "exceptions" are runtime errors that occur during the execution of a program.

## What are exceptions and how to use them

Exceptions are events that can occur during the execution of a program that disrupts the normal flow of instructions. They can be handled using `try`, `except`, `else`, and `finally` blocks.

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Caught an exception: {e}")
else:
    print("No exception occurred.")
finally:
    print("This will be executed regardless of whether an exception occurred.")
```

## When do we need to use exceptions

Exceptions are useful when dealing with unexpected situations or errors that may occur during runtime, allowing the program to gracefully handle these scenarios.

## How to correctly handle an exception

To handle an exception, use a `try` block to enclose the code that might raise an exception, and then use an `except` block to specify how to handle the exception.

```python
try:
    result = int("abc")
except ValueError as e:
    print(f"Caught a ValueError: {e}")
```

## Purpose of catching exceptions

Catching exceptions allows the program to respond to errors without crashing. It provides a way to gracefully handle unexpected situations and continue execution or take appropriate actions.

## How to raise a built-in exception

You can raise a built-in exception using the `raise` keyword.

```python
def example_function(value):
    if value < 0:
        raise ValueError("Value must be non-negative.")
    return value

try:
    result = example_function(-5)
except ValueError as e:
    print(f"Caught an exception: {e}")
```

## When to implement a clean-up action after an exception

A clean-up action, specified in a `finally` block, is executed whether an exception occurs or not. This is useful for releasing resources or performing cleanup tasks.

```python
file = None
try:
    file = open("example.txt", "r")
    # Code that may raise an exception
except FileNotFoundError as e:
    print(f"Caught an exception: {e}")
finally:
    if file:
        file.close()
    print("File closed, regardless of whether an exception occurred.")
```
## Some common Python exeptions

Here are some of the most common exceptions in Python and brief explanations of each:

1. **SyntaxError:**
   - Raised when there is a syntax error in the code, indicating a mistake in the way the code is written.

   ```python
   print "Hello, World!"
   ```

2. **IndentationError:**
   - Occurs when there is an incorrect indentation in the code, violating the Python indentation rules.

   ```python
   def example_function():
   print("Indented incorrectly.")
   ```

3. **NameError:**
   - Raised when a local or global name is not found.

   ```python
   print(variable_not_defined)
   ```

4. **TypeError:**
   - Occurs when an operation or function is applied to an object of an inappropriate type.

   ```python
   result = "10" + 5
   ```

5. **ValueError:**
   - Raised when a built-in operation or function receives an argument with the correct type but an inappropriate value.

   ```python
   number = int("abc")
   ```

6. **ZeroDivisionError:**
   - Raised when the second operand of a division or modulo operation is zero.

   ```python
   result = 10 / 0
   ```

7. **FileNotFoundError:**
   - Raised when an attempt is made to open a file that does not exist.

   ```python
   with open("nonexistent_file.txt", "r") as file:
       content = file.read()
   ```

8. **IndexError:**
   - Raised when a sequence subscript is out of range.

   ```python
   my_list = [1, 2, 3]
   print(my_list[5])
   ```

9. **KeyError:**
   - Raised when a dictionary key is not found.

   ```python
   my_dict = {"a": 1, "b": 2}
   print(my_dict["c"])
   ```

10. **AttributeError:**
    - Raised when an attribute reference or assignment fails.

    ```python
    my_list = [1, 2, 3]
    my_list.append(4)
    print(my_list.len())
    ```

Understanding these common exceptions is crucial for effective debugging and writing robust Python code.
