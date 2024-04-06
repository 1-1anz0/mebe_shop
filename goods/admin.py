from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Categories)
class CatgoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'quantity', 'price', 'discount']
    list_editable = ['quantity', 'price', 'discount']
    search_fields = ['title', 'description']
    list_filter = ['category', 'discount', 'price']
    fields = [
        'title',
        'category',
        'image',
        'description',
        ('price', 'discount'),
        'quantity',
        'slug',
    ]