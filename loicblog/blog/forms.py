from django import forms
from django.contrib.auth.models import User
from .models import Post, Category
from markdownx.fields import MarkdownxFormField

class CreatePostForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label=None)
    author = forms.ModelChoiceField(queryset=User.objects.none(), empty_label=None)

    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'My post title'}),
            'author': forms.Select(attrs={'readonly': True}),  # Non-editable field
            'date': forms.DateInput(attrs={'type': 'date'}),
            'body': MarkdownxFormField(),
        }

    def __init__(self, *args, **kwargs):
        current_user = kwargs.pop('current_user')
        super().__init__(*args, **kwargs)
        self.fields['author'].queryset = User.objects.filter(username=current_user.username)
        self.initial['category'] = Category.objects.first()
        self.initial['author'] = current_user.pk


class EditPostForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label=None)
    author = forms.ModelChoiceField(queryset=User.objects.none(), empty_label=None)

    class Meta:
        model = Post
        fields = ['title', 'author', 'date', 'category', 'body']
        widgets = {
            'title': forms.TextInput(),
            'author': forms.Select(attrs={'readonly': True}),  # Non-editable field
            'date': forms.DateInput(attrs={'type': 'date'}),
            'body': MarkdownxFormField(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].initial = self.instance.category
        self.fields['author'].queryset = User.objects.filter(username=self.instance.author.username)
