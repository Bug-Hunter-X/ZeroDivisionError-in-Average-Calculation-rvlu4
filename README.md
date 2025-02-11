# Python Average Calculator with ZeroDivisionError Handling

This repository demonstrates a common Python coding error: a `ZeroDivisionError` that can occur when calculating the average of a list of numbers. The original code lacks proper handling for cases where the list is empty or contains only zeros. The solution adds robust error handling to prevent this error.

## Bug

The `bug.py` file contains the initial code with the error.  The code correctly handles an empty list, but fails when the sum of numbers is zero.

## Solution

The `bugSolution.py` file provides a corrected version of the code. This improved version explicitly checks for cases where the sum of numbers is zero and handles these scenarios gracefully, preventing the `ZeroDivisionError`.