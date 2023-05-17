from recipe import Recipe
import datetime


class Book:

    def __init__(self, name: str):
        """
        Class constructor
        """
        try:
            self.name = self.__check_name(name)
            self.creation_date = self.last_update = datetime.datetime.now()
            self.recipes_list = {
                "starter": [],
                "lunch": [],
                "dessert": []
            }
        except (TypeError, ValueError) as error:
            print(error)
            exit(1)

    def __str__(self) -> str:
        """
        Return the string to print with the book info
        """
        return f"""Book name: {self.name}
Creation date: {self.creation_date}
Last update: {self.last_update}
Recipes: {self.recipes_list}"""

    def __check_name(self, name: str) -> str:
        """
        Check if the name is a string
        """
        if not isinstance(name, str):
            raise TypeError("Error: Book.name must be a string")
        elif not name:
            raise ValueError("Error: Book.name must not be empty")
        return name

    def get_recipe_by_name(self, name: str) -> Recipe:
        """Prints a recipe by its name and returns the instance"""
        if not isinstance(name, str):
            raise TypeError("Error: Book.get_recipe_by_name() takes a string")
        for recipe_type in self.recipes_list:
            for recipe in self.recipes_list[recipe_type]:
                if recipe.name == name:
                    print(recipe)
                    return recipe
        raise ValueError(f"Error: Recipe {name} not found")

    def get_recipes_by_types(self, recipe_type: str) -> list:
        """Get all recipe names for a given recipe_type"""
        if not isinstance(recipe_type, str):
            raise TypeError("Error: Book.get_recipes_by_types()"
                            + " takes a string")
        if recipe_type not in self.recipes_list:
            raise ValueError(f"Error: Recipe type {recipe_type} not found")
        return self.recipes_list[recipe_type]

    def add_recipe(self, recipe: Recipe):
        """Add a recipe to the book and update last_update"""
        if not isinstance(recipe, Recipe):
            raise TypeError("Error: Book.add_recipe() takes a Recipe object")
        self.get_recipes_by_types(recipe.recipe_type).append(recipe)
        self.last_update = datetime.datetime.now()
