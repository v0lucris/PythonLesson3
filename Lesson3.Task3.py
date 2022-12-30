# 3. Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.
import math
#   Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import sys

lst1 = [1.1, 1.2, 3.1, 5, 10.01]

# i = 0
# count = None
# for i in range( 0, len(lst1)):
#     count = round((((lst1[i] * 10) % 10) / 10), 10)
#     if count !=0:
#         lst2.append(count)
#
# max_count = max(lst2)
# min_count = min(lst2)
# result = float (max_count - min_count)
#
# print(result)

# New version
float_path = list(map(lambda count: (((count * 10) % 10) / 10), lst1))
float_path.remove(0)
print(max(float_path)-min(float_path))

