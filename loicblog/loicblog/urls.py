from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('blog.urls')),
    path('members/', include('django.contrib.auth.urls')), # django built in auth urls: login/logout
    path('members/', include('members.urls')), # if not django auth urls, go for our custom app urls: register
]
