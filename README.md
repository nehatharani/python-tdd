# String Calculator

**Problem Statement:**
> Using Python with a Test Driven Development (TDD) approach, create a simple String Calculator which covers the following requirements from [read more](http://osherove.com/tdd-kata-1/):
> 1. adds numbers present in the input, e.g "1,2" = 3, "10,4"=14 
> 2. treats empty or null input as zero, e.g "" = 0, null = 0
> 3. supports different delimiters, e.g "1,2,3", "1 2 3"
> 4. does not support negative numbers
> 5. ignores numbers greater than 100


---
The problem is solved keeping in mind the extendability. 

**string_calculator.py**

This file contains the main add function. The signature of the function is:
```
def add(input_str, delim=",")

```
The function accepts an input string of digits and a type of delimiter and returns the sum of the digits. 

**utility_functions.py**

The main idea is to have functions that do one or two tasks in order to maintain readability and code organisation. In the current scope of the problem statement, I have just one utility function.

This file contains any utility functions that are used to solve the problem. The functions can be reused when the functionality is extended, for instance, writing a subtract method.

**string_calculator_test.py**

This is where all the magic happens. This file contains two classes namely, ```class TestUtilityFunctions(unittest.TestCase)``` and ```class TestStringCalculator(unittest.TestCase)```. All the testing is done here. 

Class TestUtilityFunctions has a method called ``` test_check_constraints``` which checks the edge case or requirement to treat a empty or null input as zero, e.g "" = 0, null = 0

Class TestStringCalculator is meant to check the implementation of add method with respect to the requirements. It has the following methods:

```test_adds_number_seperated_by_comma``` simply checks that the program adds numbers present in the input, e.g "1,2" = 3, "10,4"=14. 

```test_string_calculator_empty_str_returns_zero``` checks that treat a empty or null input as zero, e.g "" = 0, null = 0 

```test_single_number_should_return_itself``` checks if the input is a single number, it should return itself.

```test_supports_different_delimiters``` checks that it supports different delimiters, e.g "1,2,3", "1 2 3"

```test_raise_error_for_negative_num``` makes sure that the program does not support negative numbers. It should raise the ValueTooSmallError. 

```test_ignores_nums_greater_than_100``` ignores numbers greater than 100 eg. '100,2' should return 2, '101' should return 0

**string_calculator_exceptions.py**

This file contains user-defined exceptions, which define the error ValueTooSmallError for negative numbers.