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

When we install `penv` two files are created:

1. Pipfile

2. Pipfile.lock

These two files are use to keep track of the dependecies of our project and their version.

If we open the _Pipfile_ we are going to see the following info:

```python
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
requests = "*"

[dev-packages]

[requires]
python_version = "3.9"
```

In this file we have 4 sections:

1. `source`: This section specifies the repo where these packages are downloaded from.

2. `dev-packages`: Here are list the packages that we use as part of our development (Only during the developemnt). Such as packets used for automatic testing.

3. `packages`: Here we can find the packages that our application is depend on. 

4. `requires`: Specifies the Python version that we need to run the code.

Now let's take a look to the _Pipfile.lock_ file:

```python
{
    "_meta": {
        "hash": {
            "sha256": "b8c2e1580c53e383cfe4254c1f16560b855d984fde8b2beb3bf6ee8fc2fe5a22"
        },
        "pipfile-spec": 6,
        "requires": {
            "python_version": "3.9"
        },
        "sources": [
            {
                "name": "pypi",
                "url": "https://pypi.org/simple",
                "verify_ssl": true
            }
        ]
    },
    "default": {
        "certifi": {
            "hashes": [
                "sha256:0f0d56dc5a6ad56fd4ba36484d6cc34451e1c6548c61daad8c320169f91eddc7",
                "sha256:c6c2e98f5c7869efca1f8916fed228dd91539f9f1b444c314c06eef02980c716"
            ],
            "markers": "python_version >= '3.6'",
            "version": "==2023.5.7"
        },
        "charset-normalizer": {
            "hashes": [
                "sha256:04afa6387e2b282cf78ff3dbce20f0cc071c12dc8f685bd40960cc68644cfea6",
                "sha256:04eefcee095f58eaabe6dc3cc2262f3bcd776d2c67005880894f447b3f2cb9c1",
                
            ],
            "markers": "python_full_version >= '3.7.0'",
            "version": "==3.1.0"
        },
        "idna": {
            "hashes": [
                "sha256:814f528e8dead7d329833b91c5faa87d60bf71824cd12a7530b5526063d02cb4",
                "sha256:90b77e79eaa3eba6de819a0c442c0b4ceefc341a7a2ab77d7562bf49f425c5c2"
            ],
            "markers": "python_version >= '3.5'",
            "version": "==3.4"
        },
        "requests": {
            "hashes": [
                "sha256:58cd2187c01e70e6e26505bca751777aa9f2ee0b7f4300988b709f44e013003f",
                "sha256:942c5a758f98d790eaed1a29cb6eefc7ffb0d1cf7af05c3d2791656dbd6ad1e1"
            ],
            "index": "pypi",
            "version": "==2.31.0"
        },
        "urllib3": {
            "hashes": [
                "sha256:61717a1095d7e155cdb737ac7bb2f4324a858a1e2e6466f6d03ff630ca68d3cc",
                "sha256:d055c2f9d38dc53c808f6fdc8eab7360b6fdbbde02340ed25cfbcd817c62469e"
            ],
            "markers": "python_version >= '3.7'",
            "version": "==2.0.2"
        }
    },
    "develop": {}
}

```

This is a _.json_ file with all dependecies that the application will need and it exact version.

In case you are working with a project that doesn't have virutal environment but it has the _Pipfile_ and the _Pipfile.lock_ you can use the following command to install all the dependencies:

```bash
pipenv install
```

After this we can check the virtual environment by using the following command:

```bash
pipenv --venv
```

The versions to be installed are specified in the _packages_ section from the _Pipfile_.

In some cases this could cause the virtual enviroment to use the latest version of the dependecies. But in case you were working with another version, this will be save in the _Pipfile.lock_.

To use these versions you have to run the following command:

```bash
pipenv install --ignore-pipfile
```

## 7- Managing the dependecies

Now, let's take a look to useful commands to manage the dependecies of our application.

1. `pipenv grap`: We can run this command to check all the downloaded modules and dependecies.

```text
Courtesy Notice: Pipenv found itself running within a virtual environment, so it will automatically use that environment, instead of creating its own for any project. You can set PIPENV_IGNORE_VIRTUALENVS=1 to force pipenv to ignore that environment and create its own instead. You can set PIPENV_VERBOSITY=-1 to suppress this warning.
requests==2.31.0
├── certifi [required: >=2017.4.17, installed: 2023.7.22]
├── charset-normalizer [required: >=2,<4, installed: 3.2.0]
├── idna [required: >=2.5,<4, installed: 3.4]
└── urllib3 [required: >=1.21.1,<3, installed: 2.0.4]
```

If we decided to uninstall the `requests` module, the dependecies will still be installed in the env.

However, if we take this project and put it on a different machine and install all these dependencies from scratch, these packages will not en up there, because will we have not referenced them in out pip file because we uninstalled `request`.

If we want to update all the packages we can use the following command:

```bash
pipenv update --outdated
```

This will update the packages to the latest version but this could be restricted by the version set on the _Pipfile_.

If we want to udpate a specific package we can use the following command:

```bash
pipenv update <package_name>
```

## 8- Publishing Packages

WIP

## 9- Docstrings

In Python we have a special format for documentating our code, called _docstring_ or documentation string. 

It's basically a string with triple quotes  (`"""`) that we add right after the declaration of a function or class or variable. This is different from using comments, because we should be using comments to explain why we have done things in a certain way.

Here is an example how document a module:

```python
""" This module provides functions to convert a PDF to text.""" 

def convert(path):
    """
    Convert the given PDF to text.

    Paramters:
    path (str): The Path to a PDF file.

    Returns:
    str: The content of the PDF file as text.
    """
    print("pdf2text")
```

```python
class Converter:
    """ A simple converter for converting PDFs to text."""

    def convert(self,path):
    """
    Convert the given PDF to text.

    Paramters:
    path (str): The Path to a PDF file.

    Returns:
    str: The content of the PDF file as text.
    """
    print("pdf2text")
```

## 10- Pydoc

In python we have a utility called _pydoc_ that comes with python installation. With this utility you can easily see the documentation for a module. That module can be on of the modules in Python standard library, or one of our own modules.

One terminal type pydoc:

```bash
pydoc math
```

With the previous command we can take a look at the documentation for the `Math` module for Python standard library.

```text
$ pydoc math
Help on built-in module math:

NAME
    math

DESCRIPTION
    This module provides access to the mathematical functions
    defined by the C standard.

FUNCTIONS
    acos(x, /)
        Return the arc cosine (measured in radians) of x.

        The result is between 0 and pi.

    acosh(x, /)
        Return the inverse hyperbolic cosine of x.

    asin(x, /)
        Return the arc sine (measured in radians) of x.

        The result is between -pi/2 and pi/2.

    asinh(x, /)
        Return the inverse hyperbolic sine of x.

    atan(x, /)
        Return the arc tangent (measured in radians) of x.

        The result is between -pi/2 and pi/2.
    
    atan2(y, x, /)
        Return the arc tangent (measured in radians) of y/x.

        Unlike atan(y/x), the signs of both x and y are considered.

    atanh(x, /)
        Return the inverse hyperbolic tangent of x.

    ceil(x, /)
        Return the ceiling of x as an Integral.

        This is the smallest integer >= x.

    comb(n, k, /)
        Number of ways to choose k items from n items without repetition and without order.

        Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
        to zero when k > n.

        Also called the binomial coefficient because it is equivalent
        to the coefficient of k-th term in polynomial expansion of the
        expression (1 + x)**n.

        Raises TypeError if either of the arguments are not integers.
        Raises ValueError if either of the arguments are negative.

    copysign(x, y, /)
        Return a float with the magnitude (absolute value) of x but the sign of y.

        On platforms that support signed zeros, copysign(1.0, -0.0)
        returns -1.0.

    cos(x, /)
        Return the cosine of x (measured in radians).

    cosh(x, /)
        Return the hyperbolic cosine of x.

    degrees(x, /)
        Convert angle x from radians to degrees.

-- More  --
```

We can use this command to print the information in a HTML file:

```bash
pydoc -w math
```