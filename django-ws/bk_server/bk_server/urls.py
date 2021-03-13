# mysite/urls.py
from django.conf.urls import include
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('ws_test/', include('apps.ws_test.urls')),
    path('admin/', admin.site.urls),
]