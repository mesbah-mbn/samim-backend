import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# 🔐 SECURITY
SECRET_KEY = os.environ.get("SECRET_KEY", "unsafe-secret-key")
DEBUG = False
ALLOWED_HOSTS = ['*']

# 📦 APPS
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "corsheaders",
    "rest_framework",
    "api",
]

# ⚙️ MIDDLEWARE (ORDER IS IMPORTANT)
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # MUST BE FIRST
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# 🌍 CORS + CSRF
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

CSRF_TRUSTED_ORIGINS = [
    "https://leed-production.up.railway.app",
]

# 📁 STATIC
STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# 📁 MEDIA
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# 🌐 URLS
ROOT_URLCONF = "core.urls"

# 🧩 TEMPLATES
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# 🚀 WSGI
WSGI_APPLICATION = "core.wsgi.application"

# 🗄 DATABASE
DATABASES = {
    "default": dj_database_url.config(
        default="sqlite:///db.sqlite3"
    )
}

# 🔐 PASSWORD VALIDATION
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# 🌍 INTERNATIONAL
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
