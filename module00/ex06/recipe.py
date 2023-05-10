
cookbook: dict = {
    "sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10,
    },
    "cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60,
    },
    "salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15,
    },
}


def print_recipe_names():
    """
    Print the recipe names
    """
    print("The cookbook contains:")
    for recipe_name in cookbook:
        print(f"- {recipe_name}")


def print_recipe():
    """
    Print a recipe from the cookbook
    """
    recipe_name: str = input(
        "Please enter the recipe's name to get its details:\n")
    if (recipe_name in cookbook):
        print(f"Recipe for {recipe_name}:")
        print(f"Ingredients list: {cookbook[recipe_name]['ingredients']}")
        print(f"To be eaten for {cookbook[recipe_name]['meal']}")
        print(f"Takes {cookbook[recipe_name]['prep_time']} minutes of cooking")
    else:
        print(f"ERROR, {recipe_name} is not in the cookbook")


def delete_recipe():
    """
    Delete a recipe from the cookbook
    """
    recipe_name: str = input(
        "Please enter the recipe's name to delete it:\n")
    if (recipe_name in cookbook):
        del cookbook[recipe_name]
        print(f"{recipe_name} has been deleted")
    else:
        print(f"ERROR, {recipe_name} is not in the cookbook")


def add_recipe():
    """
    Add a recipe to the cookbook
    """
    recipe_name: str = input(
        "Please enter the recipe's name to add it:\n")
    if (recipe_name in cookbook):
        print(f"ERROR, {recipe_name} is already in the cookbook")
    else:
        ingredients: list = []
        print("Please enter the ingredients : (Enter an empty line to finish)")
        while (True):
            ingredient: str = input()
            if (ingredient == ""):
                break
            ingredients.append(ingredient)
        meal: str = input(
            "Please enter the recipe's meal type:\n")
        prep_time: int = int(input(
            "Please enter the recipe's preparation time in minutes:\n"))
        if (prep_time < 0):
            print("ERROR, the preparation time must be positive")
            return
        cookbook[recipe_name] = {
            "ingredients": ingredients,
            "meal": meal,
            "prep_time": prep_time,
        }
        print(f"{recipe_name} has been added to the cookbook")


def print_options():
    print("List of available actions:")
    print("  1- print_recipe_names")
    print("  2- print_recipe")
    print("  3- delete_recipe")
    print("  4- add_recipe")
    print("  5- quit")


if __name__ == "__main__":
    print("Welcome to the cookbook!")
    while (True):
        print_options()
        try:
            action: int = int(input("Please select an action:\n"))
            print()
            if (action == 1):
                print_recipe_names()
            elif (action == 2):
                print_recipe()
            elif (action == 3):
                delete_recipe()
            elif (action == 4):
                add_recipe()
            elif (action == 5):
                print("Cookbook closed.")
                exit(0)
            else:
                print("ERROR, invalid action")
        except ValueError:
            print("\nERROR, invalid action\n")
            continue
        except EOFError:
            print("\nERROR, invalid action\n")
            continue
        except KeyboardInterrupt:
            print("\nERROR, invalid action\n")
            continue
        print()
