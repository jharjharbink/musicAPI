from django.urls import re_path
from musicApp import views

urlpatterns = [
    re_path(r'^albums$', views.AlbumAPI)
]