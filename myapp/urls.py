from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:cat_slug>/<slug:slug>/', views.detail, name='detail'),
]