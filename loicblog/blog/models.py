from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    body = MarkdownxField()

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('home')
    
    @property
    def formatted_markdown(self):
        return markdownify(self.body)

