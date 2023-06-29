# Build Rules

This document outlines the build rules for our projects to ensure the highest level of reliability and safety. All projects should adhere to these rules to maintain a standard of quality that is on par with NASA's coding standards.

## 1. Code Reliability and Safety

- All code should be written with a focus on reliability and safety.
- Code should be deterministic, with no reliance on real-time operations.
- Avoid the use of dynamic memory allocation after initialization.
- All code must be compiled with all warnings enabled. Any piece of code that results in a warning must be revised.

## 2. Code Readability and Maintainability

- Code should be written to be easily read and understood by others.
- Use clear and descriptive names for variables, functions, and files.
- Use comments and docstrings to explain the purpose and functionality of your code.
- Follow the conventions for docstrings in Python (PEP 257).
- Code should be formatted consistently. Consider using a tool like `black` for Python to automatically format your code.

## 3. Code Structure and Complexity

- Code should be structured to minimize complexity.
- Avoid deep nesting of control structures (if/else statements, for loops, etc.).
- Keep functions and modules small and focused on a single task.
- Follow the Single Responsibility Principle.
- Avoid the use of global variables. Encapsulate state within classes or structures as much as possible.
- Avoid the use of function pointers. Use higher-level abstractions like classes and interfaces instead.

## 4. Error Handling and Exceptions

- Code should handle potential errors gracefully.
- Use exceptions to handle unexpected conditions.
- Check the return values of all functions and handle errors appropriately.
- All exceptions must be caught and handled. Uncaught exceptions should be considered a critical failure.

## 5. Testing and Code Coverage

- All code should be thoroughly tested to ensure its correctness.
- Strive for high code coverage in your tests, aiming to test all lines of code and all branches of control structures.
- Use automated testing tools and continuous integration to ensure that tests are run on every commit.
- All bugs found should result in a new test case to prevent regressions.

## 6. Code Reviews and Inspections

- All code should be reviewed by at least one other person before it is merged into the main codebase.
- Code reviews should check for potential issues, adherence to these build rules, and overall code quality.
- Use static analysis tools to automatically check for common issues and enforce coding standards.

## 7. Documentation

- All projects should include a README file that provides an overview of the project and explains how to install and use it.
- Include a LICENSE file that specifies the license under which your project is distributed.
- Include a CONTRIBUTING file that explains how others can contribute to your project.
- All public APIs should be documented. Include an example of how to use the API in the documentation.

By adhering to these build rules, we can ensure that our projects are reliable, safe, and of the highest quality. These rules are not exhaustive and may be updated as necessary to accommodate new practices and technologies.
