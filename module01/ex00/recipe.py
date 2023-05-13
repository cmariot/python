class Recipe:
    """
    Recipe is a class used to store a recipe in a cook book.
    """

    def __init__(self,
                 name: str,
                 cooking_lvl: int,
                 cooking_time: int,
                 ingredients: 'list[str]',
                 recipe_type: str,
                 description: str = ""
                 ):
        """
        Class constructor
        """
        try:
            self.name = self._check_name(name)
            self.cooking_lvl = self._check_cooking_lvl(cooking_lvl)
            self.cooking_time = self._check_cooking_time(cooking_time)
            self.ingredients = self._check_ingredients(ingredients)
            self.recipe_type = self._check_recipe_type(recipe_type)
            self.description = self._check_description(description)
        except (TypeError, ValueError) as error:
            print(error)
            exit(1)

    def __str__(self) -> str:
        """
        Return the string to print with the recipe info
        """
        return f"""Recipe name: {self.name}
Cooking level: {self.cooking_lvl}
Cooking time: {self.cooking_time}
Ingredients: { ", ".join(self.ingredients)}
Recipe type: {self.recipe_type}
Description: {self.description}"""

    def _check_name(self, name: str) -> str:
        """
        Check if the name is a string
        """
        if not isinstance(name, str):
            raise TypeError("Error: Recipe.name must be a string")
        elif not name:
            raise ValueError("Error: Recipe.name must not be empty")
        return name

    def _check_cooking_lvl(self, cooking_lvl: int) -> int:
        """
        Check if the cooking level is between 1 and 5
        """
        if not isinstance(cooking_lvl, int):
            raise TypeError("Error: Recipe.cooking_lvl must be an integer")
        elif cooking_lvl < 1 or cooking_lvl > 5:
            raise ValueError(
                "Error: Recipe.cooking_lvl must be between 1 and 5")
        return cooking_lvl

    def _check_cooking_time(self, cooking_time: int) -> int:
        """
        Check if the cooking time is positive
        """
        if not isinstance(cooking_time, int):
            raise TypeError("Error: Recipe.cooking_time must be an integer")
        elif cooking_time < 0:
            raise ValueError("Error: Recipe.cooking_time must be positive")
        return cooking_time

    def _check_ingredients(self, ingredients: 'list[str]'):
        """
        Check if the ingredients is a list of strings
        """
        if not isinstance(ingredients, list):
            raise TypeError("Error: Recipe.ingredients must be a list")
        elif not all(isinstance(ing, str) for ing in ingredients):
            raise TypeError(
                "Error: Recipe.ingredients must be a list of strings")
        return ingredients

    def _check_recipe_type(self, recipe_type: str) -> str:
        """
        Check if the recipe type is "starter", "lunch" or "dessert"
        """
        if not isinstance(recipe_type, str):
            raise TypeError("Error: Recipe.recipe_type must be a string")
        elif recipe_type not in ["starter", "lunch", "dessert"]:
            raise ValueError(
                "Error: Recipe.recipe_type must be 'starter',"
                + "'lunch' or 'dessert'")
        return recipe_type

    def _check_description(self, description: str) -> str:
        """
        Check if the description is a string
        """
        if not isinstance(description, str):
            raise TypeError("Error: Recipe.description must be a string")
        return description
