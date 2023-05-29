from django.urls import path, include
from .views import HomeView, PostDetailsView, CreatePostView, EditPostView, DeletePostView
from django.conf import settings
from django.conf.urls.static import static

## map URLs to class-based views
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostDetailsView.as_view(), name='post_details'),
    path('post/create', CreatePostView.as_view(), name='create_post'),
    path('post/edit/<int:pk>', EditPostView.as_view(), name='edit_post'),
    path('post/delete/<int:pk>', DeletePostView.as_view(), name='delete_post'),
    path('markdownx/', include('markdownx.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)