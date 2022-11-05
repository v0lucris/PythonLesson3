# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
#    Пример:
#- для k = 8 список будет выглядеть так:
#  [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

count = int(input('Write count: '))
lst = [] 
lst2 = []
fib1 = 0
fib2 = 1
fib3 = 0
fib4 = - 1
#print(fib1, fib2, end=' ')
for i in range(1, count + 1):
    fib3, fib4 = fib4, fib3 + fib4
    #print(fib2, end=' ')
    lst2.append(fib3)
lst2.reverse()     
for i in range(1, count + 1):
    fib1, fib2 = fib2, fib1 + fib2
    #print(fib2, end=' ')
    lst.append(fib1)
lst3 = lst2 + lst
for i in range(-count-1, count + 1):
    if lst3[i] == -1 and lst3[i+1] == 1:    
        lst3.insert(lst3.index(lst3[i+1]),0)
        print(lst3)



#print(lst3)