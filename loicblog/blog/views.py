from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm

## Class-Based Views (CBVs)

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class PostDetailsView(DetailView):
    model = Post
    template_name = 'post_details.html'

class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create_post.html'