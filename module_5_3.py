class House:
    def __init__(self, name, number_of_floors):
        # Уникальные характеристики класса
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        # Метод проверяет новый заданный этаж на наличие такого в классе House.
        # Если такой этаж есть, то выводит от одного до нового этажа значения (включительно)
        if new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        elif new_floor < 1:
            print("Такого этажа не существует")
        else:
            for floor in range(1, new_floor + 1):
                print(floor)

    def __eq__(self, other):
        # Метод определяющий равны значения number_of_floors двух классов House
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        # Метод определяющий меньше значение number_of_floors класса House первого чем второго
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        # Метод определяющий равен или меньше значение number_of_floors класса House первого чем второго
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        # Метод определяющий больше значение number_of_floors класса House первого чем второго
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        # Метод определяющий равен или больше значение number_of_floors класса House первого чем второго
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        # Метод определяющий неравен значение number_of_floors класса House первого и второго
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return House(self.name, self.number_of_floors)

    def __radd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return House(self.name, self.number_of_floors)

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return House(self.name, self.number_of_floors)

    def __len__(self):
        # Магический метод, возвращает количество этажей объекта класса House
        return self.number_of_floors

    def __str__(self):
        # Магический метод, выводит информацию о объекте классе House
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'


# Создание нововых объектов класса House
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
