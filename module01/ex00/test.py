from book import Book
from recipe import Recipe


def test_recipe():

    print("\nRECIPE CLASS TESTS :\n")

    # # Test recipe with an invalid name
    # Recipe(name="", cooking_lvl=1, cooking_time=20,
    #        ingredients=["eggs", "flour"],
    #        recipe_type="dessert")

    # # Test recipe with an invalid cooking level
    # Recipe(name="cake", cooking_lvl=-1,
    #        cooking_time=20, ingredients=["eggs", "flour"],
    #        recipe_type="dessert")

    # # Test recipe with an invalid cooking time
    # Recipe(name="cake", cooking_lvl=1,
    #        cooking_time=-20, ingredients=["eggs", "flour"],
    #        recipe_type="dessert")

    # # Test recipe with an invalid ingredients list
    # Recipe(name="cake", cooking_lvl=1,
    #        cooking_time=20, ingredients=[42, "flour"],
    #        recipe_type="dessert")

    # # Test recipe with an invalid recipe type
    # Recipe(name="cake", cooking_lvl=1,
    #        cooking_time=20, ingredients=["eggs", "flour"],
    #        recipe_type="dinner")

    # # Test recipe with an invalid description
    # Recipe(name="cake", cooking_lvl=1,
    #        cooking_time=20, ingredients=["eggs", "flour"],
    #        recipe_type="dessert", description=42)

    # Test recipe with all valid parameters
    cake = Recipe(name="cake", cooking_lvl=1,
                  cooking_time=20, ingredients=["eggs", "flour"],
                  recipe_type="dessert", description="A delicious cake")

    # Test the __str__ method
    to_print: str = str(cake)
    print(to_print)


def test_book():

    print("\nBOOK CLASS TESTS :\n")

    # # Test book with invalid arguments
    # Book(42)

    # # Test book with an invalid name
    # Book(name="")

    cookbook = Book(name="My CookBook")

    # Test the __str__ method
    print(cookbook)

    print("creation_date: {}".format(cookbook.creation_date))

    cake = Recipe(name="cake", cooking_lvl=3,
                  cooking_time=20, ingredients=["eggs", "flour"],
                  recipe_type="dessert", description="A delicious cake")

    cookies = Recipe(name="cookies", cooking_lvl=2,
                     cooking_time=30,
                     ingredients=["flour", "eggs", "chocolate"],
                     recipe_type="dessert")

    pizza = Recipe(name="pizza", cooking_lvl=1,
                   cooking_time=30, ingredients=["pasta", "tomato", "cheese"],
                   recipe_type="lunch", description="A delicious pizza")

    # Test the add_recipe method

    # try:
    #     cookbook.add_recipe(42)
    # except TypeError as error:
    #     print(error)

    cookbook.add_recipe(cake)
    cookbook.add_recipe(cookies)
    cookbook.add_recipe(pizza)

    # Test the get_recipe_by_name method
    # try:
    #     cookbook.get_recipe_by_name(42)
    # except TypeError as error:
    #     print(error)

    # try:
    #     unknown_recipe = cookbook.get_recipe_by_name("salad")
    #     print(unknown_recipe)
    # except ValueError as error:
    #     print(error)

    try:
        pizza_recipe = cookbook.get_recipe_by_name("pizza")
        print(pizza_recipe)
    except ValueError as error:
        print(error)

    # Test the get_recipes_by_types method
    # try:
    #     cookbook.get_recipes_by_types(42)
    # except TypeError as error:
    #     print(error)

    # try:
    #     cookbook.get_recipes_by_types("dinner")
    # except ValueError as error:
    #     print(error)

    try:
        dessert_recipes = cookbook.get_recipes_by_types("dessert")
        for recipe in dessert_recipes:
            print(recipe)
    except ValueError as error:
        print(error)

    print(cookbook)


def main():
    test_recipe()
    test_book()


if __name__ == "__main__":
    main()
