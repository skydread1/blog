from django.urls import path
from .views import HomeView, PostDetailsView, CreatePostView

## map URLs to class-based views
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostDetailsView.as_view(), name='post_details'),
    path('create_post/', CreatePostView.as_view(), name='create_post'),
]