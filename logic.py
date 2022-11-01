from rectangle import Rectangle

class Logic:
    def calculate_total_square(rectangles):
        if isinstance(rectangles, (list, tuple)):  #проверяет что rectangles является списком или тьюплом
            total = 0
            for rect in rectangles:
                if isinstance(rect, Rectangle):   #проверить что rect действительно из Rectangle
                    total += rect.calculate_square()
            return total


    def calculate_total_perimeter(rectangles):
        if isinstance(rectangles, (list, tuple)):  #проверяет что rectangles является списком или тьюплом
            total = 0
            for rect in rectangles:  #проверить что rect действительно из Rectangle
                if isinstance(rect, Rectangle):
                    total += rect.calculate_perimeter()
            return total