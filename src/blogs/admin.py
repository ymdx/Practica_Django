from django.contrib import admin

# Register your models here.
from blogs.models import Blog, Post, Category

admin.site.register(Blog)
admin.site.register(Post)
admin.site.register(Category)

