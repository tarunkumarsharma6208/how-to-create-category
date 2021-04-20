from django.shortcuts import render, get_object_or_404
from .models import *


def home(request):
    category = Category.objects.all()
    return render(request, 'home.html', {"category": category})


def detail(request, cat_slug, slug):
    obj = get_object_or_404(Products, category__slug=cat_slug, slug=slug)
    return render(request, 'detail.html', {'obj': obj})
