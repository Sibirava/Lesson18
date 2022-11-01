from rectangle_creator import RectangleCreator
from logic import Logic
from view import View

def main():
    size = 200

    ls = RectangleCreator.get_rectangles(size)
    total_square = Logic.calculate_total_square(ls)
    total_perimeter = Logic.calculate_total_perimeter(ls)

    msg = (f"Total square = {total_square}\n"
           f"Total perimeter = {total_perimeter}")

    print(View.convert(ls))
    print(msg)



if __name__ == "__main__":
    main()