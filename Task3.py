# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Минимальное значение дробной части отличное от нуля, у целых чисел дробной части нет их в расчет не берем

# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


lst = list(map(float, input("Введите числа через пробел:\n").split()))
new_lst = [round(i%1,2) for i in lst if i%1 != 0]
print(f'Разница между мексимальным и минимальным значением дробной части элементов -> {max(new_lst) - min(new_lst)}')