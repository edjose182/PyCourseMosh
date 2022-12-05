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

print(increment(number=2,by=1)) #This the key arguments
```

## 5- Default Arguments

We can set default values in the functions

```python
def increment(number,by=1):
    return number + 1

result = increment(2)
print(result) ##It will print 3
```

But if it pass an second argument de function will use the second arguemnt

```python
def increment(number,by=1):
    return number + 1

result = increment(2,5)
print(result) ##It will print 7
```

All default arguments should go after the require arguments.

## 6- xargs

In the cases where is necessary to use multiple arguments, it is useful to use _xargs_ (*args)

Here is a scenario

```python
def multiply(x,y)
    return x*y

multiply(2,3,4,5) #Only receives two arguments
```

The previous code it wont work.

Here is another way of implimenting this:

```python
def multiply (*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print(multiply(2,3,4,5)) #It will print 120
```

## 7- xxargs

This type of functions will create a dictionary:

```python
def save_user(**user):
    return user

print(save_user(id=1, name="Valery",age=27)) #It will print {'id': 1, 'name': 'Valery', 'age': 27}
```

## 8- Scope

In python you can have Local Variables and Global Variables

Example of a Local Variable:

```python
def greet():
    name = "Joe"
    print(name) # This is a local variable

greet()
```

Example of a Global Variable

```python
name = "Joe" #This is a local variable
def great():
    print(name)

greet()
```

If the code is write as is shown next

```python
name = "Joe" #This is a local variable
def great():
    
    name = "Peter"
    print(name)

greet() 
```

The function will print _Peter_. This is becuase python stores "Joe" in the space used for `name`.

To change it you can try this:

```python
name = "Joe" #This is a local variable
def great():
    global name #Indicates that we want to use the global variable
    name = "Peter" #It will modify the global variable
    print(name)

greet() 
```

The previous code will print _Peter_.
