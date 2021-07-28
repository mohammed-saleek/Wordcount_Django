from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name = "homepage"),
    path('word-counting/', views.result, name = 'word_count')
]