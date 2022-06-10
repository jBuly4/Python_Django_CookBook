from django.urls import path, include
from . import views

app_name = 'cookbook'

urlpatterns = [
    path('', views.recipe_lst, name='recipe_lst'),
    path('<str:title>/', views.recipe_detail, name='recipe_detail'),  # Django3 by example p29
    path('ingredient/<str:title>/', views.ingredient_detail, name='ingredient_detail'),
    path('tags/<str:title>/', views.tags_view, name='tags_page'),
]