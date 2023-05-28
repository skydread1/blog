from django import forms
from .models import Post

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'My post title'}),
            'author': forms.Select(),
            'date': forms.DateInput(attrs={'type': 'date'}),
            'body': forms.Textarea(attrs={'placeholder': 'My post content'}),
        }

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'date', 'body']
        widgets = {
            'title': forms.TextInput(),
            'date': forms.DateInput(attrs={'type': 'date'}),
            'body': forms.Textarea(),
        }