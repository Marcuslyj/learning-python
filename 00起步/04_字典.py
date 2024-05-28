alien_0 = {'color': 'green', 'points': 5}
# print(alien_0['color'])

# for key, value in alien_0.items():
#     print(key, value)

# for key in alien_0.keys():
#     print(key)

# for value in alien_0.values():
#     print(value)

# 作用域？

# # 这遍历顺序？？
# for language in set(['python', 'python', 'ruby']):
#     print(language.title())

# for language in (['python', 'python', 'ruby']):
#     print(language.title())

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    'anotherPizza': {
        'crust': 'thin',
        'toppings': ['pepperoni', 'extra cheese']
    },
    'alien_0': alien_0
}

c = {'aa': 1}
pizza['all'] = c
# pizza['alien_0'] = alien_0

print(pizza)
