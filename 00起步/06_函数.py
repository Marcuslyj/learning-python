# def greet_user():
#     """显示简单的问候语"""
#     print("Hello!")

# greet_user()

# # 关键字实参
# def describe_pet(animal_type, pet_name):
#     """显示宠物的信息"""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# # describe_pet('hamster', 'harry')
# describe_pet(pet_name='hamster', animal_type='harry')

# obj = {'name': 'lala'}
# obj2 = {'obj': obj}
# obj2['obj']['name'] = 'lala2'
# print(obj)

# # 传递任意数量的实参
# def make_pizza(size, *toppings):
#     """打印顾客点的所有配料"""
#     print(toppings)
#     print(len(toppings))

# make_pizza('fr', 'en')


# 使用任意数量的关键字实参
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert',
                             'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
