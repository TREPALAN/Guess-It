from django.urls import path
from . import views

app_name = 'what_am_i'
urlpatterns = [
    path('', views.index, name='index'),
]