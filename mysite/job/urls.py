from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.index),
    path('signup/',views.signup),
    path('explore/',views.Explore),
    path('signin/',views.signin),
    path('signup/',views.code),
]