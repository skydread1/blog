from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('blog.urls')),
    path('members/', include('django.contrib.auth.urls')), # django built in auth urls: login/logout
]
