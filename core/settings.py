import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '$mv9a_)qa)osf2ua_l_&tp1kl2+wwf0866u)y^xc+#!4#1k#am'

DEBUG = True

ALLOWED_HOSTS = ['yourdomain.com', '127.0.0.1', 'localhost']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'store',
    'basket',
    'account',
    'payment',
    'orders',
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

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'store.context_processors.categories',
                'basket.context_processors.basket',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Basket session ID
BASKET_SESSION_ID = 'basket'

# Stripe Payment
os.environ.setdefault('STRIPE_PUBLISHABLE_KEY','pk_test_51LaK0qKnMqatNE9EQ2Zq1knzNTZTF3kxJEM1jgIAAistHJhAIRnh11tirHEFSXjBJldCVtM5qktptTS2WZnnAivV00XdqVVhhr')
STRIPE_SECRET_KEY = 'sk_test_51LaK0qKnMqatNE9ElbejyQYX7TqRYnr4t0qBISQqKuufolJTZ372VSlHwjfNXRtxW7t3aPiBnGiD73q3lkGdlMpg008AbJjVjH'
# STRIPE_ENDPOINT_SECRET = 'whsec_4a7c906142e54b20ac80e9ff189c425d8a153575412147e0aea3ec98449bac44'
# stripe listen --forward-to localhost:8000/payment/webhook/

# Custom user model
AUTH_USER_MODEL = 'account.UserBase'
LOGIN_REDIRECT_URL = '/account/dashboard'
LOGIN_URL = '/account/login/'

# Email setting
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'