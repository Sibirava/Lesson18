#init - конструктор
#def __del__ (self):  #деструктор

# ОПИСЫВАЕМ КЛАСС!!!!

class Rectangle:
    def __init__(self, a=1, b=1):  #дефолтные значения параметров (конструктор с параметрами)
        self.a = a
        self.b = b

    def calculate_square(self):
        return self.a * self.b

    def calculate_perimeter(self):
        return (self.a + self.b) * 2

    # def get_info(self):
    #     return f"Rectangle: a = {self.a}, b = {self.b}"

    def __repr__(self):     # описывает технические параметры
        return f"Technical information about instance"

    def __str__(self):       # с точки зрения предметной области, строковый эквивалент
        return f"Rectangle: a = {self.a}, b = {self.b}"

# rect = Rectangle()
# print(rect)



# rect1 = Rectangle(10, 15)   #вызывает один и тот же конструктор
# rect2 = Rectangle(b=15)     # значит а будет по дефолту
# rect3 = Rectangle(20, 10)
# rect4 = Rectangle(20)        #а инициализируется, а б по дефолту
# rect5 = Rectangle()          # значения по умолчанию

# print(rect1.get_info())
# print(rect2.get_info())
# print(rect3.get_info())
# print(rect4.get_info())
# print(rect5.get_info())


