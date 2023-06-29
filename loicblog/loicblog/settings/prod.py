from loicblog.settings.common import *

DEBUG = False

ALLOWED_HOSTS = ["blog.loicblanchard.me", "*"] # add localhost for local testing

CSRF_TRUSTED_ORIGINS = ['https://blog.loicblanchard.me']

# Amazon S3 configuration
AWS_ACCESS_KEY_ID = env.str('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env.str('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env.str('AWS_STORAGE_BUCKET_NAME')

INSTALLED_APPS += [
   'storages',
]

STORAGES = {
    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3StaticStorage"
    }
}

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_S3_FILE_OVERWRITE = True

# Set the static root to the S3 bucket path
STATIC_ROOT = 's3://%s/static' % AWS_STORAGE_BUCKET_NAME

## Admin styling adjustment

ADMIN_MEDIA_PREFIX = '/static/admin/'

# PostgreSQL Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.str('DB_NAME'),
        'USER': env.str('DB_USER'),
        'PASSWORD': env.str('DB_PASSWORD'),
        'HOST' : env.str('DB_HOST'),
        'PORT': env.str('DB_PORT', default='5432'),
    }
}