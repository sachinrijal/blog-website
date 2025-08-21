from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=15,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'categories'


class Blogs(models.Model):

    title = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(blank=True,unique=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images')
    short_body = models.TextField(max_length=1000)
    body = models.TextField(max_length=2000)

    STATUS_CHOICE =[
        (0, 'draft'),
        (1 ,'Published'),
    ]

    status = models.IntegerField(choices = STATUS_CHOICE , default = 0)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

    class Meta:
        verbose_name_plural = 'blogs'

    def __str__(self):
        return self.title[0:10]