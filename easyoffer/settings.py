from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-7hq^*6vd0+6nplt(yhxhh(!g4%wczu4!v(touy2$6^ze0-tz%u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rating',
    'mentor',
    'analytic',
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

ROOT_URLCONF = 'easyoffer.urls'

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

WSGI_APPLICATION = 'easyoffer.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

GRADES = [
    ('Не указан', 'Не указан'),
    ('Trainee', 'Trainee'),
    ('Junior', 'Junior'),
    ('Middle', 'Middle'),
    ('Senior', 'Senior'),
]

UTC = [
    ('UTC−12', 'UTC−12'),
    ('UTC−11', 'UTC−11'),
    ('UTC−10', 'UTC−10'),
    ('UTC−9', 'UTC−9'),
    ('UTC−8', 'UTC−8'),
    ('UTC−7', 'UTC−7'),
    ('UTC−6', 'UTC−6'),
    ('UTC−5', 'UTC−5'),
    ('UTC−4', 'UTC−4'),
    ('UTC−3', 'UTC−3'),
    ('UTC−2', 'UTC−2'),
    ('UTC−1', 'UTC−1'),
    ('UTC+0', 'UTC+0'),
    ('UTC+1', 'UTC+1'),
    ('UTC+2', 'UTC+2'),
    ('UTC+3', 'UTC+3'),
    ('UTC+4', 'UTC+4'),
    ('UTC+5', 'UTC+5'),
    ('UTC+6', 'UTC+6'),
    ('UTC+7', 'UTC+7'),
    ('UTC+8', 'UTC+8'),
    ('UTC+9', 'UTC+9'),
    ('UTC+10', 'UTC+10'),
    ('UTC+11', 'UTC+11'),
    ('UTC+12', 'UTC+12'),
    ('UTC+13', 'UTC+13'),
    ('UTC+14', 'UTC+14'),
]


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
