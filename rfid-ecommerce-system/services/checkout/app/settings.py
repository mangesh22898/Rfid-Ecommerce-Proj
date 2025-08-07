SECRET_KEY = 'dummy'
DEBUG = True
ALLOWED_HOSTS = ['*']
ROOT_URLCONF = 'app.urls'
INSTALLED_APPS = ['django.contrib.contenttypes', 'django.contrib.auth']
MIDDLEWARE = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}
