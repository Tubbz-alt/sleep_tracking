from django.contrib import admin
from django.urls import path, include

from tracking import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tracking.urls'))
]
