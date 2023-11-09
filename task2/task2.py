# ещё хочу реализовать новый файл с координатами который заполнится функцией рандом
def point_relative_to_circle(circle, dots):

    dots_list = []

    with open(circle, 'r', encoding='utf8') as file1:
        x_circle, y_circle = map(float, list(file1.readline().rstrip('\n').split()))
        rad_circle = float(file1.readline().rstrip('\n'))

    with open(dots, 'r', encoding='utf8') as file2:
        for line in file2:
            dots_list.append(line.rstrip('\n'))
        # dots = file2.read().rstrip('\n')

    for xy in dots_list:
        x, y = map(float, list(xy.split()))
        formula = (x - x_circle) ** 2 / rad_circle ** 2 + (y - y_circle) ** 2 / rad_circle ** 2
        if formula < 1:
            print('1-точка внутри')
        elif formula == 1:
            print('0-точка лежит на окружности')
        else:
            print('2-точка снаружи')


def main():
    import os

    current_directory = os.path.dirname(os.path.abspath(__file__))
    file1 = current_directory + "\\file1.txt"
    file2 = current_directory + "\\file2.txt"

    point_relative_to_circle(file1, file2)


if __name__ == '__main__':
    main()
