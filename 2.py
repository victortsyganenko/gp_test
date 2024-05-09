from statistics import mean


if __name__ == "__main__":
    m = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]

    print(f'Общее количество чисел: {sum(len(item) for item in m)}')
    print(f'Общая сумма чисел: {sum(list(sum(item) for item in m))}')
    print(f'Cреднее значение: {mean(num for item in m for num in item)}')
    print(f'Все числа из множеств в одином кортеже: {tuple(num for item in m for num in item)}')
