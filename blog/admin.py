from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from .models import Categoria, Post
# Register your models here.



admin.site.register(Categoria, )
admin.site.register(Post, )

