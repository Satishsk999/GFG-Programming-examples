"""
Author      : Satish Kumar
Created On  : 23.01.2026

Problem Statement : Given a string containing Python code, the task is to execute it dynamically.
Input: "x = 5\ny = 10\nprint(x + y)"
Output: 15

Approaches:
    1. Using exec()
        exec(code) executes the string code as Python code.
        Variables x and y are created, and their sum is printed.
    2. Using eval()
        eval() function can execute a single expression stored in a string and return its result.
        It is more limited compared to exec() but can be useful for evaluating expressions.

| Feature                      | `exec()` | `eval()` |
| ---------------------------- | -------- | -------- |
| Executes statements          | YES      | NO       |
| Evaluates expressions        | NO       | YES      |
| Returns value                | NO       | YES      |  for ex- exec("2 + 3")  # Does nothing
| Can define functions/classes | YES      | NO       |


"""

# Approach 1
code = "x = 5\ny = 10\nprint(x + y)"
exec(code)

# Approach 2
code = "5 + 10"
res = eval(code)
print(res)

