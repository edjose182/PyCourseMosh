# U4- Functions

## 1- Defining Functions

A simple function will have th following format:

```python
def greet():
    print("Hi there")
    print("Welcome aboard")


greet()
```

## 2- Arguments

You can arguments to an function in python. Here is an example:

```python
def greet(first_name, last_name):
    print(f"Hello {first_name} {last_name}")
    print("Welcome aboard")


greet("Edgar", "Campos")
```

## 3- Type of functions

In programming there are two types of functions:

1. Perform a task
2. Return a value

Here is an example of thesecond case:

```python
def get_greeting(name):
    return f"Hi {name}"

message = get_greeting("Edgar")

print(message)
```

## 4- Key Arguments

We can write a program like this:

```python
def increment(number,by):
    return number + 1

result = increment(2,1)
print(result)
```

But we can simplify it:

```python
def increment(number,by):
    return number + 1

print(increment(number=2,by=1)) #This athe key arguments
```
