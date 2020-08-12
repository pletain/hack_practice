from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50, null=False)
    desc = models.CharField(max_length=50, null=False)
    price = models.IntegerField(null=False)
    cnt = models.CharField(max_length=50, null=False)
    content = models.TextField()
    view_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    image = models.ImageField(upload_to='images/', null=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)

class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name='comments')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)