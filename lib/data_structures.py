spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = []
    for item in spicy_foods:
        names.append(item["name"])
    return names
    pass

def get_spiciest_foods(spicy_foods):
    spiciest_food = []
    for item in spicy_foods:
        if item["heat_level"] > 5:
            spiciest_food.append(item)
    return spiciest_food
    pass

def print_spicy_foods(spicy_foods):
    for item in spicy_foods:
        print(f"{item['name']} ({item['cuisine']}) | Heat Level: {'🌶' * item['heat_level']}")
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for item in spicy_foods:
        if item["cuisine"] == cuisine:
            return item
    pass

def print_spiciest_foods(spicy_foods):
    for item in spicy_foods:
        if item["heat_level"] > 5:
           print(f"{item['name']} ({item['cuisine']}) | Heat Level: {'🌶' * item['heat_level']}") 
    pass

def get_average_heat_level(spicy_foods):
    spice_list = []
    for item in spicy_foods:
        spice_list.append(item["heat_level"])
    total_spice = sum(spice_list)
    return total_spice / len(spice_list)
    pass

def create_spicy_food(spicy_foods, spicy_food):
    new_spicy_foods = spicy_foods.copy()
    new_spicy_foods.append(spicy_food)
    return new_spicy_foods
    pass
