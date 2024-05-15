from django.urls import re_path as url
from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('form/', views.form, name='form'),
    path('add_album/', views.album_form, name='album_form'), 
    path('add_musician/', views.musician_form, name='musician_form')
]