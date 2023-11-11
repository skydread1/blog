from loicblog.settings.common import *

DEBUG = True

# SQLite Database

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'dev-blog-statics')
