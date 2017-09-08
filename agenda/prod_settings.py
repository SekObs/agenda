DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'production_db',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': '',
        'PORT': '',
    }
}
