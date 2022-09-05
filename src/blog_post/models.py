from django.db import models
from django.contrib.auth.models import User

from django.utils.text import slugify
from datetime import datetime



class Category(models.Model):
    name = models.CharField(max_length=15)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

class Post(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField()
    content = models.TextField()
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    date = models.DateTimeField()
    isPublished = models.BooleanField()
    categories = models.ManyToManyField(Category)

    def save(self, *args, **kwargs):

        if not self.date:
            self.date = datetime.now

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def get_categories(self):
        categories = ''
        for i in self.categories.all():
            categories += ' ' + str(i)
        return categories
