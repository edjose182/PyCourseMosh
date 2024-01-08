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

## 6- Sending Text Messages

[Twilio](www.twilio.com) is a very popular communication platform for adding voice, video and messaging to your applications. For example, you can quickly make and receive video calls, send text messages and this is parituclary useful for confirming reservations, sending appointment reminders ot promotions, the possibilities are endless.
They provide an API is perfectly documented and super easy to use. So, we can directly communicate with this API by sending an http requets using the request model. But you they also provide a library that we can install using pip or pipenv this library is essentially a wrapper around the API so it gives us objects and these objects encapsulate all that http communication. So we no longer have to work at a low level of sending http requests to twilio API. We work at ahigher level and more abstract and simplified fashion.

There are objects, these objects have methods, we call them and they in turn, will take care of sending the right http requests to Twilio API. The first thing to do is create a Twilio account.

After creating the account we cereate phone number using the web page. Once we hve the number we can do the following:

1. Create a new project and called "PyText"

2. Create an app to send messages

```python
from twilio.rest import Client

client = Client(account_sid,auth_token)
client.messages.create(
    to="+50688473578",
    from_="+16562184241",
    body="Hello Mate"
)
```

## 7- Web Scraping

Not every website has an _API_ for us to work with. So in situations like that, the only way to tge the data we want is to parse the HTML behin the web page, get rid of all the HMTL tags, and extract the actual data, this technique is called **Web Scraping**. So we scrape all the html tagas and get hte actual data that we want.
In this lecture we are going to write a program that will extract a list of new list questions on stack overflow.com. We refer to this kind of program as a Web crawler or a Web Spider.
For this we are going to create a new project (folder) called _PyCrawler_.

In this new project we are going to install the following package:

```bash
pipenv install beautifulsoup4
```

This is a very popular Python package for extracting information from HTML and XML files.

We also need to install the requests module to download the Web page that contains the newest questions from Stack Overflow.

```bash
pipenv install requests
```

After this we create a file called _app.py_. So the first step is to download the Webpage that contains the newest questions.
(check the _app.py_ to read more about the next steps.)

If we right click on the first question and select inspect it, we are going to see something like this:

![webpage_html_view](./images/webpage_html_view.PNG)

In here we have an anchor that containts the title of our first question. There is a `div` with and `id="questions"`. This is the container for all our questions. So using out soup object, we need to find all elements, for the class `s-post-summary--content-title`. And that's pretty easy.
Please take a look at the code. 
Each element from the `questions` list is of the type _bs4.element.Tag_.

```python
questions = soup.select(".s-post-summary--content-title") # This returns a list and works as css selector
print(type(questions[0]))

#Output: <class 'bs4.element.Tag'>
```

If run the following code we are going to have access to different attributes of the css class.

```python
questions = soup.select(".s-post-summary--content-title") # This returns a list and works as css selector

print(questions[0].attrs)

#Output: {'class': ['s-post-summary--content-title']}
```

The Output is a diccitionary with the different values used in the `s-post-summary--content-title` class.

## 8- Browser Automation
