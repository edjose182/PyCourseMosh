# Python Standard Library

## 1- Python Standard Library

Python has batteries included philosophy which means it comes with a comprehensive library of packages and modules that provide common feature that we need when bilding real applications. So in this section, we are going to explore python standard library more specifically, you are going to learn how to work with:

- Files

- SQLite

- Date/Time

- Random Values

- Emails

## 2- Working with paths

From the `pathlib` module you can import the `Path` class. This class will containt methods that we an use to access, create, rename and find folders.

```python
from pathlib import Path
```

`Path` is used to create an abosolute path, for example we create a path like this in Linux we have something like this:

```python
from pathlib import Path

Path(r'/home/edjose2206/Desktop/githubProjects/PyCourseMosh/py-standard-lib-u9')
```

`Path` can so be used to create relative paths. For example:

```python
Path("ecommerce/__init__.py")
```

We can also combine _path_ objects by using slash:

```python
Path() / Path("ecommerce")
```

Or we can also combine _path_ objects with strings:

```python
Path() / "ecommerce" / "__init__.py"
```

Here are a lsit of useful methods taht we can fin in the `Path` class:

- `home()`

It will return the user's home path.

```pyhon
Path.home()
```

- `exists()`

It will check if the paht exists.

```python
from pathlib import Path

path = Path("/home/edjose2206/Desktop/githubProjects/PyCourseMosh/py-standard-lib-u9/images")

path.exists() # True
```

- `is_file()`

Check if the path represents a file.

```python
from pathlib import Path

path = Path("/home/edjose2206/Desktop/githubProjects/PyCourseMosh/py-standard-lib-u9/images")

path.is_file() #False
```

- `is_dir()`

Check if the path represents a directory.

```python
from pathlib import Path

path = Path("/home/edjose2206/Desktop/githubProjects/PyCourseMosh/py-standard-lib-u9/images")

path.is_dir()
```

- `name`

Returns the name of the file.

```python
from pathlib import Path

path = Path("/home/edjose2206/Desktop/githubProjects/PyCourseMosh/py-standard-lib-u9/images/image.jpg")

print(path.name) #image.jpg
```

- `stem`

Returns the file name without the extension.

```python
from pathlib import Path

path = Path("/home/edjose2206/Desktop/githubProjects/PyCourseMosh/py-standard-lib-u9/images/image.jpg")

print(path.stem) #image
```

- `suffix`

Returns the file extension.

```python
from pathlib import Path

path = Path("/home/edjose2206/Desktop/githubProjects/PyCourseMosh/py-standard-lib-u9/images/image.jpg")

print(path.suffix) #jpg
```

- `parent`

Returns the parent folder.


```python
from pathlib import Path

path = Path("/home/edjose2206/Desktop/githubProjects/PyCourseMosh/py-standard-lib-u9/images/image.jpg")

print(path.parent) #/home/edjose2206/Desktop/githubProjects/PyCourseMosh/py-standard-lib-u9/images
```

- `with_name()`

Create a new path object based on this existing path but only change the name and the extension of the file.

```python
from pathlib import Path

path = Path("/home/edjose2206/Desktop/githubProjects/PyCourseMosh/py-standard-lib-u9/images/image.jpg")

print(path) #/home/edjose2206/Desktop/githubProjects/PyCourseMosh/py-standard-lib-u9/images/image.jpg


path = path.with_name("image_text.txt") 

print(path) #/home/edjose2206/Desktop/githubProjects/PyCourseMosh/py-standard-lib-u9/images/image_text.txt
```

- `absolute()`

It returns the absolute path.

```python
from pathlib import Path

path = Path("/home/edjose2206/Desktop/githubProjects/PyCourseMosh/py-standard-lib-u9/images/image.jpg")

print(path.absolute()) #/home/edjose2206/Desktop/githubProjects/PyCourseMosh/py-standard-lib-u9/images/image.jpg
```

- `with_suffix()`

It's used to change the extension of a file.

```python
from pathlib import Path

path = Path("/home/edjose2206/Desktop/githubProjects/PyCourseMosh/py-standard-lib-u9/images/image.jpg")

path = path.with_suffix(".txt") #/home/edjose2206/Desktop/githubProjects/PyCourseMosh/py-standard-lib-u9/images/image.txt

print(path)
```

## 3- Working with directories

Here there is a path object that represents a directory. 

```python
from pathlib import Path

path = Path("ecommerce")
```

Here is a list of methods that we can use to manage directories:

- `path.exists()`

- `path.mkdir()`

- `path.rmdir()`

- `path.rename()`

But there is another method called `iterdir()`. When the path points to a directory, yield path objects of the directory contents.

Here is an example:


```python
from pathlib import Path

path = Path("/home/edjose2206/Desktop/githubProjects/PyCourseMosh/py-standard-lib-u9/")

for i in path.iterdir():
    print(i)
```

This will return:

```text
/home/edjose2206/Desktop/githubProjects/PyCourseMosh/py-standard-lib-u9/app.ipynb
/home/edjose2206/Desktop/githubProjects/PyCourseMosh/py-standard-lib-u9/images
/home/edjose2206/Desktop/githubProjects/PyCourseMosh/py-standard-lib-u9/notes.md
```

The `iterdir()` is a generator object. Generator objects as the name implies, returns a new value every time we iterate. So when we are working with large list of items, instead of storing allthose items into memory, we use a generator object. We iterate it and get avalue everytime, this is more efficient. 

So that's the reason this method returns a generator object because when working with files and directories it is possible to have a directory with a million files in it.

Now, if you are working with a directory that doesn't have a million of directories inside of it, you can convert this generator to a list using a list comprehension expression. So instead of iterating over this generator we can use  list comprehension which is pretty similar to what we have here :

```python
from pathlib import Path

path = Path("/home/edjose2206/Desktop/githubProjects/PyCourseMosh/py-standard-lib-u9/")

paths_list = [i for i in path.iterdir()]

paths_dict = {i for i in path.iterdir()}

print(paths_list)

print(paths_dict)
```

```text
[PosixPath('/home/edjose2206/Desktop/githubProjects/PyCourseMosh/py-standard-lib-u9/app.ipynb'), PosixPath('/home/edjose2206/Desktop/githubProjects/PyCourseMosh/py-standard-lib-u9/images'), PosixPath('/home/edjose2206/Desktop/githubProjects/PyCourseMosh/py-standard-lib-u9/notes.md')]
```


We can take this to next level by adding filters. Here is an example:

```python
from pathlib import Path

path = Path("/home/edjose2206/Desktop/githubProjects/PyCourseMosh/py-standard-lib-u9/")

paths_list = [i for i in path.iterdir() if i.is_dir()]

print(paths_list)
```

```text
[PosixPath('/home/edjose2206/Desktop/githubProjects/PyCourseMosh/py-standard-lib-u9/images')]
```

Only stores the directories in the array.

There is another method called `glob()` which can be use it to look for files using a patern.
Here is an example:

```python
from pathlib import Path

path = Path("/home/edjose2206/Desktop/githubProjects/PyCourseMosh/py-standard-lib-u9/")

md_files = [i for i in path.glob("*.md")]

print(md_files)
```

```text
[PosixPath('/home/edjose2206/Desktop/githubProjects/PyCourseMosh/py-standard-lib-u9/notes.md')]
```

To search recursevily we have to use `rglob()`. This will give us the folders and their childrens.

## 4- Working with Files

There are some useful methods to use when you are working with files, here is a list of methods that you can use:

- `exists()`

It will tell if a specific file exists in a given path.

```python
from pathlib import Path

path = Path("/home/edjose2206/Desktop/githubProjects/PyCourseMosh/py-standard-lib-u9/app.ipynb")

path.exists() #True
```

- `rename()`

It allows to rename a given file.

```python
from pathlib import Path

path = Path("app.ipynb")

path.rename("app.py")
```

- `unlink()`

You can delete a file by using the `unlink()` method.

```python
from pathlib import Path

path = Path("app.ipynb")

path.unlink("app.py")
```

- `stat()`

It will return a file information.

```python
from pathlib import Path

path = Path("app.ipynb")

path.stat()
```

To print human readable time it is necesary to use the ctime library.

```python
from pathlib import Path

from time import ctime

path = Path("app.ipynb")

print(ctime(path.stat().st_ctime)) #This is the creation time
```

- `read_bytes()`

Returns the content of the fileas bytes object when representing binary data.

```python
from pathlib import Path

from time import ctime

path = Path("notes.md")

file_data = path.read_text()

print(file_data)
```

- `read_text()`

Returns the content of the file as a string.

```python
from pathlib import Path

from time import ctime

path = Path("notes.md")

file_data = path.read_text()

print(file_data)
```

- `write_text`()

This method is use it to write data to a file.

### Copy a file

To copy a file, the best thing to do is to use the shell utilities. This module combines a number of high level operations for copying and moving files. 

``` python
import shutil
```

## 5- Working with ZIP files

To create a _zip_ file we can do something similar to this:

```python
from pathlib import Path
from zipfile import ZipFile

zip = ZipFile("files.zip","w") #Create a zip file object. The "w" is to write

for path in Path("images").rglob("*.*"): #The rglob return an object that can be
    zip.write(path)                      #iterate it
zip.close()
```

The previous code can be written as follows:

```python
from pathlib import Path
from zipfile import ZipFile

with ZipFile("files.zip","w") as zip: #Create a zip file object. The "w" is to write
    for path in Path("images").rglob("*.*"): #The rglob return an object that can be
        zip.write(path)                      #iterate it
```

To read the _zip_ file we can use the following code:

```python
from pathlib import Path
from zipfile import ZipFile

with ZipFile("files.zip") as zip:
    print(zip.namelist()) #Return a list with all the files inside the .zip file
```

To extract all the files from the _zip_ file we can use the `extract()` method:

```python
from pathlib import Path
from zipfile import ZipFile

with ZipFile("files.zip") as zip:
     zip.extractall("extracted_files")
```

## 6- Working with CSV Files

To create or read a _csv_ file we can use the csv module. Here is an example of how you can create a _csv_ file:

```python
import csv

with open("data.csv","w") as file:
    writer = csv.writer(file)
    writer.writerow(["Transaction_ID","Price","Amount"])
    writer.writerow([1000,1,5])
    writer.writerow([1001,2,15])
```

To read the _csv_ file it is necessary to use the `reader` method.

```python
import csv

with open("data.csv") as file:
    reader = csv.reader(file)
    print(list(reader))
```

Something important to take into account is that the numbers are expresed as **strings** an to be used as strings is necessary to use change them manually.

The result from the reader method is iterable but you only can iterates the result once.

```python
import csv

with open("data.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
    #print(list(reader))
```


## 7- Working with JSON Files

Here is an example of how to create a **JSON** structure on python:

```python
import json

movies = [
    {"id": 1, "title": "Terminator", "year": 1989},
    {"id": 2, "title": "Kindergarten Cop", "year": 1993}
]

data = json.dumps(movies)

print(data)
```

To create the _json_ file we need to use the `Path` object:

```python
import json
from pathlib import Path

movies = [
    {"id": 1, "title": "Terminator", "year": 1989},
    {"id": 2, "title": "Kindergarten Cop", "year": 1993}
]

data = json.dumps(movies)

print(data)

Path("movies.json").write_text(data)
```

To read the data from a _json_ file it is necessary to use the `loads` method:

```python
import json
from pathlib import Path

data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies)
```

## 8- Working with SQLite Database

SQLite is a very lightweight database that we use for storing data on an application. It's often technology of choice for small applications like apps that we run on phones and tablets. So it allows us to easily store our data in a strcuture format with a table of rows and columns.

Let's write the code to create a DB to store the info inside the `movies.js` file.

```python
#Imports
import sqlite3
import json
from pathlib import Path

#Extract json file info into the movies variable
data = Path("movies.json").read_text()
movies = json.loads(data)

#Create database
with sqlite3.connect("db.sqlite3") as conn: #This opens the database
    command = "INSERT INTO Movies VALUES (?,?,?)" #Info is stored in a table
                                                  #called Movies. The ? in
                                                  #the command are place
                                                  #holders for the value
                                                  #to supply to the table
    for movie in movies:
        conn.execute(command,tuple(movie.values()))
        print(tuple(movie.values()))
    conn.commit() # This closes the database

    #This will print an error because there isn't a table called Movies
```

To create the table, it is necessary to use the SQLite program. Here is the link with the `.exe` that you can use to install it: [SQLite_download](https://sqlitebrowser.org/dl/)

After creating the Table we should be able to write the info into the DB.

To read the information in the database we will use the following code:

```python
#Read the database
with sqlite3.connect("db.sqlite3") as conn: #This opens the database
    command = "SELECT * FROM Movies" #Info is stored in a table
                                                  #called Movies. The ? in
                                                  #the command are place
                                                  #holders for the value
                                                  #to supply to the table
    cursor = conn.execute(command) #cursor is a iterable variable
    for row in cursor:
        print(row)

#(1, 'Terminator', 1989)
#(2, 'Kindergarten Cop', 1993)
```

## 9- Working with Timestamps

THere are two modules that we can use to work with dates and times. 

- `datetime`: It gives us date/time objects with attributes like year, month, and so on.

- `time`: It will give us methods to work with time.

### time

Th time module can be used to get the time at the moment when the `time()` method is called. Here is an example:

```python
#Imports
import time
print(time.time())
#1683500116.1324465
```

The timestamp _1683500116.1324465_ in human date is equal to: 

```text
Assuming that this timestamp is in seconds:
GMT: Sunday, May 7, 2023 10:55:16.132 PM
Your time zone: Sunday, May 7, 2023 5:55:16.132 PM GMT-05:00 DST
Relative: 2 minutes ago
```

Here is a on-line tool that converts the timestamp to human date: [timestamp_converter](https://www.epochconverter.com/)

## 10- Working with DateTimes

### datetime()

To use the _datetime_ it is necessary to call the `datetime` module. To create _datetime_ objects we will count with two approaches:

You can pass the year, month and the date. And optionally we can pss the hour minute and second as well. Here is an example:

```python
#Imports
import datetime

datetime.datetime(2023,4,7)

print(datetime) # This return a datetime object
```

To clear the code a little bit, we can modify the code as follows:

```python
#Imports
from datetime import datetime

datetime(2023,4,7)

print(datetime)
```

With these changes is not necessary to use the `datetime.datetime` notation.

### now()

There is another function called `now` that will return a _datetime_ object with the current time.

```python
#Imports
from datetime import datetime

now = datetime.now()

print(now) #2023-05-07 18:16:25.791577
```

### strptime()

We can also find the `strptime` method. This method is for parsing or converting a date time string. This is particulary useful when we get inout from the useror read it from the file. In both thesee scenarios we're dealing with strings. So our date time values are represented on strings, and we need to convert them to date time objects.

Here is an example:

```python
#Imports
from datetime import datetime

date_str = "2023/5/7"

date_obj = datetime.strptime(date_str,"%Y/%m/%d")

print(date_obj)
```

We used the second argumet `"%Y/%m/%d"` to tell **python** how to parse the values on the date.

### fromtimestamp()

We can also conver _timestamp_ objects to _datetime_ objects. To do it we have to use the `fromtimestamp()` method.

Here is an example:

```python
#Imports
from datetime import datetime
import time

dt = datetime.fromtimestamp(time.time())

print(dt) #2023-05-07 18:34:54.064333
```

### strftime()

The `strftime()` method is use to convert _datetime_ objects to strings.

Here is an example:

```python
#Imports
from datetime import datetime
import time

dt = datetime.fromtimestamp(time.time())

print(dt.strftime("%Y/%m")) #2023/05
print(dt.strftime("%Y/%m/%d")) #2023/05/07
```

## 11- Working with Time Deltas

Inside the `datetime` class, exists the `timedelta` class. This calss is uses to calculate the duration between two _datetime_ objects. Here is an example: 

```python
#Imports
from datetime import datetime, timedelta

dt1 = datetime(2018,1,1)
dt2 = datetime.now()

duration = dt2 - dt1

print(duration) #1952 days, 18:45:25.445932
```

Now this _timedelta_ object has a few interesting attributes, we have for example `days`. This will return the days value.

Also we have `seconds`, it will return the seconds.

```python
#Imports
from datetime import datetime, timedelta

dt1 = datetime(2018,1,1)
dt2 = datetime.now()

duration = dt2 - dt1

print("days {0}".format(duration.days)) # Days value
print("seconds {0}".format(duration.seconds)) # Seconds value
```

## 12- Generating Random Values

To randomize value sin python we can use the `random` module.

### random()

Generates a valu between 0 and 1.

```python
import random
print(random.random()) #0.056527554795549384
```

### randint()

Generates a value between _x_ and _y_ (`random.randint(x,y)`).

```python
import random
print(random.randint(1,10)) #9
```

### choice()

Randomly picks one value from an array.

```python
import random
print(random.choice([1,2,3,4])) #4
```

### choices()

Select multiple values from an array.

```python
import random
print(random.choices([1,2,3,4],k=2)) #[3, 4]
```

`k` is the number of elements to be pick.

We can use `choices` to generate a random password:

```python
import random
print("".join(random.choices("abcdef123456",k=4)))#b442
```

If want have more options create a better password we can use the `string` module. This module counts with some methods that can be used the generate a list of strings with all the ascii characters or numbers.

```python
import random
import string

print("".join(random.choices(string.ascii_letters + string.digits,k=8)))
```

### shuffle()

There is also another useful method for shuffling an array. The `shuffle()` method will randomize the order of elements in the array.

```python
import random
import string

arr = [1,2,3,4,5,6]

random.shuffle(arr)

print(arr) #[3, 4, 1, 6, 5, 2]
```

## 13- Opening the Browser

To deploy a browser it is necessary to use the `webbrowser` module.

```python
import webbrowser

print("Deployment completed")

webbrowser.open("http://google.com")
```

## 14- Sending Emails

We need to import a couple of classes to abe to send a e-mail. 1 to create the e-mail message, and the other to connect with a mpa server for sending e-mails.

To create the message we have to use `e-mail` module.

```python
from email.mime.multipart import MIMEMultipart
```

MIME stands for: Multipurpose Internet Mail Extensions. And this is the standar that defines the format for e-mail messages. This has nothing to do with python, it's purely a standard ofr defining the format of emails. In this package we have another sub-package that is multi part that exposes a class called `MIMEMultipart`.
With this object the email message that includes both HTML and plain text content. So when the email clientof the receiver receives this email message if it supports TML it will render the HTML content, otherwise it will render plain text content. 

```python
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

message = MIMEMultipart() #Create an object
message["from"] = "Edgar Campos"
message["to"] = "edjose2206@gmail.com"
message["subject"] = "This is a test"
message.attach(MIMEText("Body"))

with smtplib.SMTP(host="edjose182.gmail.com",port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("edjose182@gmail.com","Bass2206")
    smtp.send_message(message)
    print("Sent...")
```

If we want to attach image we can modify the code as is shown below:

```python
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import  Path
import smtplib

message = MIMEMultipart() #Create an object
message["from"] = "Edgar Campos"
message["to"] = "edjose2206@gmail.com"
message["subject"] = "This is a test"
message.attach(MIMEText("Body"))
message.attach(MIMEImage(Path("image1.png").read_bytes()))

with smtplib.SMTP(host="edjose182.gmail.com",port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("edjose182@gmail.com","Bass2206")
    smtp.send_message(message)
    print("Sent...")
```

## 15- Templates (emails)

In the last lecture, we added the body of our email like this:
```python
message.attach(MIMEText("Body","plain"))
```

But in real world applications the body of an email cam be several lines of text, you don't want to write all that text here.
Quite often that text is put in a separate file as a template. And we use HTML to build that template.

```python
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import  Path
from string import Template
import smtplib

template = Template(Path("template.html").read_text())
template.substitute()

message = MIMEMultipart() #Create an object
message["from"] = "Edgar Campos"
message["to"] = "edjose2206@gmail.com"
message["subject"] = "This is a test"
body = template.substitute({"name":"John"})
message.attach(MIMEText(body,"html"))
message.attach(MIMEImage(Path("image1.png").read_bytes()))

with smtplib.SMTP(host="edjose182.gmail.com",port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("edjose182@gmail.com","Bass2206")
    smtp.send_message(message)
    print("Sent...")
```

## 16- Command-line Arguments

You might want to create a python program that expands command line arguments.

Like this `app.py -a -b -c`

To do it we need to import the `sys` module. From this module we can use the `argv` method that will return a list with the arguments that we passed to the program.

```python
#We run this on the terminal: python3 app.py -a -b -c

import sys

print(sys.argv)
```

This is the resul that we got:

```text
['app.py', '-a', '-b', '-c']
```

We can try something interesting with this:

```python
import sys

print(sys.argv)

if len(sys.argv) == 1:
    print("USAGE: python3 app.py <password>")

else:
    password = sys.argv[1]
    print("Password", password)
```

## 17- Running External Programs

We can use python to run external programs, for this we can use the `subprocess` module.
A process is basically an instanceprogram. So with this module, we can run another programs. NOw in this module, there are a bunch of functions or methods. Like `call`, `check_call`, `check_output` and so on. All these methods are helper methods to create an instance of the _Popen_ class process. 

Now, these methods have been around for a long time, and they're kind of considered legacy, there is a newer method, and that is the preferred approach, to create an instance of the _Popen_ class.
That method is called `run`.

The first argument of this method is an array of elements.
Here is an example:

```python
import subprocess

subprocess.run(["ls","-l"])
```

```text
-rw-r--r-- 1 edjose2206 edjose2206  7284 May 22 21:48 app.ipynb
-rw-r--r-- 1 edjose2206 edjose2206   163 May 18 22:29 app.py
-rw-r--r-- 1 edjose2206 edjose2206    50 Apr 23 19:39 data.csv
-rw-r--r-- 1 edjose2206 edjose2206  8192 May  7 17:39 db.sqlite3
-rw-r--r-- 1 edjose2206 edjose2206    22 Apr 23 19:18 files.zip
drwxr-xr-x 2 edjose2206 edjose2206  4096 Apr 15 16:53 images
-rw-r--r-- 1 edjose2206 edjose2206   172 May  7 17:39 movies.json
-rw-r--r-- 1 edjose2206 edjose2206 23407 May 18 22:29 notes.md
-rw-r--r-- 1 edjose2206 edjose2206   126 May 18 21:59 template.html
```

In the first element of the array we pass the _command_ and in the other elements we pass the _arguments_.

We can get more information about the `subproces`

```python
import subprocess

completed = subprocess.run(["ls","-l"])
print("args",completed.args)
print("returncode",completed.returncode)
print("stderr",completed.stderr)
print("stdout",completed.stdout)
```

`args` is an array that includes the command that we execute.

`returncode` is zero, which means success, any none zero values indicates an error.

`stderr` is equal None because we don't have any errors.

`stdoutput` is also None because we are not capturing the output, the output is automatically printed on the terminal.

<!-- Min 4-->

To save/use the result from a command that we just use, it is possible to use the following option.

The `run()` method takes quite a few keywrods arguments and all of these have default values, the one we're going to use now is capture output.

```python
import subprocess

completed = subprocess.run(["ls","-l"],capture_output=True)
print("args",completed.args)
print("returncode",completed.returncode)
print("stderr",completed.stderr)
print("stdout",completed.stdout) # In the sldout is store the information
                                 # But it is store in a binary format
```

```text
args ['ls', '-l']
returncode 0
stderr b''
stdout b'total 64\n-rw-r--r-- 1 edjose2206 edjose2206  1776 May 29 19:35 app.ipynb\n-rw-r--r-- 1 edjose2206 edjose2206   163 May 18 22:29 app.py\n-rw-r--r-- 1 edjose2206 edjose2206    50 Apr 23 19:39 data.csv\n-rw-r--r-- 1 edjose2206 edjose2206  8192 May  7 17:39 db.sqlite3\n-rw-r--r-- 1 edjose2206 edjose2206    22 Apr 23 19:18 files.zip\ndrwxr-xr-x 2 edjose2206 edjose2206  4096 Apr 15 16:53 images\n-rw-r--r-- 1 edjose2206 edjose2206   172 May  7 17:39 movies.json\n-rw-r--r-- 1 edjose2206 edjose2206 25742 May 29 19:29 notes.md\n-rw-r--r-- 1 edjose2206 edjose2206   126 May 18 21:59 template.html\n'
```

To convert the binary to a string we have to pass another argument to the method.

```python
import subprocess

completed = subprocess.run(["ls","-l"],
                           capture_output=True,
                           text=True) #Converts Binary to string
print("args",completed.args)
print("returncode",completed.returncode)
print("stderr",completed.stderr)
print("stdout",completed.stdout) 
```

```text
args ['ls', '-l']
returncode 0
stderr 
stdout total 64
-rw-r--r-- 1 edjose2206 edjose2206  1860 May 29 19:37 app.ipynb
-rw-r--r-- 1 edjose2206 edjose2206   163 May 18 22:29 app.py
-rw-r--r-- 1 edjose2206 edjose2206    50 Apr 23 19:39 data.csv
-rw-r--r-- 1 edjose2206 edjose2206  8192 May  7 17:39 db.sqlite3
-rw-r--r-- 1 edjose2206 edjose2206    22 Apr 23 19:18 files.zip
drwxr-xr-x 2 edjose2206 edjose2206  4096 Apr 15 16:53 images
-rw-r--r-- 1 edjose2206 edjose2206   172 May  7 17:39 movies.json
-rw-r--r-- 1 edjose2206 edjose2206 25742 May 29 19:29 notes.md
-rw-r--r-- 1 edjose2206 edjose2206   126 May 18 21:59 template.html
```

As another example we are going to run another python script:

```python
import subprocess

completed = subprocess.run(["python3","another.py"],
                           capture_output=True,
                           text=True) #Converts Binary to string
print("args",completed.args)
print("returncode",completed.returncode)
print("stderr",completed.stderr)
print("stdout",completed.stdout) 
```

It is important to mention that we are running the seond script as a child process so the memory space used for each script will be different. Because of this won't use the same variables or info.

If want to check for an error on the command, it is possible to use the `check` argument to see if there is an error and also this will trigger an exeception.

```python
import subprocess

completed = subprocess.run(["false"],
                           capture_output=True,
                           text=True,
                           check=True)# Check if there is an error in the process
print("args",completed.args)
print("returncode",completed.returncode)
print("stderr",completed.stderr)
print("stdout",completed.stdout) 
```

```vbnet
---------------------------------------------------------------------------
CalledProcessError                        Traceback (most recent call last)
Cell In[5], line 3
      1 import subprocess
----> 3 completed = subprocess.run(["false"],
      4                            capture_output=True,
      5                            text=True,
      6                            check=True)# Check if there is an error in the process
      7 print("args",completed.args)
      8 print("returncode",completed.returncode)

File /usr/lib/python3.9/subprocess.py:528, in run(input, capture_output, timeout, check, *popenargs, **kwargs)
    526     retcode = process.poll()
    527     if check and retcode:
--> 528         raise CalledProcessError(retcode, process.args,
    529                                  output=stdout, stderr=stderr)
    530 return CompletedProcess(process.args, retcode, stdout, stderr)

CalledProcessError: Command '['false']' returned non-zero exit status 1.
```


Here is another way of writting the code:

```python
import subprocess

try:
    completed = subprocess.run(["false"],
                               capture_output=True,
                               text=True,
                               check=True)# Check if there is an error in the process
    print("args",completed.args)
    print("returncode",completed.returncode)
    print("stderr",completed.stderr)
    print("stdout",completed.stdout)

except subprocess.CalledProcessError as ex:
    print(ex)
```
