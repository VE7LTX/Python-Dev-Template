# Function Definition Rules

This document outlines the rules for defining functions in Python. Adhering to these rules will ensure that our functions are reliable, safe, and of high quality.

## 1. Function Naming

- Function names should be lowercase, with words separated by underscores as necessary to improve readability (PEP 8).
- Use clear, descriptive names for functions to indicate what the function does.
- Avoid using names that are too general or ambiguous.

## 2. Function Size

- Functions should be small and focused on a single task. As a general rule, if a function is more than 50 lines, it might be doing too much and should be split into smaller functions.
- Each function should do one thing and do it well, following the Single Responsibility Principle.

## 3. Function Parameters

- Limit the number of function parameters, ideally no more than three. Too many parameters can make a function difficult to understand and use.
- Use default arguments to make function calls more straightforward when certain values are commonly used.
- Avoid using mutable default arguments.
- Use keyword arguments to improve readability of function calls.

## 4. Docstrings

- Include a docstring at the start of the function to describe what the function does.
- The docstring should follow the conventions outlined in PEP 257. This includes having a one-line summary, a more detailed explanation, and sections for parameters, return value, and exceptions.
    - **One-line Summary**: The docstring should start with a one-line summary of the function's purpose. This line should begin with a capital letter and end with a period.
    - **Parameters Section**: This section should list each parameter by name, followed by its expected type in parentheses, and then its role in the function.
    - **Return Section**: This section should start with the word "Returns", followed by the type of the return value, and then a description of the return value.
    - **Exceptions Section**: This section should list all the exceptions that the function can raise, along with the conditions under which they are raised.
- The docstring should be written in the imperative mood, as if you are giving orders to the function.
- If the function is a generator, the docstring should also explain what the generator yields.

## 5. Return Statements

- Each function should have a clear and single return statement. Avoid multiple return statements if possible.
- Always specify a return value unless the function is intended to return None.
- Avoid using the `return` statement in a generator.

## 6. Error Handling

- Functions should handle potential errors gracefully and not fail silently.
- Use exceptions to handle unexpected conditions and to indicate errors.
- Do not use exception handling as a substitute for a regular control flow mechanism.
- Avoid catching general exceptions. Instead, catch specific exceptions that you can handle.

## 7. Function Complexity

- Avoid complex functions. A function should do one thing and do it well.
- If a function is becoming complex, consider breaking it down into smaller, more manageable functions.
- Avoid deep nesting of control structures (if/else statements, for loops, etc.).

## 8. Use of Global Variables

- Avoid using global variables in functions. Instead, pass the variables as parameters and return them if necessary.
- If you must use global variables, make sure to document them in the function's docstring.


## 9. Testing

- Write tests for your functions to ensure they work as expected in all scenarios.
- Use a unit testing framework like `unittest` or `pytest` to structure your tests.
- Strive for high code coverage in your tests, aiming to test all lines of code and all branches of control structures.

## 10. Type Annotations

- Consider using type annotations (Python 3.5 and later) to make your function signatures self-documenting and to enable better tooling.
- Use the `typing` module to specify complex types, such as `List[int]` for a list of integers.

## 11. Function Decorators

- Use function decorators sparingly and for a clear purpose, as they can make the code harder to understand.
- Document any decorators used in the function's docstring.

## 12. Recursion

- Use recursion judiciously, as Python has a limited recursion depth and it can lead to readability issues.
- Always define a base case for recursive functions.

## 13. Function Side Effects

- Avoid functions with side effects where possible. Functions should not modify global variables or change the state of the program outside of their scope.
- If a function must have side effects, they should be clearly documented in the function's docstring.

## 14. Consistent Return Types

- Functions should have consistent return types. A function should not return different types of values in different circumstances, as this can make the function confusing to use.

## 15. Use of `*args` and `**kwargs`

- Use `*args` and `**kwargs` sparingly. While they can make functions more flexible, they can also make the function interface less clear and harder to use.
- If you use `*args` or `**kwargs`, document clearly in the docstring what types of arguments are expected.

## 16. Function Cohesion

- Functions should exhibit high cohesion, meaning they should perform a single, well-defined task.
- Avoid "god" functions that perform multiple unrelated tasks.

## 17. Function Coupling

- Minimize the coupling between functions. Functions should not rely heavily on the internal workings of other functions.
- Use function parameters and return values to pass data between functions, rather than relying on shared global state.

By adhering to these function definition rules, we can ensure that our functions are reliable, safe, and of high quality. These rules are not exhaustive and may be updated as necessary to accommodate new practices and technologies.

