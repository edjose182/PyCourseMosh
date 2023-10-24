# Popular Python Packagaes

## 1- Introduction

In this unit we are goin to learn how to work with Excel Spreadsheets, PDFs, Sending Text, Browser Automation, Web Scraping, etc...
And this with the help of some packages.

## 2- What are APIs?

Mosst of the Web Pages make their data available with the help of the APIs (Application Programming Interfaces).

These APIs are endpoints that are publicly accessignle on the internet, so they have URL's just the websites themselves.

Here is an example.

From the **YELP** web page we have this API

```txt
GET https://api.yelp.com/v3/businesses/search
```

We can send an http request to this point to get a list of businesses that match some criteria.

## 3- Yelp API

There is a [Web Site](https://www.yelp.com/developers) in which we can find the the REST (Representational State Transfer) API used by YELP. This inside the **Yelp Fusion** section.

RESTI API is basically a bunch of conventions of rules and conventions that we have to follow to build or consume API's for exchanging data.

In this other [link](https://docs.developer.yelp.com/docs/fusion-intro) we can find the documentation about the API's used by Yelp Fusion.

For working with businesses for example we have endpoint for finding businesses by keyword, location, category or using a phone number, we also have an endpoint for getting details that we want for a particular business, or reviews, these are all business endpoints.

To get started we first need to create an app.

After we crete the app, we will have a client ID that uniquely identifies our application. This is like a user name for an application. We also have an API key, whicj is kind of like a password fo an application, we will lend this API key wheveer we want to talk to any of endpoints on Yelp, this is for security.
So Yelp wants to know who's calling theri API endpoints. With this basic information that we've provided at least we have contact information.

## 4- Searching for Businesses

We are going to start by creating a new project called **PYYELP**

![pyyelp_project](./images/pyyelp_project.PNG)

Now let's open up the terminal window and using pipenv install the requests package.

Before installing the packages , we need to install `pipenv`:

```bash
pip install pipenv
```

And after this we can install the requests package.

```bash
pipenv install requests
```

We use this package to send http requests.

```python
import requests

url = "https://api.yelp.com/v3/businesses/search"
api_key = "Dy6YtUIGTCaDBoUFuYJLU9HwOKqvPGQ579ky53jC4ffztIdFEQC_a2S9oqTrjQEbGJe3jNmwHcPLAuVJHzKlBK2poVgCaXiX5j-s8PlwE-omYdhYLjUfkmeIhCkeZXYx"
headers = {
    "Authorization":"bearer " + api_key
}
params = {
    "term":"Barber",
    "location":"NYC"
}
response = requests.get(url=url,headers=headers,params=params,verify=False)#False is used to fix an issue

#print(response.text)

result = response.json()
businesses = response.json()["businesses"]

for business in businesses:
    print(business["name"])

names = [business["name"] for business in businesses if business["rating"] > 4.5]

print(names)
```

It was necessary to add the `verify` parameter to avoid problems with the authentication.

## 5- Hiding API Keys

In the previous implmentation was stored the API key in the source code. There is a problem with this. If this code is added, to a version control system like git and publish in Github, this API key is visible to anyone who has access to that Github repository and that means they can create an application, a malicious application and use the API key to pretend to be us. That's not good. So if they violate any of the policies of Yelp, we'll be in trouble.

So to prevent this, it is necessary to extract the API key from the code and put itin a separeate file, and execute that file from git. Here is how:

1. Create a new file called _config.py_. In this file we'll have all kinds of configuration parameters for our application

2. Move the _API_ to the _config.py_ file

3. Include the `api_key` variable importing it from the _config.py_ module.

4. Exclude this from git. By adding _config.py_ file to the _.gitignore_ file.