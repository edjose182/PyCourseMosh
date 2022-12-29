# U6-Exceptions

## 1-Exceptions

A exception is something that stops a jobs because of a programmets mistake for example.

Here is an example:

```python
list = [1,2]

print(list[3]) #This will print an error message
```

Here is the error message:

> Traceback (most recent call last):
>  File "C:\Users\campedga\Desktop\courses\PyCourseMosh\exceptions-u6\app.py", line 3, in <module>
>    print(list[3]) #This will print an error message
> IndexError: list index out of range

## 2-Handling Exceptions

Here is an example of how you can handle an error:

1. Error

Here is case of error. The program is expecting a integer but the user inputs a string.

```python
age = int(input("Age: "))
```

Here is the error message:

> Traceback (most recent call last):
>  File "C:\Users\campedga\Desktop\courses\PyCourseMosh\exceptions-u6\app.py", line 1, in <module>
>    age = int(input("Age: "))
>ValueError: invalid literal for int() with base 10: 'e'

2. Avoiding the error

To avoid an error it is possible to use the `try` and `except`.

```python
try:
    age = int(input("Age: "))
except ValueError:
    print("You didn't enter a valid age.")
```

In case a incorrect value is introduce the program will print the error message that we create.

There is a else clause that will only be excecuted if we don't have any exceptions.

```python
try:
    age = int(input("Age: "))
except ValueError:
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
```

The program will print: _No exceptions were thrown._

It is possible to print information about the error by using `as`.

```python
try:
    age = int(input("Age: "))
except ValueError as ex:
    print("You didn't enter a valid age.")
    print(ex)
    print(type(ex))
else:
    print("No exceptions were thrown.")
```

Here is the error message:

> You didn't enter a valid age.
>
> invalid literal for int() with base 10: 's'
>
> <class 'ValueError'>

## 3- Handling Different Exceptions

If we want to add a new operation to our previous program (`xfactor = 10 / age`) there is a limition with the age value.
If want to add more exceptions we have to do something similar to this:

```python
try:
    age = int(input("Age: "))
    xfactor = 10 / age

except ValueError:
    print("You didn't enter a valid age.")
except ZeroDivisionError:
    print("Age cannot be Zero.")
else:
    print("No exceptions were thrown.")
```

Now let's imagine if the user enters 0 fo the age you want to print the same message as if the user enters an invalid age.

Like this:

```python
try:
    age = int(input("Age: "))
    xfactor = 10 / age

except ValueError:
    print("You didn't enter a valid age.")
except ZeroDivisionError:
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
```

To not repeat the message , we can do this:

```python
try:
    age = int(input("Age: "))
    xfactor = 10 / age

except (ValueError,ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
```

## 4- Cleaning Up

In cases where you want to exexute something wheter the program found an exception or not, the best thing to do is to use the _finally_ clause.

Here is an example:

```python
try:
    file = open("app.txt")
    age = int(input("Age: "))
    xfactor = 10 / age

except (ValueError,ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
finally:
    file.close()
```

## 5- The With Statement

The _With_ stament is used to release automatically external resources (without using _Finally_).

If an object has the _enter_ and the _exit_ methods, python will automatically call the exit method and ther it will release external resourses, that is the reason we don't need a _Finally_ clause.

```python
try:
    with open("app.txt") as file:
        print("File opened.")
    
    age = int(input("Age: "))
    xfactor = 10 / age

except (ValueError,ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
```

If we are working with multiple external sources, we can try the following:

```python
try:
    with open("app.txt") as file, open("another.txt") as target:
        print("File opened.")
    
    age = int(input("Age: "))
    xfactor = 10 / age

except (ValueError,ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
```

## 6- Raising Exceptions

To raise an exception we can use _raise_ to indicate if something is wrong with our program.
We don't have to Python to report the error.
It is necessary to use the _exceptions_ to handle this in the program.

```python
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)
```

## 7- Cost of Raising Exceptions

When writing your on functions prefer not to raise exceptions, because these expections come with a cost.

`timeit` allow us to calculate the executation program in Python.
Here we are going to use it to see the cost of using exceptions in our functions:

```python
from timeit import timeit

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)
"""

print("First Code",timeit(code1,number=10000)) ##number tell how many times will
                                               ## repeat the operation
```

This is the response:

> Age cannot be 0 or less.
>
> Age cannot be 0 or less.
>
> Age cannot be 0 or less.
>
> Age cannot be 0 or less.
>
> Age cannot be 0 or less.
>
> Age cannot be 0 or less.
>
> First Code 1.1990610999055207

It takes 1.199 seconds to execute the program.

Now insted of priting the "error" message we are goin to use the _pass_ statement.

```python
from timeit import timeit

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""

print("First Code",timeit(code1,number=10000)) ##number tell how many times will
                                               ## repeat the operation
```

It takes 0.002303800079971552 seconds to execute the code