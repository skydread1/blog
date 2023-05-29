from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import CreatePostForm, EditPostForm
from django.urls import reverse_lazy

## Class-Based Views (CBVs)

### Category

class CategoryView(DetailView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'category'
    slug_field = 'name'
    slug_url_kwarg = 'cat_name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.object
        posts = Post.objects.filter(category=category)
        context['category_posts'] = posts
        return context

class CreateCategoryView(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'create_category.html'

### Post

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-date']

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