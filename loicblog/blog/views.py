from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import CreatePostForm, EditPostForm

## Class-Based Views (CBVs)

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class PostDetailsView(DetailView):
    model = Post
    template_name = 'post_details.html'

class CreatePostView(CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'create_post.html'

class EditPostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'edit_post.html'