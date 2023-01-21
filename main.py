# base_rate = 10
# region = 'Дальний восток'
#
# user_region = input('В каком регионе проживаете? ')
#
# if user_region == region:
#     base_rate = 2
#     print(f'Ваша финальная ставка составляет: {base_rate}%')
#
# if user_region != region:
#     user_children = int(input('Сколько у вас детей? '))
#     if_salary = input('Получаете ли вы зарплату от нашего банка? ').upper()
#     insurance = input('Оформлено ли страхование? ').upper()
#
#     if user_children > 3:
#         base_rate -= 1
#     if if_salary == 'ДА':
#         base_rate -= 0.5
#     if insurance == 'ДА':
#         base_rate -= 1.5
#     print(f'Ваша финальная ставка составляет: {base_rate}%')


from pprint import pprint


# словарь {меню: ингредиенты, количество, единица измерения}
def prepare_dict(file_name: str) -> dict:
    result: dict = dict()
    with open(file_name, 'r', encoding='utf8') as file:
        for line in file:
            dish_name = line.strip()
            records_quantity = int(file.readline())
            cook_book = []
            for ingredient in range(records_quantity):
                ingredient_name, quantity, measure = file.readline().split(' | ')
                cook_book.append(
                    {'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure.strip()}
                )
            result[dish_name] = cook_book
            file.readline()
    return result


cook_book = prepare_dict('recipes.txt')


# словарь с названием ингредиентов и множителем по количеству блюд для персон
# def get_shop_list_by_dishes(dishes, person_count):
#     shop_list = {}
#     for key, values in cook_book.items():
#         for dishes_name in dishes:
#             if dishes_name == key:
#                 for res in values:
#                     if res['ingredient_name'] not in shop_list.keys():
#                         shop_list[res['ingredient_name']] = {'quantity': res['quantity'] * person_count,
#                                                              'measure': res['measure']}
#                     else:
#                         shop_list[res['ingredient_name']] = {'quantity': res['quantity']}
#     return shop_list

def get_shop_list_by_dishes(dishes, person_count):
    dict_dishes = {}
    for dish in dishes:
        if dish in cook_book:
             for ingridient in cook_book[dish]:
                dict_dishes[ingridient['ingredient_name']] = {'quantity': ingridient['quantity'] * person_count, 'measure': ingridient['measure']}
                print(ingridient)
    return dict_dishes


# print(cook_book)

# print()
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 250))
