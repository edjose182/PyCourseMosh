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