def step_for_similar_arrays(file) -> int:

    array = []
    res = 0

    with open(file, encoding='UTF-8') as file:
        for line in file:
            array.append(int(line.rstrip('\n')))

    closest_num = (sum(array) // len(array)) + 1

    for num in array:
        res += abs(closest_num - num)

    return res


assert step_for_similar_arrays('file.txt') == 16
assert step_for_similar_arrays('file1.txt') == 21


def main():
    import os

    current_directory = os.path.dirname(os.path.abspath(__file__))
    file = current_directory + input()

    print(step_for_similar_arrays(file))


if __name__ == '__main__':
    main()
