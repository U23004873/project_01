# Задача 1.1.

# Есть строка с перечислением песен

my_favorite_songs = 'Потеряй мгновение, останься в живых, своего рода сказка, начни меня, Новое спасение'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца

# txt = my_favorite_songs
# print (txt [0:17] + txt [68:83] + txt [18:35] + txt [-27:-16])

txt = my_favorite_songs
x = txt.replace('Потеряй мгновение, останься в живых, своего рода сказка, начни меня, Новое спасение',
    'Потеряй мгновение Новое спасение останься в живых начни меня')
print(x)







# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.
