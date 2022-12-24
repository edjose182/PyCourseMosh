# U5-Data Structures

## 1-Lists

To create a list you will have to "[ ]" (square brackets).

E.g.: `letters = ["a","b","c"]`

Here is an example of a list inside another list:

`matrix = [ [0,1] , [2,3] ]`

In this way ,you can repeat the iteam in a list:

```python
zeros = [0]*100 # It will generate a list
                  #of 100 columns
print(zeros) 
```

Also you can use the "+" symbol to combine lists:

For example:

```python
letters = ["a","b","c"]

zeros = [0]*5

combined = zeros + letters

print(combined) #[0, 0, 0, 0, 0, 'a', 'b', 'c']
```

You can also create a list in the following way:

```python
numbers = list(range(20))

print(numbers) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
```

You can create a list of strings with the "list" function. Here is an example:

```python
chars = list("Hello World!")

print(chars) #['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!']
```

## 2- Accesing items

You can access to a list in the following way:

```python
letters = ["a","b","c","d"]

print(letters[0]) #['a']
```

Modify an item in a list:

```python
letters = ["a","b","c","d"]

letters[0] = "A"

print(letters) #['A', 'b', 'c', 'd']
```

## 3- List Unpacking

You can assign values from a list to a variable(s) like is shown below:

```python
numbers = [1,2,3]

first = numbers[0]
seecond = numbers[1]
third = numbers[2]
```

But you can aso try it in this way:

```python
first, second, third = numbers
```

In ase you only want the first two elements you can use a syntax similar to this one:

```python
numbers = [1,2,3,4,5,6,7]

first, second, *others = numbers
```

## 4- Looping over Lists

Here is an example of how you can loop over a list:

```python
letters = ["a","b","c","d"]

for letter in letters:
    print(letter) # a b c d
```

If you want to use the index of the list you can try it as is shown next:

```python
letters = ["a","b","c","d"]

for letter in enumerate(letters):
    print(letter) # It will print a touple:
#(0, 'a')
#(1, 'b')
#(2, 'c')
#(3, 'd')
```

To get the index we can try the following:

```python
letters = ["a","b","c","d"]

for letter in enumerate(letters):
    print(letter[0]) # It will print:
#0
#1
#2
#3
```

We can unpack the the touples as follows:

```python
letters = ["a","b","c","d"]

for index, letter in enumerate(letters):
    print(index, letter) # It will print :
#0 a
#1 b
#2 c
#3 d
```

## 5- Adding or Removing items

You can use `.append()` to add an element in the end of a list:

```python
letters = ["a","b","c"]

letters.append("d")

print(letters) #['a', 'b', 'c', 'd']
```

To insert something in any position of the list you can use the `.insert()` function.

```python
letters = ["a","b","c"]

letters.insert(0,"1")

print(letters) #['-', 'a', 'b', 'c']
```

To removean item from the end of the list you can use `.pop()` method

```python
letters = ["a","b","c","d"]

letters.pop()

print(letters) #['a', 'b', 'c']

```

You can pass an index remove something from a specific index:

```python
letters = ["a","b","c","d"]

letters.pop(0)

print(letters) #['b', 'c', 'd']
```

You can use the `.remove()` method to delete an specific item:

```python
letters = ["a","b","c","d"]

letters.remove("b")

print(letters) #['a', 'c', 'd']
```

`del` will remove a range of elements:

```python
letters = ["a","b","c","d"]
del letters[0:3]
print(letters) #['d']
```

The method `.clear` will delete everything inside the list

```python
letters = ["a","b","c","d"]

letters.clear()

print(letters) #[]
```

## 6- Finding Items

To find the index of a specific item of the list you can use the `.index()` method

```python
letters = ["a","b","c"]
if "d" in letters:
    print(letters.index("d"))
```

Also you can use the method `.count()` to get the number of occurrences of the given item in a list.

## 7- Sorting Lists

To sort a list is it possible to use two methods:

* Use the method `.sort`

    This will sort the list and overwrite the varible with the sorted list

    ```python
    numbers = [3, 51, 2, 8, 6]
    numbers.sort()
    ```

    You can also sort the list in a reverse form

    ```python
    numbers = [3, 51, 2, 8, 6]
    numbers.sort(reverse = True)
    ```

* Use the `sorted()` function

    This function will sort the list momentary:

    ```python
    numbers = [3, 51, 2, 8, 6]
    sorted(numbers)
    ```

    It is possible to also get the reverse sorted list:

    ```python
    numbers = [3, 51, 2, 8, 6]
    sorted(numbers,reverse = True)
    ```

    Here is an example of a more complex list:

    ```python
    items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
    ]

    def sort_item(item):
        return item[1]

    items.sort(key=sort_item)

    print(items)
    ```

## 8- Lambda Functions

We can modify the previous code using lambda functions:

```python
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

items.sort(key=lambda item:item[1])

print(items)
```

## 9- Map Function

An example of this is that you want it to store the prices from one list into another list:

```python
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

prices = []

for item in items:
    prices.append(item[1])

print(prices)
```

But it is possible to write this code in another way:

```python
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

prices = list(map(lambda item:item[1],items))
print(prices)
```

* The `map` function will apply the lambda function to an iterable variable.
* The `map` function return a map object which is another iterable.
* The function `list()` is used to create a list

It is possible to access the information of that result as follows:

```python
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

x = map(lambda item:item[1],items)

for item in x:
    print item
```

## 10- Filter Function

To items that complete some specific conditions it is possible to use the `filter` function.

```python
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

filtered = list(filter(lambda item:item[1]>=10,items))

print(filtered)
```

## 11-List Comprehensions

You can use lists of comprehensions instead of the `map()` and `filter()` functions.
The adventages of using list comprehensions are more clear and easy to understand.

List comprehensions is **something you can only find in Python.** 

Here is an example of the equivalent to a `map()` function:

```python
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

prices = [item[1] for item in items]

         #`Expression` for `item` in `list` 

print(prices)
```

Here is an example of the equivalent to a `filter()` function:

```python
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

prices = [item for item in items if item[1] >= 10]

         #`Expression` for `item` in `list` if `filter` 

print(prices)
```

## 12- Zip Functions

The `zip()` function is used to combine the elements of different lists (or iterable variable)

```python
list1 = [1, 2, 3]
list2 = [10, 20, 30]

print(list(zip(list1,list2))) #[(1, 10), (2, 20), (3, 30)]
```

## 13- Stacks

This refers to the _LIFO_ (Last In - First Out). In python we can use a list object as a stack.

Here is an example:

```python
browsing_session = []

browsing_session.append("https://www.youtube.com/")
browsing_session.append("https://codepen.io/")
browsing_session.append("https://stackblitz.com/")

last = browsing_session.pop()  #It will remove the last item
                                #from list and return it

print(last)

print(browsing_session)
```

## 14- Queues

This referes to the _FIFO_ (First In - First Out). In python we can use dequeue object (is more efficent)

Here is an example:

```python
from collections import deque

queue = deque([]) # It is created an object

queue.append(1)
queue.append(2)
queue.append(3)

queue.popleft() # Removes the first Item on the left

print(queue)

if not queue: # This will print if the queue is empty
    print("empty")
```

## 15- Tuples

A tuple is basically a read only list. We can add new items, remove items or modigy items.

Here is an example:

```python
point = (1,2)
```

If we don't use the parenthesis python will interpretated as a tuple

```python
point = 1,2
```

## 16- Swapping Variables

To swap the value between variables you can try something like this:

```python
x = 10
y = 11

z = x

x = y
y = z

print("x",x)
print("y",y)
```

But you can get the same result without using a third variable, you can use tuple for this:

```python
x = 10
y = 11

x, y = (y,x)

print("x",x)
print("y",y)
```

## 17- Arrays

When you are working with a huge amount of sequences the best thing to do is to use array to get a good performance. To do it you have to import the _array_ object from the `array` module. To use this module it is important to define the type of the objects that you will use in your array ([typeCodesPython](https://www.educative.io/answers/what-are-type-codes-in))

```python
from array import array

numbers = array("i",[1,2,3])

numbers.append(4)

print(numbers)
```

## 18- Sets

It is basically a collection with no duplicates. _Sets_ are define with curly brackets (_{ }_).

Here is an example:

```python
numbers = [1,1,1,2,3,4,4,4,4]

uniques = set(numbers)

print(uniques) #{1, 2, 3, 4}
```

We can add, remove and modify items in a _set_.
Also it is possible to use several matemathical operations with set:

For example:

```python
numbers = [1,1,1,2,3,4,4,4,4]

first = set(numbers)

second = {1,5}

# To get the union of both sets

union = first | second

# To get the intersertion

inter = first & second

# To get the difference

diff = first - second
```

## 19- Dictionaries

There two of ways to create a dictionary.

1. Using curly brackets and keys:

    ```python
    point = {"x": = 1, "y": = 2}
    ```

2. Using the `dict()` function:

    ```python
    point = dict(x=1,y=2)
    ```

## 20- Dictionary Comprehensions

Similarly to the list, we can use Comprehensions for the dictionaries instead of using several lines of codes. Here is an example:

```python
values = {}

for x in range(5):
    values[x] = x*2

print(values) #{0: 0, 1: 2, 2: 4, 3: 6, 4: 8}
```

Instead of using the for loop, it is possible to create a Dictionary Comprehension:

```python
values = {x:x*2 for x in range(5)}

print(values) #{0: 0, 1: 2, 2: 4, 3: 6, 4: 8}
```

## 21- Generator Expressions

In the next code we created a list using a list comprehension expression and we iterate each item of the list and print it:

```python
values = [x*2 for x in range(10)]

for x in values:
    print(x)
```

But there cases where we want to use a bigger amount of data. For this cases it's better to use _Generators_.

_Generator_ objects are iterable so just like like list we can iterate over them.
Unlike list, they don't store the value in memory, They generate a new value in each iteration.

Here is an example that stores the values in memory:

```python
values = [x*2 for x in range(10)]

for x in values:
    print(x)
```

But if don't want to store these values in memory we can try using _( )_ instead of the _[ ]_

```python
values = (x*2 for x in range(10))

print(values) # This generate a generator object

for x in values:
    print(x)
```

To get the size of an object we can do this

```python
from sys import getsizeof

values = (x*2 for x in range(1000))

value_size = getsizeof(values)

print(value_size) #It takes 120 bytes of memory
```

## 22- Unpacking Operator

In cases where we don't want to get the info packed in a list, we can use a
unpacking operator to present the individual information:

```python
values = [1,2,3] 
print(values) #[1,2,3]
```

```python
values = [1,2,3] 
print(*values) # 1 2 3
```

Here is another example, instead of using the _list()_ function to create a list, we can use the unpacking operator:

* Using list funtion

```python
values_list = list(range(5))
```

* Using unpacking operator:

```python

values_unpack = [*range(5)]
```

With this we can create a list of several items:

```python
first = [1,2]

second = [3]

values = [*first,"a", *second,*"Hello"]

print(values) #[1, 2, 'a', 3, 'H', 'e', 'l', 'l', 'o']
```

This is also we can apply to dictionary:

```python
first = {"x": 1}

second = {"x": 10, "y": 2}

combined = {**first, **second, "z": 1}

print(combined) #{'x': 10, 'y': 2, 'z': 1}
```
