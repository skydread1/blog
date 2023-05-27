from django.urls import path
from .views import HomeView, PostDetailsView

## map URLs to class-based views
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostDetailsView.as_view(), name='post_details'),
]