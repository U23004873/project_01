# Задача 2.3.

# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'Один'
# переключить_ит_ап(3) -> 'Три'
# switch_it_up(10000) -> Нет
# Использовать условный оператор if-elif-else нельзя!
# switch_it_up def(число):


# Как смогла)

# 1. Вариант

# d = {0:'ноль', 1:'один', 2:'два', 3:'три', 4:'четыре', 5:'пять', 6:'шесть', 7:'семь', 8:'восемь', 9:'девять'}
# z = int(input('Введите запрос: '))
# try:
#     print(d[z])
# except KeyError:
#     print('Такого ключа нету в словаре')


# 2. Вариант

# user_input = input("Введите число от 0 до 9: ")
# number = int(user_input)
# print('Вы ввели', number)
         
# dictionary = {0:'ноль', 1:'один', 2:'два', 3:'три', 4:'четыре', 5:'пять', 6:'шесть', 7:'семь', 8:'восемь', 9:'девять'}

# def switch_it_up(number):
#     if number in dictionary:
#         print("Это число", dictionary[number] )
#     else:
#         print("Такого числа нет")
# print(switch_it_up(number))




# 3. Вариант

# user_input = input("Введите число от 0 до 9: ")
# number = (user_input)
# print('Вы ввели', number)
# dictionary = {0:'ноль', 1:'один', 2:'два', 3:'три', 4:'четыре', 5:'пять', 6:'шесть', 7:'семь', 8:'восемь', 9:'девять'}
# def switch_it_up(dictionary):
#     X = dictionary.get(1)
# print(switch_it_up(dictionary))