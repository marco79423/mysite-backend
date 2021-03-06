from path import Path


##################################################################
# Application configuration
##################################################################

PROJECT_DIR = Path(__file__).abspath().realpath().dirname().parent
PROJECT_NAME = PROJECT_DIR.basename()

ROOT_URLCONF = 'mysite_backend.urls'

WSGI_APPLICATION = 'mysite_backend.wsgi.application'
HOST = "http://localhost:8000"

DEBUG = True

##################################################################
# Language and timezone
##################################################################

# https://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = 'Asia/Taipei'

LANGUAGE_CODE = 'zh-hant'

USE_TZ = False
USE_I18N = True
USE_L10N = True

##################################################################
# Middleware
##################################################################

MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]

##################################################################
# Static
##################################################################

# The absolute path to the directory where collectstatic will
# collect static files for deployment.
STATIC_ROOT = PROJECT_DIR / "static"

STATIC_URL = '/static/'

# The list of finder backends that know how to find static files
# in various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

##################################################################
# Media
##################################################################

MEDIA_ROOT = PROJECT_DIR / "media"
MEDIA_URL = '/media/'

##################################################################
# Templates
##################################################################

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

##################################################################
# Database
##################################################################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': PROJECT_DIR / 'db.sqlite3',
    },
}

##################################################################
# Cache
##################################################################

USE_CACHE = False
if USE_CACHE:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211',
            'TIMEOUT': 60 * 60 * 24,  # 1d
            'OPTIONS': {
                'MAX_ENTRIES': 1000
            }
        }
    }

##################################################################
# Apps
##################################################################

# Application definition
DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    "rest_framework",
    'rest_framework.authtoken',
    "corsheaders",
    'djcelery',
    'kombu.transport.django',
]

PROJECT_APPS = [
    "blog",
]

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + PROJECT_APPS

##################################################################
# Security
##################################################################

SECRET_KEY = "I dont care in development env"
ALLOWED_HOSTS = [
    "localhost",
    "api.marco79423.net",
    "api-dev.marco79423.net"
]

CORS_ORIGIN_ALLOW_ALL = True

##################################################################
# Django REST framework
##################################################################

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    )
}

##################################################################
# Celery
##################################################################

BROKER_URL = 'django://'
CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend'

##################################################################
# Application settings
##################################################################

SOURCE_DIR = Path(PROJECT_DIR) / ".." / ".." / "mysite-content"

##################################################################
# Other
##################################################################

VERSION = ""
