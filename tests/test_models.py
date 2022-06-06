from collections import namedtuple


ingredients_tup = namedtuple('ingredients', ['title', 'description'])
tags_tup = namedtuple('tags', ['title'])


def test_db_recipes(create_recipes):
    """Check recipes and their fields."""
    assert create_recipes.all().count() == 2
    assert create_recipes.get(title="Test recipe 1").title == "Test recipe 1"
    assert create_recipes.get(title="Test recipe 2").title == "Test recipe 2"
    assert create_recipes.get(title="Test recipe 1").description == "tratata"
    assert create_recipes.get(title="Test recipe 2").description == "trututu"
    assert create_recipes.get(title="Test recipe 1").instruction == "trt1"
    assert create_recipes.get(title="Test recipe 2").instruction == "trt212"
    assert create_recipes.get(title="Test recipe 1").cook_time == 20
    assert create_recipes.get(title="Test recipe 2").cook_time == 15
    assert len(create_recipes.filter(tags__title="tag1")) == 1
    assert len(create_recipes.filter(tags__title="tag2")) == 1
    assert create_recipes.filter(tags__title="tag1")[0].title == "Test recipe 1"
    assert create_recipes.filter(tags__title="tag2")[0].title == "Test recipe 2"


def test_db_recipes_factory(create_recipe_factory):
    ingredients_lst = [
        ingredients_tup("bread", "bread description"),
        ingredients_tup("onion", "onion description"),
    ]

    tags_lst = [
        tags_tup("tag1"),
        tags_tup("tag2")
    ]

    recipe = create_recipe_factory("Test recipe 1",
                                   "Description of test recipe 1",
                                   "Instruction of test recipe 1",
                                   10,
                                   ingredients_lst,
                                   tags_lst)

    assert recipe.all().count() == 1
    assert recipe.filter(tags__title="tag1")[0].title == "Test recipe 1"
    assert recipe.get(title="Test recipe 1").tags.count() == 2
    assert recipe.get(title="Test recipe 1").ingredients.count() == 2
    assert recipe.get(title="Test recipe 1").instruction == "Instruction of test recipe 1"
    assert recipe.get(title="Test recipe 1").description == "Description of test recipe 1"
    assert recipe.get(title="Test recipe 1").cook_time == 10


