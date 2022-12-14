# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n 
# и выведите на экран их сумму.

#     Для n = 6: [2, 2, 2, 2, 2, 3] -> 13

import math

num=int(input("Введите целое число: "))
num = num if num>=0 else -num

def list_gen(num):  # заполнение массива--------------------------------------------------------------
    array=[0]*num
    for i in range(1, num+1):
        array[i-1]=round(((1+1/i)**i)) 
    return array
# end ------------------------------------------------------------------------------------------------

def sum_elements(array):  #  расчет суммы элементов массива------------------------------------------
    sum=0
    for j in array:
        sum+=j
    return sum
# end ------------------------------------------------------------------------------------------------

array=list_gen(num)
print(array)
sum=sum_elements(array)
print(f"Сумма элементов - {sum}")