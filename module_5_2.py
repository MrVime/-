class House:
    def __init__(self, name, number_of_floors):
        #Уникальные характеристики класса
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

    def __len__(self):
        # Магический метод, возвращает количество этажей объекта класса House
        return self.number_of_floors

    def __str__(self):
        # Магический метод, выводит информацию о объекте классе House
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

#Создание нововых объектов класса House
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__   выводит информацию о объекте классе House
print(h1)
print(h2)

# __len__ выводит количество этажей объекта класса House
print(len(h1))
print(len(h2))
