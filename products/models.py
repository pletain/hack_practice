from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50, null=False)
    desc = models.CharField(max_length=50, null=False)
    price = models.IntegerField(null=True)
    cnt = models.IntegerField(null=True)
    view_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    image = models.ImageField(upload_to='images/', null=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    score = models.IntegerField(null=True)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name='comments')
