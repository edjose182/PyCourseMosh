# Python Package Index

## 1- Pypi

Pypi or Python package index is like npm or node package manager for JS developers. It's basically a repository of python packages built by people that uses python on the daily basis.

You can find all the packages in the following link:[pypi.org](pypi.org)

## 2- Pip

To install a package you can use the `pip` tool. Now with this tool we an do various things such as installing packages, unstalling them, upgrading them, or listing the currently installed packages. Here a few examples:

- Install a package:
 
To install a package we use the following command:

```bash
pip install request 
```

- List packages install on the machine:

```bash
pip list
```

```text
Package            Version
------------------ ---------
appdirs            1.4.4
arandr             0.1.10
astroid            2.5.1
asttokens          2.2.1
automationhat      0.2.0
backcall           0.2.0
beautifulsoup4     4.9.3
```

- Install an early version:

To install an early version we can use a command similar to this one:

```bash
pip install requests==2.9.0
```

- Uninstall a package

```bash
pip uninstall requests
```

## 3- Virtual Environments

A virtual environment is a place where we can run the project but in a more general way (With thi the program or application is compatible with almost all the computers).

## 4- Pipenv

**pipenv** is a dependency manager for python projects, similar to _npm_ for _JS_. **pipenv** use env under the hood.

To be able to use **pipenv** is necessary to install the following package:

```bash
pip install pipenv
```

Now, instead of using `pip` to install packages, we are going to to use `pipenv`.

Like this:

```bash
pipenv install requests
```

The _virtual environment_ is not store in the project's folder. To find it we are going to use the following comman:

```bash
pipenv --venv
```

This is going to display the path of the virtual environment:

```text
/home/edjose2206/.local/share/virtualenvs/py-pkg-index-u10-8zQ37eSr
```

To activate the virtual environment, it's necessary to tun the following command:

```bash
pipenv shell
```

To deactivate it, use the next command on the terminal:

```bash
exit
```

## 5- Virtual Environments in VSCode

To this lectu, we are going to start using the following code:

```python
import requests

response = requests.get("http://google.com")
print(response)
```

To be able to run the code in virtual environment using VS code extension, it's necessary to have the _env_ path:

```bash
pipenv --venv
```

```text
/home/edjose2206/.local/share/virtualenvs/py-pkg-index-u10-8zQ37eSr
```

Now we use the `open` to open the folder:

```bash
open /home/edjose2206/.local/share/virtualenvs/py-pkg-index-u10-8zQ37eSr
```

On the _bin_ folder we have the "python3" file. We need to pass this file to the interpreter.

To do we can use the following command on VS code Command palate:

`Python: Select Interpreter`

And select the virtual environment path.

## 6-  Pipfile