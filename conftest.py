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


@pytest.fixture()
def create_recipe_factory(db):
    """Fixture factory to create 1 recipe with ingredients and tags."""
    def create_recipe(
            recipe_title: str,
            recipe_description: str,
            recipe_instruction: str,
            recipe_cook_time: int,
            ingredients_lst: list = [],
            tags_lst: list = []
    ):

        Recipe.objects.create(
            title=recipe_title, description=recipe_description,
            instruction=recipe_instruction, cook_time=recipe_cook_time
            )

        for ingredient in ingredients_lst:
            Ingredients.objects.create(title=ingredient.title, description=ingredient.description)
            Recipe.objects.get(title=recipe_title).ingredients.add(Ingredients.objects.get(title=ingredient.title))

        for tag in tags_lst:
            Tags.objects.create(title=tag.title)
            Recipe.objects.get(title=recipe_title).tags.add(Tags.objects.get(title=tag.title))

        return Recipe.objects
    return create_recipe


@pytest.fixture()
def new_recipe(db, create_recipe_factory):
    return create_recipe_factory()
