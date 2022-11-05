#3. Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.

 #   Пример:

#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import math
lst1 = [1.1, 1.2, 3.1, 5, 10.01]
lst2 = []
count = None
for i in range( 0, len(lst1)):
    count = round((((lst1[i] * 10) % 10) / 10), 10) 
    if count !=0:
        lst2.append(count)
  
max_count = max(lst2)
min_count = min(lst2)
result = float (max_count - min_count)

print(result) 