import pprint
cook_book = {}
#     cook_book = {
#     'Омлет': [
#         {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#         {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#         {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ],
#     'Утка по-пекински': [
#         {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
#         {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
#         {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
#         {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
#     ],
#     'Запеченный картофель': [
#         {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
#         {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
#         {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
#     ]
# }
# {
#   'Картофель': {'measure': 'кг', 'quantity': 2},
#   'Молоко': {'measure': 'мл', 'quantity': 200},
#   'Помидор': {'measure': 'шт', 'quantity': 4},
#   'Сыр гауда': {'measure': 'г', 'quantity': 200},
#   'Яйцо': {'measure': 'шт', 'quantity': 4},
#   'Чеснок': {'measure': 'зубч', 'quantity': 6}
# }

with open("recipes.txt", encoding='utf8') as f:
    for ingredient in f:
        key = ingredient.strip().lower()
        cook_book[key] = []
        for _ in range(int(f.readline())):
            ingredient_name, quantity, measure = f.readline().strip().split(' | ')
            cook_book[key].append({'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure})
        f.readline()
# pprint.pprint(cook_book)
print(cook_book)
def get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2):
    shop_list = {}
