# blog
Blog for my technical articles

## Start python env

```bash
# create env
python -m venv blog_venv

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
# create new migrations based on the changes made to the models
python manage.py makemigrations

# apply and unapply migrations.
python manage.py migrate
```

## Run server
```bash
# be sure to migrate first
python manage.py runserver  
```

## Admin
```bash
python manage.py createsuperuser --username=myname --email=me@gmail.com
```

## Start app

One project can have multiple apps such as a blog, an authentication system etc
So `loicblog` is the project and `blog` is one app inside the project.

```bash
python manage.py startapp blog
```

- Add the `blog` app to the INSTALLED_APPS array in the project `loicblog/settings.py`.
- Add `path('', include('blog.urls'))` to the `urlpatterns` in `loic/blog/urls.py`.

## Markdown support

### django-markdownx

```bash
pip install markdown django-markdownx
```
- Then we need to add the `markdownx` app to the INSTALLED_APPS array in the project `loicblog/settings.py`.
- Add the path to urls.py: `path('markdownx/', include('markdownx.urls'))`.
- Collect MarkdownX assets to your STATIC_ROOT:
```bash
python manage.py collectstatic
```

### code block and code block highlighting

By default the code block `pre` are not supported and there is no syntax highlighting.

Adding `MARKDOWNX_MARKDOWN_EXTENSIONS = ['fenced_code', 'codehilite']` to the settings enable them.

`codehilite` required the `pygments` package:

```bash
pip install pygments
```