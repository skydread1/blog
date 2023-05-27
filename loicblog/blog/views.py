from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

## Class-Based Views (CBVs)

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class PostDetailsView(DetailView):
    model = Post
    template_name = 'post_details.html'