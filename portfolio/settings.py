from json import load
import os
from dotenv import load_dotenv
from .celery import app

load_dotenv()
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split(' ')
DB_ENGINE = os.getenv("DB_ENGINE")
DB_NAME = os.getenv("POSTGRES_DB")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASS = os.getenv("POSTGRES_PASSWORD")
DB_HOST = os.getenv("POSTGRES_HOST")
DB_PORT = int(os.getenv("POSTGRES_PORT"))
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = int(os.getenv("EMAIL_PORT"))
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS=True
DEBUG = True

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'blog.apps.BlogConfig',
    'jobs.apps.JobsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'django_social_share',
    'accounts',
    'mptt',
    'django_celery_results',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['portfolio/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

WSGI_APPLICATION = 'portfolio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': DB_ENGINE,
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASS,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Baku'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'portfolio/static')
]
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
CKEDITOR_CONFIGS = {
         # django-ckeditor uses the default configuration by default
    'default': {
                 # Editor width adaptive
        'width':'auto',
        'height':'250px',
                 # Tab key to convert the number of spaces
        'tabSpaces': 4,
                 # Toolbar style
        'toolbar': 'Custom',
                 # Toolbar button
        'toolbar_Custom': [
                         # Emoji code block
            ['Smiley', 'CodeSnippet'],
            ['Format'],
                         # Font style
            ['Bold', 'Italic', 'Underline', 'RemoveFormat', 'Blockquote'],
                         # font color 
            ['TextColor', 'BGColor'],
                         # Link
            ['Link', 'Unlink'],
                         # List
            ['NumberedList', 'BulletedList'],
                         # Maximize
            ['Maximize'],
            ['Source'],
            ['Table', 'Tabletools'],
            ['Image']
        ],
        # Add code block plugin
        'codeSnippet_languages': {
            'python': 'Python <3',
            'c': 'C',
            'cpp': 'C++',
            'csharp': 'C#',
            'bash': 'Bash',
            'aspnet': 'ASP.NET',
            'dart': 'Dart',
            'docker': 'Docker',
            'flutter': 'Flutter',
            'fortran': 'Fortran',
            'haskel': 'Haskel',
            'markup': 'HTML',
            'http': 'HTTP',
            'git': 'Git',
            'go': 'Golang',
            'java': 'Java',
            'javascript': 'JavaScript',
            'makefile':'Makefile',
            'matlab': 'MATLAB',
            'nginx': 'Nginx',
            'pascal': 'Pascal',
            'perl': "Perl",
            'php': 'PHP',
            'rust': 'Rust',
            'ruby': 'Ruby',
            'r': 'R',
            'sas': 'SAS',
            'scala': 'Scala',
            'scheme': 'Scheme',
            'sql': 'SQL',
            'swift': 'Swift',
            'vim': 'Vim',
            'yml': 'YML'
        },
       
        'extraPlugins': ','.join(['codesnippet', 'prism', 'widget', 'lineutils', 'table', 'clipboard', 'format',
                                  'image', 'tabletools']),

    }
}


# CELERY CONF
CELERY_RESULT_BACKEND = 'django-db'
CELERY_CACHE_BACKEND = 'django-cache'
CELERY_TIMEZONE = "Asia/Baku"
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = os.getenv("CELERY_BROKER_URL")
CELERY_ENABLE_UTC = False