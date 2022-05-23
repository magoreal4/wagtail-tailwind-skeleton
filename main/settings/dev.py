from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-hzb7n0nst08m46-@h8tr2mz8+vb7+k)a82^61ydh^w9u80y1n^'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# python manage.py shell_plus
INSTALLED_APPS = INSTALLED_APPS + [
    'tailwind',
    'theme',
    'django_browser_reload',
    'django_extensions'
]
# python manage.py shell_plus --ipython

MIDDLEWARE = MIDDLEWARE + [
    'django_browser_reload.middleware.BrowserReloadMiddleware',
    # "debug_toolbar.middleware.DebugToolbarMiddleware",
]

TAILWIND_APP_NAME = 'theme'

INTERNAL_IPS = [
    "127.0.0.1",
]

TAILWIND_CSS_PATH = './css/main.css'
# try:
#     from .local import *
# except ImportError:
#     pass

