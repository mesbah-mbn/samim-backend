import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# 🔐 SECURITY — crash loudly if SECRET_KEY is missing in production
SECRET_KEY = os.environ["SECRET_KEY"]

DEBUG = False

# Lock down to known hosts only — set ALLOWED_HOSTS env var in Railway
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(",")

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

# ⚙️ MIDDLEWARE — CSRF middleware restored (never remove this!)
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # Must be first
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",  # ✅ Restored
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# 🌍 CORS — never allow all origins with credentials
# Set CORS_ALLOWED_ORIGINS in Railway, e.g.:
#   https://leed-production.up.railway.app,https://your-frontend.com
CORS_ALLOWED_ORIGINS = os.environ.get("CORS_ALLOWED_ORIGINS", "").split(",")
CORS_ALLOW_CREDENTIALS = True

# 🛡️ CSRF — the actual fix for your 403 error
# Set CSRF_TRUSTED_ORIGINS in Railway, e.g.:
#   https://leed-production.up.railway.app
CSRF_TRUSTED_ORIGINS = os.environ.get("CSRF_TRUSTED_ORIGINS", "").split(",")

# 🔒 HTTPS security headers (Railway terminates SSL via proxy)
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# 📁 STATIC FILES
STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# 📁 MEDIA FILES
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# 🌐 URL CONFIG
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

# 🗄 DATABASE — no SQLite fallback; crash if DATABASE_URL is missing
# conn_max_age=600 enables persistent connections (better performance on Railway)
DATABASES = {
    "default": dj_database_url.config(conn_max_age=600)
}

# 🔐 PASSWORD VALIDATION
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# 🌍 INTERNATIONALISATION
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
