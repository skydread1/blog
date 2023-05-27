# blog
Blog for my technical articles

## Start python env

```bash
# create env
python3 -m venv blog_venv

# activate env (mac)
source blog_venv/bin/activate
```

## Install Django
```bash
pip install django
pip install --upgrade pip
```

## Start Django project
```bash
django-admin startproject loicblog
```

## Migrations
Migrations are Django’s way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema. They’re designed to be mostly automatic, but you’ll need to know when to make migrations, when to run them, and the common problems you might run into.

```bash
# apply and unapply migrations.
python3 manage.py migrate
```

## Run server
```bash
# be sure to migrate first
python3 manage.py runserver  
```

## Admin
```bash
python manage.py createsuperuser --username=myname --email=me@gmail.com
```

## Start app

One project can have multiple apps such as a blog, an authentication system etc
So `loicblog` is the project and `blog` is one app inside the project.

```bash
python3 manage.py startapp blog
```

Then we need to add the `blog` app to the INSTALLED_APPS array in the project `loicblog/settings.py`.
We also need to add `path('', include('blog.urls'))` to the `urlpatterns` in `loic/blog/urls.py`.