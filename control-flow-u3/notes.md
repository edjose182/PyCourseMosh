# U3-Control Flow

## 1-Comparison Operators

Examples:

```python
# Numbers
10 > 3 #True
10 >= 3 #True
10 < 20 #True
10 <= 20 #True
10 == 10 #True
10 == "10" #False
10 != "10" #True

# Strings
"bag" > "apple" #True
"bag" == "BAG"  #False
```

## 2-Conditional Statements

Example:

```python
temperature = 15

if temperature > 30:
    print("It's warm")
    print("Drink water")

elif temperature > 20:
    print("It's nice")

else:
    print("It's cold")

print("Done")
```

## 3-Ternary Operator

We can use the _Ternary Operators_ to create conditional statements, here is an example:

**Using:** `if` and `else`

```python
age = 22
if age >= 18:
    print("Eligible")
else:
    print("Not eligible")
```

**Using:** _ternary operators_

```python
age = 22

message = "Eligible" if age >= 18 else "Not eligible"

print(message)
```

## 4- Logical Operators

The operators are `and`, `or` and `not`
Example:

```python
high_income = True
good_credit = True

if high_income and good_credit:
    print("Eligible")
else:
    print("Not eligible")
```

## 5- Short-circuit Evaluation

The evaluation stops once of the argument fullfil the conditions of the Logical Operator

## 6- Chaining Comparison Operators

Example:

* Condition using logical operators

```python
# age should be between 18 and 65
age = 22
if age >= 18 and age < 65:
    print("Eligible")
```

* Condition using chaining comparison operators

```python
# age should be between 18 and 65
age = 22
if 18 <= age < 65:
    print("Eligible")
```

## 8- For Loops

Examples:

* Example #1

```python
for number in range(1,4): # The interation starts at 1 
                          # and finish before 4
    print("Attempt", number, (number) * ".")
```

## 9- For...Else

If it isn't necessary to go through all the cycle there is an option to stop the For loop.

```python
successful = True
for number in range(3):    
    print("Attempt")
    if successful:
        print("Successful")
        break # This stops the for loop
```

In case the loop doesn't stop before iterations we can use a else statement to do another action

```python
successful = False
for number in range(3):    
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")
```

## 10- Nested Loops

Example:

```python
for x in range(5):
    for y in range(3):
        print(f"({0},{y})")
```

## 11- Iterables

Python counts with Iterable types. `range()`, list and strings are two examples of it.

## 12- While Loops

Example:

```python
command = ""
while command != "quit":
    command = input(">")
    print("ECHO", command)
```

## 13- Inifinite Loops

Example:

```python
while True:
    command = input(">")
    print("ECHO ", command)
    if command.lower() == "quit":
        break
```

##
