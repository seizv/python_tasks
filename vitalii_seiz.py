def arithmetic(num1, num2, operation):
    #Exercise 1
    '''
    Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий -
    операция, которая должна быть произведена над ними. Если третий аргумент +, сложить
    их; если --, то вычесть; * — умножить; / — разделить (первое на второе). В остальных
    случаях вернуть строку “Неизвестная операция”.
    '''
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return 'Один или более аргуметов не число'
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return (num1 / num2) if num2 != 0 else 'Нелья делить на ноль'
    else:
        return 'Неизвестная операция'

def is_year_leap(year):
    # Exercise 2
    '''
    Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую
    True, если год високосный, и False иначе.
    '''
    return True if (year % 400 == 0 or year % 4 == 0 and year % 100 != 0) else False

def square(side):
    # Exercise 3
    import math
    '''
    Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвраща-
    ющую 3 значения (с помощью кортежа): периметр квадрата, площадь квадрата и диаго-
    наль квадрата.
    '''
    p = 4 * side
    s = side ** 2
    diag = side * math.sqrt(2)
    answer = p, s, diag
    return answer

def season(month):
    # Exercise 4
    '''
    Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12),
     и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).
    '''
    season_dict = {
        'winter': (12, 1, 2),
        'spring': (3, 4, 5),
        'summer': (6, 7, 8),
        'autumn': (9, 10, 11)
    }
    for key, val in season_dict.items():
        if month in val:
            return key
    return None

def bank(a, year):
    # Exercise 5
    '''
    Пользователь делает вклад в размере a рублей сроком на years лет под 10% годовых (каждый год размер его вклада
    увеличивается на 10%. Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).
    Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму,
    которая будет на счету пользователя.
    '''
    start = 0
    percent = 0.1
    while start < year:
        a += a*percent
        start += 1
    return a

def is_prime(num):
    # Exercise 6
    '''
    Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000,
     и возвращающую True, если оно простое, и False - иначе.
     ***Можно всё оптимизировать лучше
    '''
    if num == 0 or num == 1: return False
    for x in range(2, int(num/2)):
        if num % x == 0:
            return False
    return True

def date(day, month, year):
    # Exercise 7
    '''
    Написать функцию date, принимающую 3 аргумента — день, месяц и год. Вернуть True,
    если такая дата есть в нашем календаре, и False иначе.
    '''
    day_in_month = {(1, 3, 5, 7, 8, 10, 12): 31,
                    (4, 6, 9, 11): 30,
                    (2, 2): 29 if is_year_leap(year) else 28
                    }

    for i in day_in_month.keys():
        if i.count(month):
            if day_in_month[i] >= day:
                return True
    else:
        return False


def sortedMassive():
    # Exercise 9.1
    '''
    - Из двух отсортированных массивов сделать третий отсортированный, не сортируя его. (Вариант1)
    '''
    list1_sort = (1, 2, 3, 5, 6, 8, 10, 23)
    list2_sort = (0, 5, 7, 9, 23, 72)
    list3_result = []
    i1, i2 = 0, 0
    len1, len2 = len(list1_sort), len(list2_sort)

    while i1 < len1 and i2 < len2:
        if list1_sort[i1] <= list2_sort[i2]:
            list3_result.append(list1_sort[i1])
            i1 += 1
        else:
            list3_result.append(list2_sort[i2])
            i2 += 1

    return list3_result + list(list1_sort[i1:] + list2_sort[i2:])

def sortedMassive2():
    # Exercise 9.2
    '''
    - Из двух отсортированных массивов сделать третий отсортированный, не сортируя его. (Вариант2)
    '''
    list1_sort = [1, 2, 3, 5, 6, 8, 10, 23, 33]
    list2_sort = [0, 5, 7, 9, 23, 72]
    list3_result = []

    while list1_sort:
        if not list2_sort:
            list3_result += list1_sort
            break
        if list1_sort[0] <= list2_sort[0]:
            list3_result.append(list1_sort.pop(0))
        else:
            list3_result.append(list2_sort.pop(0))
    else:
        list3_result += list2_sort

    return list3_result

def year_leaps_interval(a, b, c):
    # Exercise 10
    '''
    Напишіть функцію, яка приймає на вхід три параметри: початковий рік (a), кінцевий рік (b), список років (c).
    Функція має повертати список високосних років між а і b, крім вказаних у списку c
    ***Задачу делал без проверок на входные данные
    '''
    leaps_result = []
    while a <= b:
        if is_year_leap(a) and a not in c:
            leaps_result.append(a)
        a += 1
    return leaps_result

def fib(a, b):
    # Exercise 11
    '''
    Написать метод который принимет два числа a, b и возвращает все числа Фибоначчи на отрезке [a, b] (будем считать включительно)
    ***Задачу делал без проверок на входные данные
    ***Будем считать что последовательность начинается c 0
    '''
    fib1 = 0
    fib2 = 1
    fib_result = []
    while fib1 <= b:
        if fib1 >= a:
            fib_result.append(fib1)
        fib1, fib2 = fib2, fib2 + fib1
    return fib_result

def odds():
    # Exercise 12
    '''
    получить список всех нечётных чисел от 0 до 100
    со звёздочкой - сделайте это в одну строку
    return list(range(1, 101, 2)) (со звездочкой)
    return list (x for x in range(101) if x % 2 !=0) (или так)
    '''
    start = 0
    finish = 100
    odds_result = []
    while start < finish:
        if start % 2 != 0:
            odds_result.append(start)
            start += 1  # так мы пропустим сразу все чётные)
        start += 1
    return odds_result

def types(a, b):
    # Exercise 13
    '''
    напишите метод, который принимает на вход два параметра: a и b
    если тип обоих переменных (a и b) - int, вывести большее из них
    если тип обоих переменных строка - сообщить, является ли строка b подстрокой строки a
    если переменные разного типа, вывести сообщение об ошибке (любое)
    '''
    if isinstance(a, int) and isinstance(b, int):
        return a if a > b else b
    elif isinstance(a, str) and isinstance(b, str):
        return True if b in a else False
    elif type(a) == type(b):
        return "a and b same types"
    else:
        return "Error: a and b different types"

def list_sum():
    # Exercise 14
    '''
    - Найти сумму элементов массива
    '''
    list1 = [1, 2, 3, -5, 3, 0]
    result = 0
    for i in list1:
        result += i
    return result

def max_and_min():
    # Exercise 15.1 and 15.2
    '''
    - Найти максимальный элемент, значение и индекс
    - Найти минимальный элемент, значение и индекс
    '''
    list1 = [1, 21, 4, 5, 7, 21, 0]
    if not list1: return None
    max_elem = min_elem = list1[0]
    for i in list1:
        if max_elem < i: max_elem = i
        if min_elem > i: min_elem = i
    return "Max element {0} his index {1}\nMin element {2} his index {3}".format(max_elem, list1.index(max_elem), min_elem, list1.index(min_elem))

def count_positiv():
    # Exercise 16
    '''
    - Посчитать количество элементов больше нуля
    '''
    list1 = [1, 21, -4, 5, 7, 21, 0]
    return len(list(x for x in list1 if x > 0))

def add_index():
    # Exercise 17
    '''
    - Прибавить к элементам массива их индекс
    '''
    list1 = [1, 2, 7, 9, 0, -1, 8]
    len1 = len(list1)
    for i in range(len1):
        list1.append(i)
    return list1

def slice_right():
    # Exercise 18
    '''
    - Циклический сдвиг элементов массива на k- позиций вправо
    '''
    list1 = [1, 2, 3, 4, 5, 0]
    k = 61
    if not list1: return None
    sl = len(list1) - k%len(list1)
    return list1[sl:] + list1[:sl]

def element_not_in_2nd():
    # Exercise 19
    '''
    - Вывести элементы одного массива, которые не равны элементам второго массива.
    '''
    list1 = [1, 2, 3, 4, 5]
    list2 = [6, 7, 5, 3, 4]
    return list(x for x in list1 if x not in list2)

def cups():
    '''
    # Exercise 20
    Світлана замовляє чашки для співробітників, на яких мають бути надруковані імена.
    Напишіть будь ласка функцію, що приймає на вхід список людей, у якому кожна людина описана як словник  ключами “name”, “surname”.
    А повертає структуру з іменами і кількістю чашок які потрібно замовити.
    По задачке про чашки уточню. На вход имена и фамилии всех сотрудников. На вьіходе - имена и количество чашек.
    На чашке только имя (без фамилии).
    Врахуйте, що результат функції - це по суті замовлення чашок в типографії. Наприклад, Сергій - 8 шт, Антон - 2 шт.
    '''
    input_list = [{'name': 'iavn', 'surname': 'ivanov'},
                  {'name': 'ivan', 'surname': 'ivanov'},
                  {'name': 'ioan', 'surname': 'ivanov'},
                  {'name': 'sergei', 'surname': 'ivanov'},
                  {'name': 'vasya', 'surname': 'ivanov'},
                  {'name': 'vasya', 'surname': 'ivanov2'},
                  {'name': 'ivan', 'surname': 'ivanov'},
                  {'name': 'ivan', 'surname': 'ivanov'},
                  {'name': 'ivan', 'surname': 'ivanov'},
                  {'name': 'iavn', 'surname': 'ivanov'},
                 ]
    dict_result = {}

    for people in input_list:
        if people['name'] not in dict_result:
            dict_result[people['name']] = 1
        else:
            dict_result[people['name']] += 1
    return dict_result


#-------IN PROGRESS---------
def XOR_cipher(string, key):
    #Exercise 8.1 and 8.2
    '''
    Написать функцию XOR_cipher, принимающая 2 аргумента: строку, которую нужно за-
    шифровать, и ключ шифрования, которая возвращает строку, зашифрованную путем
    применения функции XOR (^) над символами строки с ключом. Написать также функ-
    цию XOR_uncipher, которая по зашифрованной строке и ключу восстанавливает исход-
    ную строку.
    '''
    len_str, len_key = len(string), len(key)
    if len_str > len_key:
        key *= int(len_str/len_key) + 1     # длина ключа должна быть >= длины строки
    result = [chr(ord(st_r) ^ ord(ke_y)) for st_r, ke_y in zip(string, key)]
    return ''.join(result)

XOR_uncipher = XOR_cipher
print(XOR_cipher('Hellooo123!@#', '12'))
test_key = '123'
print(XOR_uncipher(XOR_cipher('Hellooo123!@#123001TrueТЕСТЖ^%*&', test_key), test_key))

'''    
# Exercise 21
chat

'''
