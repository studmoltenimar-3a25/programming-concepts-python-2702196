""" A Functional Breakfast """
def mix_and_cook():
    print('Mixing the ingredients')
    print('Greasing the frying pan')
    print('Pouring the mixture into a frying pan')
    print('Cooking the first side')
    print('Flipping it!')
    print('Cooking the other side\n')

def make_omelette(ingredients):
    mix_and_cook()
    omelette = f'a {ingredients} omelette'
    return omelette

def make_fancy_omelette(*ingredients):
    mix_and_cook()
    omelette = f' a fancy omelette with {len(ingredients)} ingredients'
    return omelette

def make_pancake():
    mix_and_cook()
    pancake = 'a delicious pancake'
    return pancake


# make breakfast for two
Marco_breakfast = make_omelette('Bacon')
Ronaldo_breakfast = make_fancy_omelette('Cheese', 'tomato', 'onion', 'mushroom', 'ham')
print(f"Marco is having {Marco_breakfast}\n")
print(f"Ronaldo is having {Ronaldo_breakfast}\n")

