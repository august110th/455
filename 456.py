cook_book = {}
#   'Омлет': [
#     {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#     {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ],
#   'Утка по-пекински': [
#     {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
#     {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
#     {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
#     {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
#     ],
#   'Запеченный картофель': [
#     {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
#     {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
#     {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
#     ]
#   }

with open("recipes.txt", encoding="utf8") as f:
  for ingredient in f:
    key = ingredient.strip()
    cook_book[key] = []
    for _ in range(int(f.readline())):
      ingredient_name, quantity, measure = f.readline().strip().split(' | ')
      cook_book[key].append({'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure})
    f.readline()
print(cook_book)




#   ingredient_name = f.readline()
#   quantity = int(f.readline())
#   ing_list =[]
#   for _ in range(quantity):
#     ingr = f.readline().strip()
#     splited = ingr.split("|")
#     ing_list.append(splited)
#   f.readline()
# print(ing_list)
#
# print(cook_book)
