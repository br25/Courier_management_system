from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('courierapp.urls')),
    path('admin/', admin.site.urls),
]