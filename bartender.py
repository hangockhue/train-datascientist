import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
            }

ingredients = {"strong": ["glug of rum", "slug of whisky", "splash of gin"],
               "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
               "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
               "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
               "fruity": ["slice of orange", "dash of cassis", "cherry on top"], }
drink = []
value = []

def select_ingredints():
    for i in questions.values():

        print(i + " Choose 1 for Yes, 0 for No")
        s = input("")
        value.append(int(s))
    return value
def ingredients_drink():
    if value[0]:
        drink.append(random.choice(ingredients['strong']))
    else:
        print("Only drinks strong here")
        return
    if value[1]:
        drink.append(random.choice(ingredients['salty']))
    if value[2]:
        drink.append(random.choice(ingredients['bitter']))
    if value[3]:
        drink.append(random.choice(ingredients['sweet']))
    if value[4]:
        drink.append(random.choice(ingredients['fruity']))
    return print("Your drink is " + (' add ').join(drink))

select_ingredints()
ingredients_drink()
