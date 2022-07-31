from pprint import pprint
import os

with open('cook_book.txt') as cook_file:
    nomenclature = ['ingredient_name', 'quantity', 'measure']
    menu = {}
    ingredients = {}
    name_dish = cook_file.readline().strip()
    for line in cook_file:
        number = int(line)
        lines = []
        for item in range(number):
            data = cook_file.readline().strip().split(' | ')
            data[1] = int(data[1])
            for index, ingredient in enumerate(nomenclature):
                ingredients[ingredient] = data[index]
            ingredients_copy = ingredients.copy()
            lines.append(ingredients_copy)
        menu[name_dish] = lines
        cook_file.readline()
        name_dish = cook_file.readline().strip()
    pprint(menu)

def get_shop_list(dish, person):
    ingredients = []
    for name_dish in dish:
        ingredients.extend(menu.get(name_dish))
    product_list = {}
    product_quantity = {}
    for ingredient in ingredients:
        product = ingredient.get('ingredient_name')
        if product in product_list.keys():
            product_quantity['measure'] = ingredient.get('measure')
            product_quantity['quantity'] = product_list.get(product).get('quantity') + ingredient.get('quantity') * person
            product_quantity_copy = product_quantity.copy()
            product_list[product] = product_quantity_copy
        else:
            product_quantity['measure'] = ingredient.get('measure')
            product_quantity['quantity'] = ingredient.get('quantity') * person
            product_quantity_copy = product_quantity.copy()
            product_list[product] = product_quantity_copy
    return pprint(product_list)

get_shop_list(['Омлет', 'Фахитос'], 3)



# Задача 3

path = r'D:\Netology\Home 7\home_7\123'
os.chdir(path)
file_nomenclature = os.listdir(path)

file_list = []
line_number = []
file_list_number = {}

def read_file(file_name):
    with open(file_name) as file:
        file_list_ = file.readlines()
        file_list_number_ = len(file_list_)
    return(file_list_, file_list_number_)

for file_name in file_nomenclature:
    file_list, line_number_int = read_file(file_name)
    file_list_number[line_number_int] = [file_name, file_list]
    line_number.append(line_number_int)

line_number.sort()

os.chdir(r'D:\Netology\Home 7\home_7')

with open('union.txt', 'w') as file_union:
    for i in line_number:
        file_union.write(file_list_number.get(i)[0] + '\n')
        file_union.write(str(i) + '\n')
        file_union.write(''.join(file_list_number.get(i)[1]) + '\n')
