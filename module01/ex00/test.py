# from book import Book
from recipe import Recipe

if __name__ == "__main__":
    tourte = Recipe(name="test_name", cooking_lvl=0, cooking_time=5,
                    ingredients=["a", "b"], recipe_type="aaaa",
                    description="test_description")
    to_print = str(tourte)
    print(to_print)
