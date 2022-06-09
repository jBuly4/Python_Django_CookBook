from django.urls import path, include
from . import views

app_name = 'cookbook'

urlpatterns = [
    path('', views.recipe_lst, name='recipe_lst'),
    path('<str:title>/', views.recipe_detail, name='recipe_detail'),  # Django3 by example p29
]