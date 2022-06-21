def main():

    total = []

    total_num = 0

    num = float(input(
        "Введите число, которое хотите добавить для вычисления среднего арифметического: "))

    total.append(num)

    again = int(input("'1' - Введите, чтобы добавить ещё"))

    while again == 1:
        num = float(input(
            "Введите число, которое хотите добавить для вычисления среднего арифметического: "))

        total.append(num)

        again = int(input("'1' - Введите, чтобы добавить ещё: "))

    length_list = len(total)

    for numbers in total:
        total_num += numbers

    answer = total_num / length_list

    print(f"Среднее арифметическое: {answer}")


main()
