from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import CreatePostForm, EditPostForm
from django.urls import reverse_lazy

## Class-Based Views (CBVs)

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']

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

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')