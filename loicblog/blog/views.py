from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post, Category
from .forms import CreatePostForm, EditPostForm

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = context['object_list']
        return context

class PostDetailsView(DetailView):
    model = Post
    template_name = 'post_details.html'

class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'create_post.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['current_user'] = self.request.user
        return kwargs

class EditPostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'edit_post.html'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['author'].disabled = True
        form.fields['author'].queryset = User.objects.filter(username=self.request.user.username)
        return form

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

## Class-Based Views (FBVs) - for htmx

def search_post(request):
    search_text = request.POST.get('search')
    results = Post.objects.filter(title__icontains=search_text).order_by('-date')
    context = {"results": results, "search_text": search_text}
    return render(request, 'partials/search-results.html', context)
