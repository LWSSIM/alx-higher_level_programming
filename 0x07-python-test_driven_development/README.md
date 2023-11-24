# Readme.md

## What's an interactive test?

An interactive test is a type of test where the user can actively participate and provide input during the testing process. It allows for real-time interaction and feedback between the test and the user. In the context of Python, interactive tests often involve running code snippets or functions and providing input through the command line or user prompts.

## Why tests are important

Tests are crucial in software development, including Python programming, for several reasons:

1. **Verification**: Tests verify that the code behaves as expected and produces the correct output. They help catch and prevent bugs and errors.

2. **Validation**: Tests validate that the code meets the specified requirements and performs the desired functionality. They ensure that the software works as intended.

3. **Regression detection**: Tests help identify any regressions or unintended side effects that may occur when making changes or adding new features to the codebase.

4. **Documentation**: Tests serve as living documentation that provides examples and demonstrations of how to use the code. They improve code understandability and facilitate collaboration among developers.

## How to write Docstrings to create tests

Docstrings are a way to document code in Python, and they can also be used to create tests. When writing Docstrings for tests, you can follow a structured format such as using the `doctest` module. Here's an example:

```python
def square_number(number):
    """
    Calculate the square of a given number.

    Parameters:
        number (int): The number to be squared.

    Returns:
        int: The square of the input number.

    Examples:
        >>> square_number(5)
        25
        >>> square_number(-3)
        9
    """
    return number ** 2
```

In this example, the Docstring provides a description of the function, including its parameters and return value. It also includes examples with expected outputs. These examples can be automatically extracted and executed as tests using the `doctest` module.

## How to write documentation for each module and function

To write documentation for each module and function in Python, you can utilize Docstrings. Docstrings are written as multi-line strings immediately following the definition of a module, class, or function. They provide information about the purpose, usage, parameters, return values, and examples of usage for the code.

Here's an example of how to write a Docstring for a module:

```python
"""
This module contains functions for performing mathematical operations.
"""

def add_numbers(a, b):
    """
    Add two numbers together.

    Parameters:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of the two numbers.
    """
    return a + b
```

In this example, the module Docstring provides a brief description of the module's purpose. The function Docstring describes the function's parameters and return value.

## What are the basic option flags to create tests

In Python, there are several basic option flags commonly used to create tests. Some of these flags include:

1. **-v/--verbose**: Provides more detailed output during test execution, including individual test results and any captured output.

2. **-x/--exitfirst**: Stops test execution on the first failure or error encountered. Useful when you want to focus on fixing one issue at a time.

3. **-s/--nocapture**: Disables capturing of the standard output during test execution. Allows printing to the console during tests for debugging purposes.

4. **-k/--keyword**: Selects specific tests to run based on keywords. Only tests matching the specified keywords will be executed.

5. **-m/--markers**: Runs tests based on specified markers. Markers are used to categorize and select tests with specific attributes or behavior.

These are just a few examples of basic option flags commonly used in test frameworks like `pytest`. The specific flags and their functionalities may vary depending on the testing framework being used.

## How to find edge cases

Finding edge cases involves identifying and testing scenarios that lie at the extreme boundaries or limits of the input or functionality of a program. Here are some approaches to finding edge cases in Python:

1. **Identify boundaries**: Determine the maximum and minimum values that the inputs can take or the limits of the program's functionality.

2. **Consider special values**: Think about special values or edge conditions that could affect the behavior of the program. For example, zero, negative numbers, empty inputs, or large input sizes.

3. **Analyze requirements and constraints**: Study the requirements and constraints of the problem or system you are testing. Look for any specific conditions or constraints that may lead to edge cases.

4. **Use equivalence partitioning**: Divide the input domain into smaller partitions and select representative values from each partition. Include values at the boundaries of the partitions to test edge cases.

5. **Explore corner cases**: Think about scenarios where multiple edge conditions coincide. These are often the most challenging and critical edge cases to consider.

Once youhave identified potential edge cases, you can design and write tests specifically targeting those cases. By covering edge cases in your tests, you can ensure that your code handles them correctly and behaves as expected in all scenarios.

```python
import unittest

class MyTestCase(unittest.TestCase):
    def test_edge_case(self):
        # Test an edge case scenario
        self.assertEqual(my_function(0), expected_result)

        # Test another edge case scenario
        self.assertEqual(my_function(1000000), expected_result)

        # Test a corner case scenario
        self.assertEqual(my_function(-1, 0), expected_result)

if __name__ == '__main__':
    unittest.main()
```

In this example, the `test_edge_case()` method contains test cases targeting different edge and corner case scenarios. By running these tests, you can verify the behavior of your code in these critical scenarios.

Remember that finding edge cases requires careful analysis of the problem at hand and an understanding of the requirements and constraints. It's important to cover a range of scenarios that push the boundaries of your code's capabilities and ensure its robustness and reliability.
