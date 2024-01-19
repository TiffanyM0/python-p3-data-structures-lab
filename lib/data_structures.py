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
    pass
    name_food = []
    for x in spicy_foods: 
        if "name" in x :
            val = x.get("name")
            name_food.append(val)
    return name_food


def get_spiciest_foods(spicy_foods):
    pass
    spicy = []
    for x in spicy_foods:
        if "heat_level" in x:
            val = x.get("heat_level")
            if val > 5:
                spicy.append(x)
    return spicy


def print_spicy_foods(spicy_foods):
    pass
    new_spicy = []
    for x in spicy_foods:
        food = x.get("name")
        emoji = x.get("heat_level") * "🌶"
        cuisine = x.get("cuisine")
        x.update({"heat_level" : f"{emoji}"})
        new_spicy.append({f"{food} ({cuisine}) | heat_level: {emoji}"})
    list = f"{new_spicy[0]}         \n" + f"{new_spicy[1]}   \n" + f"{new_spicy[2]}      \n"
    return list


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    pass

def print_spiciest_foods(spicy_foods):
    pass

def get_average_heat_level(spicy_foods):
    pass

def create_spicy_food(spicy_foods, spicy_food):
    pass
