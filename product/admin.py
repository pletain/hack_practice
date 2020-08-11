from django.contrib import admin
from .models import Product

# Register your models here.
# admin.site.register(Post)
@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'desc',
        'price',
        'cnt',
        'content',
        'view_count',
        'created_at',
    )
    search_fields = (
        'name',
    )