import pytest
from cookbook.models import Ingredients, Pictures, Recipe, Tags


@pytest.mark.django_db
def test_creation_db():
    """Check amount of created objects using admin site."""
    ingredients_lst = [
        Ingredients(title="bread", description="bread"),
        Ingredients(title="onion", description="onion"),
    ]
    Ingredients.objects.bulk_create(ingredients_lst)

    Tags.objects.create(title="tag1")

    recipes_lst = [
        Recipe(title="Test recipe 1", description="tratata", instruction="trt", cook_time=20)
    ]

    Recipe.objects.bulk_create(recipes_lst)
    Recipe.objects.get(title="Test recipe 1").tags.add(Tags.objects.get(title='tag1'))
    recipe_count = Recipe.objects.all().count()
    assert recipe_count == 1