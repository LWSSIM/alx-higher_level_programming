# Python Imports and Modules

Python is a powerful and versatile programming language that provides a way to organize your code into reusable units, which are known as modules. Modules allow you to structure your code, making it more maintainable and efficient. This README will guide you through various aspects of Python modules, imports, and other related topics.

## Table of Contents
- [How to import functions from another file](#how-to-import-functions-from-another-file)
- [How to use imported functions](#how-to-use-imported-functions)
- [How to create a module](#how-to-create-a-module)
- [How to use the built-in function `dir()`](#how-to-use-the-built-in-function-dir)
- [How to prevent code in your script from being executed when imported](#how-to-prevent-code-in-your-script-from-being-executed-when-imported)
- [How to use command line arguments with your Python programs](#how-to-use-command-line-arguments-with-your-python-programs)

## How to import functions from another file

In Python, you can import functions, classes, and variables from another file using the `import` statement. The syntax for importing is as follows:

```python
import module_name # do not include .py(c) extention
```
or if you want only specific function from that file:
```python
from module_name import function_name
```

For example, to import a function `my_function` from a module called `my_module`, you can do:

```python
from my_module import my_function
```

## How to use imported functions

Once you've imported a function, you can use it in your code just like any other function. For example:
```python
>>>import my_module
>>>my_module.my_function()
```
You can also store it in a variable (after import) for easy access:
```python
result = my_module.my_function()
```
if you used `from`---`import`---, you can omit the `module.` prefix, and directly call it. 

You call the function as you would with any local function.

## How to create a module

A Python module is a file containing Python definitions and statements. To create a module, you can simply create a `.py` file with your code. For example, to create a module named `my_module.py`:

```python
# my_module.py
def my_function():
    return "Hello from my_module"
```

You can then import and use this module in other Python scripts.

## How to use the built-in function `dir()`

The `dir()` function is used to list all the names in the current local and global scope. It's a useful tool for exploring the contents of a module, object, or the current scope. For example:

```python
import math
print(dir(math))
```

This will display a list of all names available in the `math` module.

## How to prevent code in your script from being executed when imported

Sometimes, you may have code in your script that you don't want to run when the script is imported as a module. To prevent specific code from running on import, you can use the following conditional check:

```python
if __name__ == "__main__":
    # Code here will only run when the script is executed, not when imported
    # Add your main program logic here
```

Code placed under the `if __name__ == "__main__":` block will only run if the script is executed directly.

## How to use command line arguments with your Python programs

You can access command line arguments in your Python scripts using the `sys.argv` list from the `sys` module. Here's a basic example of how to access command line arguments:

```python
import sys

# Get the command line arguments
args = sys.argv

# Print the arguments
for arg in args:
    print(arg)
```

When you run your Python script from the command line, you can pass arguments after the script name, and they will be accessible in the `sys.argv` list.

## More Info

-More on [modules/dir()](https://docs.python.org/3/tutorial/modules.html), [OSI/command line arguments](https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments)

*`Happy pything`*
