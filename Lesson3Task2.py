# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#    Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

lst = [10, 2, 39, 8, -3, 9, 7, 9, 5]
# listproizv = []
# p = 1
# (len(lst)/2)
#
# for i in range(1, len(lst)):
#     p = lst[-i-1] * lst[i]
#     if -i-1 < - (len(lst)/2) - 0.5:
#         listproizv.append(p)
#
#
# listproizv.reverse()
# print(listproizv)


#  New version
multiply_1 = list([v for k, v in enumerate(lst, start=1) if k < (len(lst)/2)])
multiply_2 = list([v for k, v in enumerate(lst, start=1) if k > (len(lst)/2)+1])

multiply_2.reverse()
for i, j in zip(multiply_1, multiply_2):
    print(i*j)

