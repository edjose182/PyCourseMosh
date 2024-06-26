# Building Web Applications with Django

## 2- Your first Django Project

First, we create a folder called "vidly". Now in here we are going to install _Django_.

1. `pip install pipenv`
2. `python -m pipenv shell`
3. `pip install pipenv`
4. `pipenv install django==2.1`

Next we are going to use a tool called _django admin_ for creating a new django project.

Here is the command: `django-admin startproject vidly .`

_Django admin_ created a vidly directory as well as a _manage.py_ file. We use _manage.py_ to perform some administrative tasks such as tarting our web server or migrating our database, populating it with data and so on.

Now in the "vidly" directory that was created is essentially the core of a project. It has a bunch of settings and that's where everything gets started. So we have _init.py_, this tells python to treat this directory as a package.

Bwllow that we have _settings.py_ and in this file we have various configuration settings for our project, next we have _urls.py_ and this is where we define various **URLs** endpoints for our applications, and finally we have _wsgi.py_  which is short forWeb Server Gateway Interface. The purpose for this file is to represent the standard interface between application written in python and web servers. That is an advane topic and goes beyond the scope of this course. 

Now we are going to use _manage.py_ to initialize the web server.

(To install pylint, we can use the following command: `pipenv install pylint --dev`)

To do this we are going to run _manage.py_: `manage.py runserver`

After this we can see that the server is running on port 8000: http://127.0.0.1:800/

And we can stop it at any time by pressing Control C

If we go to the created URL we should be able to see the following:

![django_init](./img/django_init.PNG)

That means that our first Django project is working.

## 3- Your First App

In Django a project can contains multiple apps, and this apps don't represent that entire application, they represent a small part of an application that is focused on one functional area.

![django_project_example_img](./img/django_project_example_img.PNG)

For example let's say we are going to build a website like Amazon. Amanzon has a lot of different functional areas such as:

![django_project_example_img_2](./img/django_project_example_img_2.PNG)

Each functional area includes a bunch of highly related function. So with this architecture we could beak down a large complex project into a smaller, more manageable and more maintainable apps. Also, we can reuse these apps in other _Django_ projects. For example, we can build an app that represents a blog and then reuse this app in any website that needs a block.

In this lecture we are going to create an app called movies. And this app will have all the funcionalities for displaying the list of the movies, as well as the details of a given movie.

First we run `python manage.py startapp movies`. This created a new directory called "movies". In this directory we have the following:

1. _migrations_ folder.
2. _\_\_init\_\_.py_: This tell python that this is a package, so pontentially in the future we can distribute this package in pypi.org.
3. _admin.py_: This is where we define how the admistration are for managing the movies will look like.
4. _apps.py_: This file is a little bit confusing becase here we are in within the boundary of one app.

   So why do we have a file called _apps.py_? Basically we use this to store various configuration settings for this app.
5. _models.py_: Here we define classes that represent the domain of this app. For example, in the domain of movies we could have classes like movie, genre and so on.
6. _tests.py_:This is where we write automated tests for this app.
7. _views.py_: This is where we define out view function.

   View in short is a function that takes a request on the terms of response.

### MVC architectural pattern

In this [link](https://www.geeksforgeeks.org/mvc-design-pattern/) there is a description of **MVC architectural pattern**. Here is the diagram showed in the lecture:

![mvc_archi_pattern](./img/mvc_archi_pattern.PNG)

DJango uses the Model-Tempalte-View (**MVT**) structure.

## 4- Views

Now we are going to create the **view function**. In the _movies_ folder we are going to open up _views.py_. And in here we define a function called index.

This name is arbitrary, cd lt anything but usually we the word index for naming the function that represents a main page of an app.

```python
from django.shortcuts import render

def index(request):
    pass
```

Now, all our view functions should take the parameter called _request_ , again the name is arbitrary, but the object that is passed to this function is an http request object. We are not goin to call this function, Django will take care of doing this. So when we send an http request endpoint, Django, will figure out based on some configuration what the function should be called.

Now in every view function we should return an http response. So, on the top it is imported the http response class from Django http module.

```python
from django.http import HttpResponse

from django.shortcuts import render

def index(request):
    return HttpResponse("Hello World!")
```

And this is our first _view_, now we need to map this to the URL. So back in the movies app, let's add a new file, by convention the name of this file should be _urls.py_.

In this file we are going to create a variable called `urlpatterns` that we should set to a list, again, this is one of the conventions that Django expects us to follow.

And in this list we add objects that map URL endpoints or view functions. And for that we use the path function in Django. So, on the top from Django URLs.

Here we are going to use an empty string, and this will represent the root of this app. For example, in our movies app, we are going to have some URL endpoints like this:

- movies/
- movies/1/details

So here an empty string represents the root of this app.

```python
from django.urls import path

from . import views #It is better to do it in this way because
                    #someone can use a different path

urlpatterns = [ #This is the URL configuration
    path('', views.index,name='index')
]
```

So we are done with configuring URLs but our main app, the Vydli app, has no knowledge of the movies app. So if head over to local host.

So we need to go to the main app (Vydli) and this folder we have an _urls.py_ that defined the URL configuration for our main app.

```python
# Path of the file: vidly/urls.py
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
```

Now we need to include the movies URLs to the main URL:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/',include('movies.urls'))
]
```

## 5- Models

The next step is to create the models for this _movies_ app. These models are python clasesses that we use to represent our application data.

So here in our movies ap, we are going to have models like genre and movie.

Now we are going to create them. Here in the _movies_ directory let's open up _models.py_. Here we are going to create a class called **Genre** and we should direct this class from `models.model` 
So in Djando we have this package `django` and this package encapsulates all the functionality around working with databases. Now in this package we have a module called `models` and in this module we have a class called model.

This class encapsulates a lot of functionality who is stroring a model object in the database, or retrieving model objects, filter them and so on.

So by enheraince our class from the base model class in Django. Our genre class will also iherit all the functionality, which means we don't really have to write any code to store genre objects in a database. Django will automatically take care of that. 


With `on_delete` we tell Djang what should happen when a genre is deleted. For example, if you have a genre called comedy. And we have 5 movies in this genre, what should happen if we accidentally or deliberately delete the comedy genre? All the movies associated to this genre will be deleted.

## 6- Migrations

So we have created our model calsses, now we should be able to store our model objects in a database. In the project there is a file called: _db.sqlite3_. This is a blank sqlite database that Django automatically created for us. SQLite is avery simple light weight database that we ofen use in small applications like applications that we run in mobile devices. But it's not suitable in an enterprise with applications that is supposed to serve thousands or even millions of users.

We need to create Tables to be able to store data in database. Having said that, when using Django, we don't have to manually design these tables. We can have Djando automatically create them for us based on our models. So every time we create new model classes.

So everytime we created model classes or modify existing ones, we tell Django to compare our model classes with our database. Django will look at out database, it will figure out what tables and columns we have, then it will calculate the difference between our model classes and our database tables. And based on that it will create a migration.

A migration is essentially a python file, that includes some code, when we run that, it will synchronize our database with out model classes.

So if we open a terminal window and run `python mange.py makemigrations` it will tell us there are no changes and this is because Django is not aware of our model classes. So the first step is to register our movies app with Django. 

In our project, inside the _vidly_ package we open the _settings.py_ file. 

This file has the configurations to be use by our project and one of them is the **INSTALLED_APPS**.

The first one is admin, and this creates and administration pattern for us.

We have auth, which is the authentication framework. With this we'll be able to authenticate users and  see if they have permissions to perform various tasks.

We have content types which is a framework for creating generic classes within model classes.

Below that we have the sessions app, which is a framework that allows us to temporarily store data above the current user.

Next we have the messaging framework, and we use that in situations where let's say the user creates a new movie and then we redirect them and display the message like, the movie was successfully created.

And finally we have static files, which is used for managing static files like css files, images, so on.

Now on moost applications, we need pretty much all these install apps, but if you don't need any of these apps in your application you can simply come back here and delete that app.

For this demo, we need to register the movies app here, so Django can keep track of our model classes in that app.

In the movies folder, here we have the file _apps.py_. In here we can have various configuration settings, for the movies app. In the class `MoviesConfig`, this class is in the apps module of the movies package, so to register the movies app with Django we need to provide the complete path to this class. So now we go back to _settings.py_, here we add movies:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'movies.apps.MoviesConfig'
]
```

Now we are going to run `python manage.py makemigrtions` one more time:

```txt
Migrations for 'movies':
  movies\migrations\0001_initial.py
    - Create model Genre
    - Create model Movie
```

This time Django detected that there are some changes in the movies app, so it created a migration that is inside movies/migration/0001_initial.py. Let's have a quick look at this migration. 

```python
# Generated by Django 2.1 on 2024-06-20 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('release_year', models.IntegerField()),
                ('number_in_stock', models.IntegerField()),
                ('daily_rate', models.FloatField()),
                ('Genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Genre')),
            ],
       
```

There is a class called migration, and in this class we have a couple of operations for bringing our database up to date with the current model classes. So the first operation is for creating a Model (_Create\_Model_). We can see the name is set to genre, and here are the fills of the genre. So we have id and name.

Now in the code, we only specify the name field, we didn't add the id field. Django automatically takes care of that, so it ensures that every object has an id that uniquely identifies that object. Now similarly we have another create model operation for creating the movie table, in this table, we are going to have these fields:

- id
- title
- release_year
- number_in_stock
- daily_rate
- genre

This migration is not executed yet. It simply describes the operations that need to be performed to the database to bring it up to date with our current model classes.

So the next step is to run this migration. Before doing that, if we run `python manage.py runserver` we are going to see the following message:

```txt
You have 16 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, movies, sessions.
```

That basically means you have migrations that need to be executed. Now we run `python manage.py migrate` to apply the missing migrations in our database.
If we open the database, we can see we have a total of 13 tables. Each of these tables is prefixed with the name of the app that contains it. 

Here we can find the two tables for our movies app (genre and movie). So table names are in singular.

![database-after-migration](img/database-after-migration.PNG)

Of course this is done by convention and we can always override that in the future if we want to.

## 7- Changing the Models

Let's go through this workflow one more time. So here in the movies app, let's open up _model.py_.
Here's our movies class and we are going to add a new attribute called date "created"

```python
from django.db import models
from django.utils import timezone

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    Genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
```

It was necessary to import the timezone class and create a reference to the `timezone.now` method to get the date according to the timezone of the user.

Now we need to create a new migration, so in the terminal let's run: `python manage.py makemigrations`

```txt
$ python manage.py makemigrations
Migrations for 'movies':
  movies\migrations\0002_movie_date_created.py
    - Add field date_created to movie
```

Now we have migration number , let's take a quick look at this migration

```python
# Generated by Django 2.1 on 2024-06-20 00:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
```

So here we have an operation of type `AddField`. So this operation is going to go to the movie table, an alterior field called `date_created` and this is how it's going to alter this field.

Now in the terminal we run `python manage.py migrate`

```txt
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, movies, sessions
Running migrations:
  Applying movies.0002_movie_date_created... OK
```

The second migration is applied and now in the _movies_movie_ table we can see the new field.

If we want to know which SQL commands are being use by python we can use the following command: `python manage.py sqlmigrate movies 0001` (movies is the app that we are interesting to migrate)

```sql
BEGIN;
--
-- Create model Genre
--
CREATE TABLE "movies_genre" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(255) NOT NULL);
--
-- Create model Movie
--
CREATE TABLE "movies_movie" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(255) NOT NULL, "release_year" integer NOT NULL, "number_in_stock" integer NOT NULL, "daily_rate" real NOT NULL, "Genre_id" integer NOT NULL REFERENCES "movies_genre" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "movies_movie_Genre_id_4fca4315" ON "movies_movie" ("Genre_id");
COMMIT;
```

## 8- Admin

Alright, our database is in good shape. Now the next step is to allow the staff at our imaginary video store to populate the list of movies. So we need to create an administration panel for them.

However, when using Django, we don't have to do this manually. So all Django applications come with a powerful adminstration interface.

In the terminal we are going to run our development server `python3 manage.py runserver`

After running the command we are going to see the following:

![default-window-server](./img/default-window-server.png)

In the URL we are going to add "admin"

![admin-window-server](./img/admin-window-server.png)

This is the entrance to our adminstration panel.

So by default, we get this login screen, this is coming from the auth app that is installed by default. 

In the _settings.py_ file we can find the installed apps:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'movies.apps.MoviesConfig'
]
```

The second app is the _autho app_ and this the app that know everything about autheticating users. And the login screen is implemented inside of that app. SO as you can see, that app is a small reusable package that we are using in this project. By the same token we can create small, reusable apps that other people can use in their projects.

Now back to the login screen, currenlty we don't have any users in our database. So the next step is to create a super user. Now we are going to use another terminal so in that way in the main therminal the server can be running.

Now we are going to run the following command: `python3 manage.py createsuperuser`

Now we need to enter an user, an e-mail and password.

Now if we go to the login screen we can use the user and the password. Once everything is ready we are going to see the following window:

![login-succesful-window](./img/login-succesful-window.png)

Now in here we can manage the list of groups nad users. SO we can put users in different groups like admins, moderators, guest and so on.

If click the users options, the window is going to shows us a table with all the users that has access.

![users-table-view](./img/users-table-view.png)

Now, in the main page we can only manage hte users and groups. We cannot manage our custom models like genre and movies, but we can easily bring them here with only a single line of code.

In the _movies_ app (`PyCourseMosh/webApps_django-u12/vydli/movies/`) we have the admin file and this is where we register the models we want to manage using our administrative interface.

Now in this file we need to import our genre and movie classes.

```python
from .models import Genre, Movie

admin.site.register(Genre)
admin.site.register(Movie)
```

WIth this we are telling to Django to register these models in the administration interface.
Now we save the changes and in the main page we are goin to update the window.

![updated-admin-models](./img/updated-admin-models.png)

Now we have the Genre and Movies models in our movies app.

## 9- Customizing the Admin

We can override the str magic method in the _Genre_ class.

In the movies app, let's open up _models.py_. And here we are going to find the _Genre_ class. In here we can override the str magic method to specify the string representation of a _Genre_ object. So let's define the `__str__` method.

```python
def __srt__(self):
    return self.name
```

We want to use the name of a genre to represent it as a string.

Now we are going to take this to the next level. Let's say you want to add another clomun. To see the _ID_ of each genre, for that we need to go to our movies app and open _admin.py_ module.

We previously registered the genre calss with admin, now to customize how we work with genres in our admin panel, we need to create another class called `genre_admin`. Now to customize the list of genres in admin, we need to create.

```python
#File: admin.py
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id','name')

admin.site.register(Genre,GenreAdmin)
```

If we refresh the web page (http://127.0.0.1:8000/admin/movies/genre/) we can see that the table looks better now:

![admin-modifcations-1](./img/admin-modifcations-1.png)

Now we can use the user interface to add a new genre.
I'm going to add Action and Comedy.

>**Info: Minor fix**
>
>There was a problem with the version that I was using of Django for Python. I was getting the error show here: [No such table:main.auth_user__old](https://forum.codewithmosh.com/t/no-such-table-main-auth-user-old/2415/3).
>
>I tried the next steps to fix the problem:
>
>1. Stopped the django webserver running, Ctrl-C
>2. Delete the db.sqlite3
>3. Uninstalled Django old verison
>4. Install latest version of Django with “pip install django”
>5. Install latest version of Django with “pipenv install django” 
>6. Issue “python manage.py makemigrations”
>7. Issue “python manage.py migrate”
>8. Create a superuser with “python manage.py createsuperuser”
>9. Issue “python manage.py runserver” (or port 8080)

Now the table looks like this:

![added-genres](./img/added-genres.png)


In movies we don't anything yet. Now we are going to add a new movie using the interface.

![adding-new-movie](./img/adding-new-movie.png)

Now the interface let us to select the date that new movie(s) is included but we can hide this.

To do this, we need to create a model admin for movies.

```python
#File: admin.py
class MovieAdmin(admin.ModelAdmin):
    exclude = ('date_created')
...
admin.site.register(Movie,MovieAdmin)
```

## 10- Database Abstraction API