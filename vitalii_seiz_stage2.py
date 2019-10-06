'''
Exercise 1 (done)
Задача: создать базовый клас который описывает геометрическую фигуру (можно абстрактный). Так же нужно создать класы
которые описывают элипс, круг, треугольник, равнобедренный треугольник, равносторонний треугольник, прямоугольник, квадрат.
Все классы должны иметь методы вычисления площади и периметра.
'''

from math import pi, sqrt

class Figure:
    def __init__(self, *args):
        self.count_area = 0
        self.count_perimeter = 0
        keys = ['a', 'b', 'c']
        i = 0
        for value in args:
            if i > 2: break
            setattr(self, keys[i], value)
            i += 1

    def print_area(self):
        print("{} Area: {}".format(self.__class__.__name__, self.count_area))

    def print_perimeter(self):
        print("{} Perimeter: {}".format(self.__class__.__name__, self.count_perimeter))

class Rectangle(Figure):
    def __init__(self, *args):
        super().__init__(*args)

    def area(self):
        self.count_area = self.a * self.b
        self.print_area()

    def perimeter(self):
        self.count_perimeter = 2 * (self.a + self.b)
        self.print_perimeter()

class Square(Rectangle):
    def __init__(self, *args):
        super().__init__(*args)
        self.b = self.a

class Ellipse(Figure):
    '''
    a and b: полуоси
    '''
    def __init__(self, *args):
        super().__init__(*args)

    def area(self):
        self.count_area = pi * self.a * self.b
        self.print_area()

    def perimeter(self):
        self.count_perimeter = 2 * pi * sqrt((self.a ** 2 + self.b ** 2)/2)
        self.print_perimeter()

class Circle(Ellipse):
    '''
    a: radius
    '''
    def __init__(self, *args):
        super().__init__(*args)
        self.b = self.a

class Triangle(Figure):
    '''
    a b c: sides
    '''
    def __init__(self, *args):
        super().__init__(*args)

    def perimeter(self):
        self.count_perimeter = (self.a + self.b + self.c)/2
        self.print_perimeter()

    def area(self):
        self.p = (self.a + self.b + self.c)/2
        self.count_area = sqrt(self.p*(self.p - self.a)*(self.p - self.b)*(self.p - self.c))
        self.print_area()

class IsoscelesTriangle(Triangle):
    '''
    a = c: side
    b: base
    '''
    def __init__(self, *args):
        super().__init__(*args)
        self.c = self.a

class EquilateralTriangle(IsoscelesTriangle):
    '''
    a = b = c: side
    '''
    def __init__(self, *args):
        super().__init__(*args)
        self.b = self.a

'''
Exercise 2 (done)
реализуйте класс "BrokenCalc", у которого неправильно работают все функции
пример вызова: brocen_calc_instance.function(arg1, arg2)
перечень неисправностей:
сложение - возвращает разность
вычитание - сумму
деление - возвращает первое число в степени второго
умножение двух чисел - строку, скомпонованную из них
возведение числа в степень должно поменять местами число и степень, 
и вернуть вычисленный результат("2 в степени 3" должно вернуть "3 в степени 2" = 9)
корень из числа всегда возвращает ноль

звёздочка*: реализации методов сложения, вычитания, умножения должны уметь работать с любым количеством входных аргументов:

>>> brocen_calc_instance.add(2, 3, 4, 5, 6) # 2 - 3 - 4 - 5 - 6
<<< -16
'''
class BrokenCalc:
    def add(*args):
        result = args[0]
        for value in args[1:]:
            result -= value
        return result

    def sub(*args):
        unsub = -sum(args[1:])
        return BrokenCalc.add(args[0], unsub)

    def truediv(*args):
        return args[0] ** args[1]

    def mul(*args):
        return ''.join(map(str, args))


    def pow(*args):
        return args[1] ** args[0]

    def sqrt(*args):
        return 0

'''
R = Rectangle(1, 2)
R.area()
R.perimeter()
Sq = Square(5)
Sq.area()
Sq.perimeter()
El = Ellipse(1, 2)
El.area()
El.perimeter()
Ci = Circle(3)
Ci.area()
Ci.perimeter()
Tr = Triangle(3, 4, 5)
Tr.area()
Tr.perimeter()
Iso = IsoscelesTriangle(2, 3)
Iso.area()
Iso.perimeter()
Eqt = EquilateralTriangle(2)
Eqt.area()
Eqt.perimeter()

brocen_calc_instance = BrokenCalc
print(brocen_calc_instance.add(2, 3, 4, 5, 6))
print(brocen_calc_instance.sub(1, 2, 3, 4))
print(brocen_calc_instance.truediv(1, 2))
print(brocen_calc_instance.mul(1, 344, 4, 5, 33))
print(brocen_calc_instance.pow(2, 3))
print(brocen_calc_instance.sqrt(22))
'''

'''
Exercise 3 (in progress)
Задача со звездочкой:
Создать структуру данных типа дерево. Каждый узел дерева должен иметь строковое представление в виде "путь к вершине".
Имплементировать методы который позволяют обходить дерево горизонтально и вертикально.
'''
class Node:
    def __init__(self, name, parent=None):
        self.name = str(name)
        self.parent = parent
        self.children = []

        if parent:
            self.parent.children.append(self)
            self.name += self.parent.name

def create_random_nodes():
    pass

root = Node(1)
a12 = Node('a', root)
a13 = Node('a', root)
a14 = Node('a', root)
a21 = Node(3, a12)
a22 = Node(4, a12)
a23 = Node(7, a13)
a24 = Node(25, a12)
a25 = Node(31, a12)
a31 = Node(22, a13)
a4421 = Node(14, a23)

def print_tree(node, file=None, _prefix="", _last=True):
    print(_prefix, "`- " if _last else "|- ", node.name, sep="", file=file)
    _prefix += "   " if _last else "|  "
    child_count = len(node.children)
    for i, child in enumerate(node.children):
        _last = i == (child_count - 1)
        print_tree(child, file, _prefix, _last)

print_tree(root)
'''
Exercise 4 (failed)
Логирование. Необходимо реализовать логирование при помощи классов. Класс логирования должен обеспечивать возможность 
как записи в текстовьій файл, так и вьівод на консоль и оба. В зависимости от переданного параметра.
Простор для творчества ваш.
Форматирование не обязательно, достаточно вьіводить время, помимо сообщения.Внимание, использовать стандартную библиотеку нельзя.Со звездочкой ;)
P.S. Копировать решение из стандартной библиотеке - не красиво в плане обучения. Либо решайте сами, либо пропускайте задачу.
Пример использования:

... your code ...
logger = <YOUR LOGGER CLASS>(... params...)
logger.log(message)

Что под капотом - ваша реализация. Главное что б работало)
'''


'''
Exercise 5 (done without stars)
напишите класс "Elevator" для предположим N этажного дома. объект данного класса должен уметь:
- перемещаться между этажами (без возможности провалиться в адъ, улететь в космос).
 скорость движения лифта - 1 этаж в секунду. соответственно с 1-го на 10-й он должен ехать 9 секунд
- не перемещаться, если лифт перегружен (разрешенный вес выберите сами)
- при каждом изменении состояния выводить в консоль текущий этаж
- print() на объекте должен выводить текущую информацию о лифте (этаж, загруженность)

- звёздочка* - реализуйте возможность экстренной остановки лифта на текущем этаже (узнать как выглядят входные данные)
- звёздочка* - реализуйте возможность подбирать людей при движении вниз. пример: если едем с эт.10 на эт.1,
 должна быть возможность остановить лифт на эт.5, после чего автоматически продолжить движение. (узнать как выглядят входные данные)
'''
import time

class Elevator:
    max_floor = 5
    min_floor = 1
    floor = 1
    weight = 2
    max_weight = 200

    def move(self, n):
        '''
        n > 0: up
        n < 0: down
        '''
        if self.weight > self.max_weight: return print("Overload: max weight {} kg".format(self.max_weight))
        down_up = 1
        if n < 0:
            down_up = -1
        for i in range(abs(n)):
            if self.min_floor < self.floor < self.max_floor or (self.floor == self.max_floor and down_up < 0) or \
                    (self.floor == self.min_floor and down_up > 0):
                self.floor += down_up
                self.floor_now()
            else:
                break


    def floor_now(self):
        time.sleep(1)
        print("Этаж: {}".format(self.floor))

    def print(self):
        print("Этаж: {} Загруженность: {}".format(self.floor, self.weight))

user = Elevator()
user.weight = 101
user.move(13)
user.print()
user.move(-14)
user.print()
user.move(15)
user.weight = 1001
user.move(-2)

