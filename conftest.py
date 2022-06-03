import pytest

from cookbook.models import Ingredients, Pictures, Recipe, Tags


@pytest.fixture()
def create_recipes(db):
    """Create recipes with all fields."""
    ingredients_lst = [
        Ingredients(title="bread", description="bread"),
        Ingredients(title="onion", description="onion"),
    ]
    Ingredients.objects.bulk_create(ingredients_lst)

    Tags.objects.create(title="tag1")
    Tags.objects.create(title="tag2")

    recipes_lst = [
        Recipe(title="Test recipe 1", description="tratata", instruction="trt1", cook_time=20),
        Recipe(title="Test recipe 2", description="trututu", instruction="trt212", cook_time=15)
    ]

    Recipe.objects.bulk_create(recipes_lst)
    Recipe.objects.get(title="Test recipe 1").tags.add(Tags.objects.get(title='tag1'))
    Recipe.objects.get(title="Test recipe 1").ingredients.add(Ingredients.objects.get(title='bread'))

    Recipe.objects.get(title="Test recipe 2").tags.add(Tags.objects.get(title='tag2'))
    Recipe.objects.get(title="Test recipe 2").ingredients.add(Ingredients.objects.get(title='onion'))

    return Recipe.objects  # if we return object then we don't need @pytest.mark.django_db before test func