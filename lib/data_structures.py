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
        # x.update({"heat_level" : f"{emoji}"})
        new_spicy.append(f"{food} ({cuisine}) | Heat Level: {emoji}")
        foodie = f"{new_spicy[-1]}"
        print(foodie)


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    pass
    for x in spicy_foods:
        deli_cusy = x.get("cuisine")
        if deli_cusy == cuisine:
            return x

def print_spiciest_foods(spicy_foods):
    pass
    #  print_spicy_foods(emoji) + get_spiciest_foods(>5)
    # get spiciest foods and print with emojis
    spiciest = get_spiciest_foods(spicy_foods)
    return print_spicy_foods(spiciest)


def get_average_heat_level(spicy_foods):
    pass
    ave_lvl = []
    for x in spicy_foods:
        val = x.get("heat_level")
        ave_lvl.append(val)
    done = (ave_lvl[0] + ave_lvl[1] + ave_lvl[2])/len(ave_lvl)
    return done

def create_spicy_food(spicy_foods, spicy_food):
    pass
    spicy_foods.append(spicy_food)
    return spicy_foods
