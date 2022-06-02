from django.contrib import admin
from .models import Recipe, Ingredients, Tags, Pictures

# Register your models here.

admin.site.register(Ingredients)
admin.site.register(Recipe)
admin.site.register(Tags)
admin.site.register(Pictures)
