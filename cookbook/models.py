from django.db import models
from django.urls import reverse  # Django3 by example p30

# Create your models here.


class Ingredients(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Ingredients'


class Tags(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Tags'


class Recipe(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    instruction = models.TextField()
    ingredients = models.ManyToManyField(
            Ingredients,
            related_name='recipe'
    )
    tags = models.ManyToManyField(
            Tags,
            related_name='recipe'
    )
    cook_time = models.PositiveIntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse(
                'recipe_detail',
                args=[self.title, ]  # Django3 by example p30
        )

    def __str__(self):
        return self.title

    def get_pictures(self):
        return self.pictures.all()


class Pictures(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/')
    recipe = models.ForeignKey(
            Recipe,
            related_name='pictures',
            on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Pictures'


