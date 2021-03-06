'''
Задача 1.
Напишите программу, которая принимает на вход цифру, обозначающую день недели,
и проверяет, является ли этот день выходным.
Пример:
- 6 -> да
- 7 -> да
- 1 -> нет
'''
#Решение задачи 1
'''
n = int(input("Введите порядковый номер дня недели "))
if (n < 1 or n > 7): print("В неделе 7 дней")
elif (1 <= n <= 5): print("Будний день")
else: print("Выходной день")
'''


'''
Задача 2.
Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
для всех значений предикат.
'''
#Решение задачи 2
'''
for x in range(2):
    for y in range(2):
        for z in range(2):
            print (x, y, z, (not(x or y or z)) == (not x and not y and not z))
'''


'''
Задача 3.
Напишите программу, которая принимает на вход координаты точки (X и Y),
причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
в которой находится эта точка (или на какой оси она находится).
Пример:
- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3
'''
#Решение задачи 3
#      В условии неточноть - если координаты явно не равны 0,
#      тогда точка не может лежать на какой-либо из осей.
'''
x, y = map(int, input("Введите координаты X и Y ").split())
if (x == 0 or y == 0): print("Ни одна из координат не должна быть нулевой")
else:
    if (x > 0 and y > 0): print("Первая четверть")
    elif (x < 0 and y > 0): print("Вторая четверть")
    elif (x < 0 and y < 0): print("Третья четверть")
    else: print("Четвертая четверть")
'''


'''
Задача 4.
Напишите программу, которая по заданному номеру четверти показывает
диапазон возможных координат точек в этой четверти (x и y).
'''
#Решение задачи 4
'''
n = int(input("Введите номер четверти "))
if (n < 1 or n > 4): print("Это не номер четверти")
else:
    if (n == 1): print("X принадлежит (0;+inf), Y принадлежит (0;+inf)")
    elif (n == 2): print("X принадлежит (0;-inf), Y принадлежит (0;+inf)")
    elif (n == 3): print("X принадлежит (0;-inf), Y принадлежит (0;-inf)")
    else: print("X принадлежит (0;+inf), Y принадлежит (0;-inf)")
'''


'''
Задача 5.
Напишите программу, которая принимает на вход координаты двух точек
и находит расстояние между ними в 2D пространстве.
Пример:
- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
'''
#Решение задачи 5
'''
xA, yA, xB, yB = map(int, input("Введите координаты точек в формате: xA yA xB yB ").split())
print(round(((xA - xB) ** 2 + (yA - yB) ** 2) ** 0.5, 2))
'''

'''
Дополнительная задача.
Кузнечик прыгает по столбикам, расположенным на одной линии на равных расстояниях
друг от друга. Столбики имеют порядковые номера от 1 до N. В начале Кузнечик сидит
на стобике с номером 1. Он может прыгнуть на следующий столбик или сразу на второй
столбик, считая от текущего. Требуется найти количество способов, которыми Кузнечик
может добраться до столбика с номером N. Учитывайте, что Кузнечик не может прыгать назад.
Входная строка - N натуральное (1 <= N <= 45)
Выходная строка - число (количество способов)
Пример:
3 -> 2
10 -> 55 
'''
#Решение дополнительной задачи
'''
N = int(input("Введите номер столбика "))
if (N < 1): print("Кузнечик не может прыгать назад")
elif (N == 1): print("Кузнечик уже на первом столбике.")
elif (N == 2): print(1)
else:
    count = [0 for i in range(N)]
    count[1] = 1
    count[2] = 2
    for i in range(3, N):
        count[i] = count[i - 1] + count[i - 2]
    print(count[N - 1])
'''