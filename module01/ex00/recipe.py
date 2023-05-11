class Recipe:
    name: str
    cooking_lvl: int
    cooking_time: int
    ingredients: 'list[str]'
    recipe_type: str
    description: str

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
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.recipe_type = recipe_type
        self.description = description

    def __str__(self):
        """
        Return the string to print with the recipe info
        """
        return self.description
