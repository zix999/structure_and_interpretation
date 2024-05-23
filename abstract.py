from abc import ABC, abstractmethod  # оно нужно для создания абстрактного базового класса


# В общем случае основная идея абстракции данных состоит в том, чтобы определить для каждого типа объектов данных
# набор базовых операций, через которые будут выражаться все действия с объектами этого типа, и затем при работе с
# данными использовать только этот набор операций.

class Vehicles(ABC):  # вот это набор базовых операций
    @abstractmethod
    def move_mode(self):  # перегруженный метод
        pass

    @abstractmethod
    def engine_count(self):  # перегруженный метод
        pass


class Car(Vehicles):
    def move_mode(self):
        print("Катается по суше и немного по воде")

    def engine_count(self):
        print("1")


class Boat(Vehicles):
    def move_mode(self):
        print("Катается по воде")

    def engine_count(self):
        print("1")


class Plane(Vehicles):
    def move_mode(self):
        print("Рассекает воздух, по траектории")

    def engine_count(self):
        print("4")


class Helicopter(Vehicles):
    def move_mode(self):
        print("Свободно двигается по воздуху")

    def engine_count(self):
        print("2")


C = Car()
C.move_mode()
C.engine_count()

B = Boat()
B.move_mode()
B.engine_count()

P = Plane()
P.move_mode()
P.engine_count()

H = Helicopter()
H.move_mode()
H.engine_count()
