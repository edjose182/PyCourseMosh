# Unit #2 : Primitive Types

## 1-Variables

The are primitive types of variable in python, these are:

* Numbers:

    ```python
        students_count = 1000 #Integer
        rating         = 4.99 #Float
    ```

* Booleans:

    ```python
        is_published = True #Boolean
    ```

* Strings

    ```python
        course_name = "Python Programming" #Strings
    ```

## 2-Variable Names

Considerations when you name a variable:

1. Use names easy to understand but with meaning
2. Use lower case to name you variables
3. Use underscore to sepate words
4. Use a space bewteen the name of the variables and the value

## 3-Strings

To create a string you have to use `""` (doble-quote). You can use `"""` (triples quotes) like is shown in the next example for long text with multiple lines:

```python
    """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque id dictum felis. Suspendisse non nisl malesuada, mattis urna lacinia, consectetur eros. Morbi sed auctor arcu. Nunc vitae tempor est, a fringilla magna. Suspendisse porttitor, odio in cursus efficitur, ligula ligula luctus purus, mattis ullamcorper nisi tortor vitae ex. Sed cursus leo vitae massa egestas, sit amet rutrum neque facilisis. Morbi non dolor mattis, maximus lacus id, suscipit orci."""
```

You can sue functions to manipulate the strings. Here is a list of functions to use:

* `len`: Returns the number of characters in a string

```python
course = "Python Programming"
print(len(course))
```

The `print` will return "18" characters.

To get access to a specific member of the string you have to use bracket notation.

```python
course = "Python Programming"
course[0] # Get the first character
print(course[0]) # Will print P
```

To slice strings you have to use a syntax similar to this one:

```python
course[0:3]
print(course[0:3]) # Will print Pyt
```

## 4-Escape Sequences

Python has some problems when you are workingg with some characters in the `""`.
For example:

```python
course = "Python "Programming" 
#Programming in not taken into account
```

Because of his you have to try diffent things. Here are a couple of options:

* Use single quote `''`. For example

```python
course = 'Python "Programming' 
```

* Use doble quote `""` and `\`

```python
course = "Python \"Programming" 
```

## 5-Formatted Strings

You can create string combinations with Python and you have 2 options to do it:

**Option #1**

```python
first = "Mosh"
last  = "Hamedani"
full  = first + " " + last #Concatenation
print(full) #Will print `Mosh Hamedani`
```

**Option #2**

```python
first = "Mosh"
last  = "Hamedani"
full  = f"{first} {last}" # Formatted string
print(full) #Will print `Mosh Hamedani`
```

## 6-String Methods

The strings counts with several methods to be used. Here are some examples of the methods you can use:

1. `upper`

    Convert a string into the upper case

```python
course = "Python Programming"
print(course.upper()) #Will print `PYTHON PROGRAMMING`
```

2. `lower`

    Convert a string into the lower case

```python
course = "Python Programming"
print(course.lower()) #Will print `python programming`
```

2. `title`

    Capitalize the first character

```python
course = "Python Programming"
print(course.title()) #Will print `Python Programming`
```

3. `strip`

    Delete white spaces in a string

```python
course = "    Python Programming"
print(course.strip()) #Will print `Python Programming`
```

4. `find`

    Find a specific character in a string. If found it will print the index. If not will print -1

```python
course = "    python programming"
print(course.find("pro")) #Will print 11 print `Python Programming`
```

5. `replace`

    Replace a specific character(s) in a string

```python
course = "python programming"
print(course.replace("p","j")) #Will print 11 print `jython jrogramming`
```

6. `in`

    It will print a `True` or `False` if the character is found.

```python
course = "python programming"
print("pro" in course) #Will print True
```

7. `not`

    The opposite to the previous method

```python
course = "python programming"
print("swift" not in course) #Will print True
```

## 7-Numbers

In python there are several types of numbers

1. Integer

```python

x = 1 

```

2. Float

```python

x = 1.1 

```

3. Complex

```python

x = 1 + 2j 

```

## 8-Working with Numbers

With the numbers we can use several functions, for example:

* `round`

Rounds the number

* `abs`

Gets the absolute value

Also we can import `math` to use more fuctions.

```python

import math

math.cos()
math.exp()
math.copysign()

```

## 9-Type Conversion

To get information from the user we can use the `input()` function. This function will expect a string.
We can convert the strings to numbers. Like is shown below:

```python
x = input("x: ")

int(x)   #Convert x to an int
float(x) #Convert x to a float
bool(x)  #Convert x to a bool 
str(x)   #Convert x to a string

# You can use the type function to get the type of a variable
type(x)  #Returns the tpe of x

# For the booleans it will exist some Falsy and Truly values

# Falsy
# ""
# 0 
# None

#Truly
#Any value different to the Falsy values
```

