<div align="center">
    <a href="https://www.flybot.sg/" target="_blank" rel="noopener noreferrer"><img src="loicblog/blog/static/favicon.ico" alt="flybot logo" width="25%"></a>
</div>

<div align="center">
    <a href="https://www.python.org/downloads/release/python-3116/" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/python-v3.11.6-green.svg" alt="Python Version"></a>
    <a href="https://docs.djangoproject.com/en/4.2/releases/4.2.1/" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/django-v4.2.1-green.svg" alt="Django Version"></a>
    <a href="https://github.com/skydread1/blog" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/contributions-welcome-green.svg" alt="Contributions welcome"></a>
</div>

<h1 align="center">🐍 Django Blog for my tech articles 🐍</h1>

## 🐍 Rational

This repository contains the source code of my tech blog made in `python` using the `Django` web framework. I used a bit of `HTMX` for dynamic UI especially of the search bar. The project has 2 apps: 
- `blog`: to manage posts and categories
- `members`: to manage user authentication

The blog is deployed on `AWS`:
- the app is deployed in **AWS Elastic Beanstalk**
- the production data is stored in an **AWS RDS Postgres** db instance.
- the static files are served from an **AWS S3 bucket**.

## 🐍 Features

A superuser can login at `members/login`. Once logged in, the user can create/edit/delete posts.

A `post` is written in markdown and the UI provides a live preview of how it will look like once submitted.

Each post belongs to a `category`. A user can create category via the UI as well.

There is a dark/light mode and the website is responsive

The code blocks also support `syntax highlighting`.

## 🐍 Getting Started

If you want to try it out locally, you can clone the repo:
```
git clone https://github.com/skydread1/blog.git
```

Note: I developed the app on mac, so some command might differ if you use a different OS.

### 1. Start python env

First, activate the python env and load the project dependencies:

```bash
# activate env (mac)
source blog_venv/bin/activate

# load deps
pip install -r requirements.txt
```

### 2. Migrations

Migrations are Django’s way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema. They’re designed to be mostly automatic, but you’ll need to know when to make migrations, when to run them, and the common problems you might run into.

```bash
# create new migrations based on the changes made to the models
python manage.py makemigrations

# apply and unapply migrations.
python manage.py migrate
```

### 3. Admin

In Django, a superuser is a user account with special privileges that go beyond those of regular users. The superuser has full access to the Django Admin interface and can perform administrative tasks such as managing other user accounts, creating, updating, and deleting database records, and more.

```bash
python manage.py createsuperuser --username=myname --email=me@gmail.com
```

### 4. collectstatic

I used `django-markdownx` to be able to write the post in markdown and have them automatically rendered to html.

`django-markdownx` required us to collect all the static files in a specific locations like so:

- Collect MarkdownX assets to your STATIC_ROOT:
```bash
python manage.py collectstatic
```

This will generate all the static files in `dev-blog-statics`.

### 5. Env variables

In **dev**, I use the default django `sqlite3` database and the static files are located in `dev-blog-statics`.

In **prod**, I use an AWS `RDS Postgres` database and the static files are located in an `AWS S3 bucket`.

To define dev and prod settings, I used this [method](https://thinkster.io/tutorials/configuring-django-settings-for-production) that separate configs in 3 files:
- common
- dev
- prod

The env variables for dev or prod are shown in `.end.dist`

You need to create a `.env` file alongside the `.env.dist` and provide your own values.

For `dev`, you just need these 2 variables:
```bash
DJANGO_SETTINGS_MODULE=loicblog.settings.dev
SECRET_KEY={secret} ## replace with your own
```

To generate the django secret key, you can use:
```
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Never share this key wit anyone. The `.env` is in the .gitignore so it will not be pushed to your online repo.

## 🐍 Run server

Now that we have setup the project properly, meaning:
1. create python venv and loaded deps
2. created django superuser
3. migrated BD models
4. generated static files
5. understood how to deal with env variables

We can finally run the server:

```bash
python manage.py runserver
```

Now, let's have a look at the `prod` setting you need to setup to deploy and run the app on AWS:

## 🐍 AWS S3

You will need to create a S3 bucket on AWS first.

### django-storages

Django-storages is a Python library that provides a storage backends system for Django web applications.

For unknown reasons, the env variable `DJANGO_SETTINGS_MODULE` is not picked up by django while all the other env variables work fine.

So in order to use the `loicblog.setting.prod`, we need to manually change it in all the os.environ.setdefault like so:

```python
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "loicblog.settings.prod") # instead of "loicblog.settings.dev"
```

### boto3

It is th official AWS SDK (Software Development Kit) for Python. Boto3 allows Python developers to interact with various Amazon Web Services (AWS) resources and services programmatically.

### push static files to s3

First, make sure we use the prod env variable in `.env`:
```bash
DJANGO_SETTINGS_MODULE=loicblog.settings.prod
```

Then in `loicblog`:

```bash
python manage.py collectstatic
```

All the static files will be pushed to AWS S3.

## 🐍 AWS RDS Postgres

First, create AWS RDS postgres db and Security Group.

For the SG, it needs to have inbound rules for postgres.

### psycopg2-binary

The package `psycopg2-binary` is a PostgreSQL adapter for Python. It allows Python programs to communicate with a PostgreSQL database.

All the DB configs can be added in `.env`.

In order to migrate and setup the superuser properly, we need to run a few commands:

```bash
# apply migrations.
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

## 🐍 AWS Beanstalk

You cna have a look at this [EB guide](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html) on deploying django app to EB.

First, we need to be sure all the packages are present in the requirements.txt:

```bash
pip freeze > requirements.txt
```

### gunicorn

`Gunicorn` (Green Unicorn) is a commonly used HTTP server for deploying Python web applications, including Django apps. When deploying a Django app on AWS Elastic Beanstalk, Gunicorn is often used as the application server to handle incoming HTTP requests and serve the Django application.

### EB config

Can be found in `.ebextensions/django.config`

### AWS CLI EB

Using the eb cli allows us to deploy the new app version in just a few commands.

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

## 🐍 Domain name

I personally use **GoDaddy** as DNS manager but you can use the one of your choice.

Fo HTTPS, we can create SSL certificate using AWS Certificate Manager for the subdomain (in my case `blog.loicblanchard.me`).

Note: ACM provides the CNAME record name and value. For the name, it will provide something like this:
`_SOME-NUMBERS-HERE.blog.loicblanchard.me.` but we need to only enter `_SOME-NUMBERS-HERE.blog` in GoDaddy record name for it to work.

Then in GoDaddy, to resolve `blog.loicblanchard.me` to the Application Load Balancer domain name (created when we created the EB), we need to add another CNAME record for the `blog` subdomain.

Then, we need to add rules to the ALB to redirect http to https using the ACM certificate.

Finally, we need to be sure the Security Group of the ALB allows inbound HTTPS.

Update the `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` with the subdomain and redeploy the EB.

## 🐍 Contributions

Feel free to open new issues if you find bugs or want to add new features.

## 🐍 Disclaimer

Using this AWS setup should be practically free within the AWS free tier (as of Nov 12th 2023). Once your free tier expires, expect around $50/month for a low traffic blog (it is just an estimation).
