## Control flow with if / else and Conditional Operators

```python 

if condition:
do this 
else:
do this

```
### Comparison Operators 

> Greater Than 
< Less Than 
>= Greater than or equal to 
<= Less than or equal to 
== Equal to 
!= Not Equal to 

### Nested if statements and elif statements 

> 120 cm 

<= 18 $ 7 

> 8 $ 12

< 12 "5$" 

12 - 18 "$7"

> 18 "$ 12"

#### Nested if / else

```python 

if condition:
    if another condition:
    do this 
else:
    do this

else:
    do this

```

### if / elif / else 

```python

if condition1:
    do A
elif condition2:
    do B
else : 
    do this 

```


# if / elif/ else - Multiple if 

```python
if condition1:
    do A
elif condition2:
    do B
else: 
    do C 
```
Only one condition is carried out 

```python
if condition1:
    do A
if condition2:
    do B
if condition3:
    do C
```

All 3 conditions can be carried out at once. 

#### In most programming languages, including Python, `if`, `elif` (else-if), and `else` statements are used for conditional branching. These statements allow you to execute different blocks of code based on specific conditions. Here is a breakdown of how they work:

### `if` statement:

- **Purpose**: Checks if a condition is `True`.
- **Syntax**:
  ```python
  if condition:
      # Code block to execute if the condition is True
  ```

### `elif` statement:

- **Purpose**: Checks another condition if the previous `if` or `elif` conditions were not met.
- **Syntax**:
  ```python
  elif another_condition:
      # Code block to execute if the another_condition is True
  ```
- **Note**: An `elif` statement must follow an `if` statement.

### `else` statement:

- **Purpose**: Executes a block of code if none of the above conditions are met.
- **Syntax**:
  ```python
  else:
      # Code block to execute if none of the above conditions are True
  ```

### Example:

Here is an example to demonstrate how `if`, `elif`, and `else` work together in Python:

```python
x = 10

if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is equal to 10")
else:
    print("x is less than 10")
```

In this example, the output will be "x is equal to 10" because that's the condition that is met.

### Conditions:

- Conditions should evaluate to either `True` or `False`.
- You can use relational operators (`<`, `>`, `==`, `!=`, `>=`, `<=`) to form conditions.
- Logical operators (`and`, `or`, `not`) can be used to combine conditions.

### When to use:

- Use `if` statements to check an initial condition.
- Use `elif` statements to check additional conditions after the initial `if`.
- Use `else` for all other scenarios when none of the above conditions are met.

Understanding the logic behind these conditional statements is crucial for computer science and will be particularly useful as you aspire to become a data scientist, where you'll need to implement various algorithms and data manipulations based on conditions.


### Logical Operators 


To check for multiple conditions using logical operators in the same line of code.

A and B
C or D
not E

Logical operators allow you to form more complex conditions by combining multiple conditions. In Python, the main logical operators are `and`, `or`, and `not`.

### `and` Operator

- **Purpose**: Checks that both conditions are `True`.
- **Syntax**:
  ```python
  if A and B:
      # Code block to execute if both A and B are True
  ```

### `or` Operator

- **Purpose**: Checks if at least one of the conditions is `True`.
- **Syntax**:
  ```python
  if C or D:
      # Code block to execute if either C or D is True
  ```

### `not` Operator

- **Purpose**: Negates a condition.
- **Syntax**:
  ```python
  if not E:
      # Code block to execute if E is False
  ```

### Example:

Here's an example that incorporates all these logical operators.

```python
A = True
B = False
C = True
D = False
E = False

# Using 'and' Operator
if A and B:
    print("Both A and B are True")
else:
    print("Either A or B is False")

# Using 'or' Operator
if C or D:
    print("Either C or D is True")
else:
    print("Both C and D are False")

# Using 'not' Operator
if not E:
    print("E is False")
else:
    print("E is True")
```

Understanding how to use logical operators effectively is a critical skill in computer science, especially for tasks such as decision-making algorithms and data filtering, which you'll encounter in your future career as a data scientist.