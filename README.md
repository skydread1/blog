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

- Add the `blog` app to the INSTALLED_APPS array in the project `loicblog/common.py`.
- Add `path('', include('blog.urls'))` to the `urlpatterns` in `loic/blog/urls.py`.

## Markdown support

### django-markdownx

```bash
pip install markdown django-markdownx
```
- Then we need to add the `markdownx` app to the INSTALLED_APPS array in the project `loicblog/common.py`.
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

## Env variables

```bash
## install
pip install django-environ
```

Add `import environ` in `common.py`.

To define dev and prod settings, I used this [method](https://thinkster.io/tutorials/configuring-django-settings-for-production) that separate configs in 3 files:
- common
- dev
- prod

The env variables for dev or prod to be set are shown in `.end.dist`

## AWS S3

### django-storages

Django-storages is a Python library that provides a storage backends system for Django web applications.

```bash
pip install -U django-storages
```

For unknown reasons, the env variable `DJANGO_SETTINGS_MODULE` is not picked up by django while all the other env variables work fine.
So in order to use the `loicblog.setting.prod`, we need to manually change it in all the os.environ.setdefault like so:

```python
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "loicblog.settings.prod") # instead of "loicblog.settings.dev"
```

### boto3

official AWS SDK (Software Development Kit) for Python. Boto3 allows Python developers to interact with various Amazon Web Services (AWS) resources and services programmatically.

```bash
pip install -U boto3
```

### push static files to s3

First, make sure we use the prod env variable in `.env`:
```bash
DJANGO_SETTINGS_MODULE=loicblog.settings.prod
```

Then in `loicblog`:

```bash
python manage.py collectstatic
```

## AWS RDS Postgres

First, create AWS RDS postgres db and Security Group.

For the SG, it needs to have inbound rules for postgres.

### psycopg2-binary

The package `psycopg2-binary` is a PostgreSQL adapter for Python. It allows Python programs to communicate with a PostgreSQL database.

```bash
pip install psycopg2-binary
```

All the DB configs can be added in `.env`.

In order to migrate and setup the superuser properly, we need to run a few commands:

```bash
# apply migrations.
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

## AWS Beanstalk

[EB guide](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html) on deploying django app to EB.

First, we need to be sure all the packages are present in the requirements.txt:

```bash
pip freeze > requirements.txt
```

### gunicorn

Gunicorn (Green Unicorn) is a commonly used HTTP server for deploying Python web applications, including Django apps. When deploying a Django app on AWS Elastic Beanstalk, Gunicorn is often used as the application server to handle incoming HTTP requests and serve the Django application.

```bash
pip install gunicorn
```

### EB config

Can be found in `.ebextensions/django.config`

### AWS CLI EB

```bash
## first leave python virtual env
deactivate

## then proceed with eb cli
brew install awsebcli

## init eb
eb init

## BE SURE TO HAVE DJANGO_SETTINGS_MODULE=loicblog.settings.prod

## Create all resources
eb create

## (re)deploy
eb deploy
```

## Domain name

Fo HTTPS, we can create SSL certificate using AWS Certificate Manager for the subdomain `blog.loicblanchard.me`.

Note: ACM provides the CNAME record name and value. For the name, it will provide something like this:
`_SOME-NUMBERS-HERE.blog.loicblanchard.me.` but we need to only enter `_SOME-NUMBERS-HERE.blog` in GoDaddy record name for it to work.

Then in GoDaddy, to resolve `blog.loicblanchard.me` to the Application Load Balancer domain name (created when we created the EB), we need to add another CNAME record for the `blog` subdomain.

Then, we need to add rules to the ALB to redirect http to https using the ACM certificate.

Finally, we need to be sure the Security Group of the ALB allows inbound HTTPS.

Update the `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` with the subdomain and redeploy the EB.

## Font awesome free

```
pip install fontawesomefree
```

This requires to add a CORS policy on the S3 bucket like so:

```json
[
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "GET",
            "HEAD"
        ],
        "AllowedOrigins": [
            "https://blog.loicblanchard.me"
        ],
        "ExposeHeaders": []
    }
]
```

## HTMX

In order to use htmx with Django, we can use the package `django-htmx`:

```
## django-htmx does not include htmx itself, since it can work with many different versions.
pip install django-htmx
```

To download and setup htmx, follow the [installation instructions](https://django-htmx.readthedocs.io/en/latest/installation.html)

- I downloaded [htmx.min.js](https://unpkg.com/browse/htmx.org@1.9.3/dist/htmx.min.js)