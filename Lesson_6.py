class Worker:
    name = "Jhon"
    surname = "Wilson"
    position = "Driver"
    income = 30000
    def __init__(self):
        self._income = {"wage":30000, "bonus":10000}

class Position:
    name = "Jhon"
    surname = "Wilson"
    position = "Driver"
    income = 30000
    def __init__(self, name, surname, position):
        self.get_full_name = print(f'Имя = {self.name} Фамилия = {self.surname} Должность = {self.position}')
        self.get_total_income = print(f'Доход с учетом премии {worker_1._Worker_income[wage] * worker_1._Worker_income[bonus]}')

worker_1 = Worker()
position_1 = Position("Jhon", "Wilson", "Driver")
print(position_1.name)






class TrafficLight:
# атрибуты
    green_1 = "Зеленый"
    yellow_1 = "Желтый"
    red_1 = "Красный"

    def __init__(self):
        self.__running = "Запуск"
        self.red = "7"
        self.yellow = "2"
        self.green = "10"

TL = TrafficLight()
print(TL._TrafficLight__running, TL.red_1, TL.red)
print(TL._TrafficLight__running, TL.yellow_1, TL.yellow)
print(TL._TrafficLight__running, TL.green_1, TL.green)


class Road:

    def __init__(self, length, width):
        self.length = length
        self.width = width
        print(f'Масса асфальта = {(self.length * self.width * 25 * 0.5) / 100}')


road_1 = Road(20, 5000)


class Machine:

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def __str__(self):
        print(f'Скорость{self.speed}, Цвет{self.color}, Название{self.name}')


car = Machine('120 км/ч', "White", "BMW")
print(str(car))
