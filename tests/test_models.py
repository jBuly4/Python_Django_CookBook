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


