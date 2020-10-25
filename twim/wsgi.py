"""
WSGI config for twim project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

# 10/26heroku設定で11~17行までコメントアウト
# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'twim.settings')

# application = get_wsgi_application()


# heroku用
import os

from dj_static import Cling
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sample_app.settings")

application = Cling(get_wsgi_application())
