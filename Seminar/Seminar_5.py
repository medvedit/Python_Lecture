
# Задача №1: --------------------------------------------------------------------------------------------------------------

# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.

# Ввод:
# values = [1, 23, 42, ‘asdfg’]
# transformed_values = list(map(trasformation, values))
# if values == transformed_values:
#     print(‘ok’)
# else:
#     print(‘fail’)
# Вывод:
# ok

values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
transformed_values = list(map(lambda x: x, values))
if values == transformed_values:
    print('ok')
else:
    print('no')

print(values)
print(transformed_values)

# Задача №2: --------------------------------------------------------------------------------------------------------------

# Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту,
# орбита которой имеет самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits),
# которая среди списка орбит планет найдет ту, по которой вращается самая далекая планета.
# Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет,
# зато искусственные спутники были были запущены на круговые орбиты. Результатом функции должен быть кортеж,
# содержащий длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита представляет из себя
# кортеж из пары чисел - полуосей ее эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи используйте списочные выражения.
# Подсказка: проще всего будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса,
# а затем найти и сам эллипс, имеющий такую  площадь. Гарантируется, что самая далекая планета ровно одна

# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))

# Вывод:
# 2.5 10

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

def find_farthest_orbit(orbits):
    s = [3.14*max(x)*min(x) if max(x) != min(x) else 0 for x in orbits]
    return(orbits[s.index(max(s))])

print(*find_farthest_orbit(orbits))

# Или

from math import pi

# S=pi*a*b
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]


def find_farthest_orbit(list_of_orbits):
    s_max = 0
    index = 0
    list_s = []

    def sqare(a, b):
        return pi * a * b

    for i in range(len(list_of_orbits)):
        x = list_of_orbits[i][0]
        y = list_of_orbits[i][1]
        if x != y:
            if sqare(x, y) > s_max:
                s_max = sqare(x, y)
                index = i
    list_s.append(pi * list_of_orbits[i][0] * list_of_orbits[i][1])

    return [list_of_orbits[index], s_max]


print(find_farthest_orbit(orbits))

# Или

from math import pi

def find_farthest_orbit(list_of_orbits):
    temp_list = ((pi * i[0] * i[1], i[0], i[1]) for i in list_of_orbits if i[0] != i[1])
    MAX =  max(temp_list)
    return MAX[1], MAX[2]

orbits = [(1, 3), (2.5, 10), (7, 2), (10, 10), (4, 3)]
print(*find_farthest_orbit(orbits))

# Задача №3: --------------------------------------------------------------------------------------------------------------

# Напишите функцию same_by(characteristic, objects), которая проверяет,
# все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов отличается - то False. Для пустого набора объектов,
# функция должна возвращать True. Аргумент characteristic - это функция, которая принимает объект и
# вычисляет его характеристику.


values = [0, 3, 12, 6]

def same_by(func, val):
    return True if len(set(map(func, val))) == 1 or 0 else False

print(same_by(lambda x: x%2, values))

# Или...

values = [0, 2, 12, 6]

def same_by(characteristic, objects):
    f = set(list(map(characteristic,objects)))
    return len(f)==1

print(same_by(lambda x: x%2, values))

# Или...

values = [0, 2, 10, 7]

def same_by(f, list_num):
    # return set(map(f, list_num))
    return True if len(set(map(f, list_num))) == 1 else False

print(values)
print(same_by(lambda x: x % 2, values))

# ==================================================================================== Дополнительные задачи ==================================================================================
# * Задача 101: ________________________________________________
# Вычислить число π c заданной точностью d

# Пример:
# при d = 0.001, π = 3.141    0.1 ≤ d ≤ 0.00000000001

from decimal import Decimal
import math

number = Decimal(math.pi)
precision_number = Decimal(input('Введите точность: '))

number_out = number.quantize(Decimal(precision_number))

print(number_out)

# * Задача 102: ________________________________________________
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = 99800

def prime_factors_number(n:int) -> list:
    out = []
    for i in range(2, n + 1):
        while not n % i:
            n //= i
            out.append(i)
            if n == 1:
                break
    return out

print(n) # 99800
print(prime_factors_number(n)) # [2, 2, 2, 5, 5, 499]


# * Задача 105: ________________________________________________
# Напишите программу, удаляющую из текста все слова, содержащие "ла".

text = 'Через 20 лет вы будете больше разочарованы теми вещами, \
        которые вы не делали, чем теми, которые вы сделали. Так отчальте от тихой пристани. \
        Почувствуйте попутный ветер в вашем парусе. Двигайтесь вперед, действуйте, открывайте!'


del_word = 'ла'
text = [i for i in text.split() if del_word not in i]
print(" ".join(text))




# ===================================================================================== Домашняя работа ==========================================================================

# Задача 26: ___________________________________________________________
# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

ch = 2
st = 4

def degree_recursion(x, y):
    if y > 1:
        return x * degree_recursion(x, y - 1)
    return x

print(degree_recursion(ch, st))


# Задача 28: ____________________________________________________________________________________
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.


def sum_num(A, B):
    if (B==0):
        return A
    else:
        return sum_num(A+1,B-1)

a = int(input('Input A>>'))
print()
b = int(input('Input B>>'))
print()
if (a>=b):
    print (sum_num(a,b))
else:
    print(sum_num(b,a))






