class Recipe:
    name: str
    cooking_lvl: int
    cooking_time: int
    ingredients: 'list[str]'
    description: str
    recipe_type: str

    def __init__(self,
                 name: str
                 ):
        self.name = name


if __name__ == "__main__":
    tourte = Recipe(name="testaaa")
    print(tourte.name)
