class House:
    def __init__(self, number_of_floors):
        self.__number_of_floors = number_of_floors

    def number_of_floors(self):
        return self.__number_of_floors


house = House(10)

for i in range(house.number_of_floors()):
    print(f"Текущий этаж равен {i+1}")
