

# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566] -> макс = 566, мин = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> мин = -110, макс = 56
# * [42, 54, 65, 87, 0] -> min = 0, max = 87
# * [5] -> минимум = 5, максимум = 5
# функции max и min использовать нельзя!

# def minimum ( arr ):
#     пройти

# def maximum ( arr ):
#     пройти

arr = [[4,6,2,1,9,63,-134,566],[-52, 56, 30, 29, -54, 0, -110],[42, 54, 65, 87, 0],[5]]
def insertion(data):
  for i in range(len(data)):
    j = i - 1
    key = data[i]
    while data[j] > key and j >= 0:
      data[j + 1] = data[j]
      j -= 1
    data[j + 1] = key
  return data

def minimum(arr):
  for data in arr:
    print ( data, "мин =", insertion(data)[0])

def maximum(arr):
  for data in arr:
    print ( data, "макс =", insertion(data)[len(data)-1])

print(minimum(arr), maximum(arr))    












    