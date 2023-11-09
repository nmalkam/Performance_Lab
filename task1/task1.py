def circular_array(n: int, m: int) -> int | str:

    c_array = []
    intervals = []
    part_interval = [0]
    res = ''
    pointer = 1

    for element in range(1, n + 1):
        c_array.append(element)

    while part_interval[-1] != 1:
        part_interval = []
        pointer -= 1
        for num in range(1, m + 1):
            part_interval.append(c_array[pointer])
            pointer += 1
            if pointer == n:
                pointer = 0
        intervals.append(part_interval)

    for _ in intervals:
        res += str(_[0])
    return res


assert circular_array(4, 3) == '13'
assert circular_array(5, 4) == '14253'
assert circular_array(3, 6) == '132'


def main():

    n = int(input())
    m = int(input())

    print(circular_array(n, m))


if __name__ == '__main__':
    main()
