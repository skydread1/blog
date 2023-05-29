from django import forms
from .models import Post, Category
from markdownx.fields import MarkdownxFormField

choices = Category.objects.all().values_list('name', 'name')
choice_list = [choice for choice in choices]

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'My post title'}),
            'author': forms.Select(),
            'date': forms.DateInput(attrs={'type': 'date'}),
            'category': forms.Select(choices=choice_list),
            'body': MarkdownxFormField(),
        }

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'date', 'category', 'body']
        widgets = {
            'title': forms.TextInput(),
            'date': forms.DateInput(attrs={'type': 'date'}),
            'category': forms.Select(choices=choice_list),
            'body': MarkdownxFormField(),
        }