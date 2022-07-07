from django.urls import path, include
from . import views

app_name = 'cookbook'

urlpatterns = [
    path('', views.recipe_lst, name='recipe_lst'),
    path('ingredients/', views.ingredient_lst, name='ingredients'),  # dunno why, but if it is after recipe_detail
    # link then views.recipe_detail raises error
    path('tags/', views.tag_lst, name='tags'),
    path('<str:title>/', views.recipe_detail, name='recipe_detail'),  # Django3 by example p29
    path('ingredients/<str:title>/', views.ingredient_detail, name='ingredient_detail'),
    path('tags/<str:title>/', views.tags_view, name='tags_page'),
]