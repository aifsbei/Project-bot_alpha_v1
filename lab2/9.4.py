m_number_of_products = int(input())
fridge = [input() for i in range(m_number_of_products)]
n_number_of_recipes = int(input())
recipes = []
names = []
for i in range(n_number_of_recipes):
    recipe = {}
    name_of_recipe = input()
    names.append(name_of_recipe)
    number_of_ingredients = int(input())
    ingredients = [input() for j in range(number_of_ingredients)]
    recipe = {'name': name_of_recipe, 'ingredients': ingredients}
    recipes.append(recipe)
for recipe in recipes:
    print(recipe['name']) if (set(recipe['ingredients']) & set(fridge)) == set(recipe['ingredients']) else None