from django import forms
from .models import Post, Category
from markdownx.fields import MarkdownxFormField


class CreatePostForm(forms.ModelForm):
    category = forms.ChoiceField(choices=[])

    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'My post title'}),
            'author': forms.Select(),
            'date': forms.DateInput(attrs={'type': 'date'}),
            'body': MarkdownxFormField(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].choices = Category.objects.all().values_list('name', 'name')


class EditPostForm(forms.ModelForm):
    category = forms.ChoiceField(choices=[])

    class Meta:
        model = Post
        fields = ['title', 'author', 'date', 'category', 'body']
        widgets = {
            'title': forms.TextInput(),
            'date': forms.DateInput(attrs={'type': 'date'}),
            'body': MarkdownxFormField(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].choices = Category.objects.all().values_list('name', 'name')
