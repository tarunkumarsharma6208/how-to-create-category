from django.contrib import admin
from .models import *


@admin.register(Category)
class adminCategory(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Products)
class adminProducts(admin.ModelAdmin):
    list_display = ['name', 'price']
    prepopulated_fields = {'slug': ('name',)}
